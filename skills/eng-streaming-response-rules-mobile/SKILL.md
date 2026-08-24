---
name: eng-streaming-response-rules-mobile
description: Use when implementing or debugging the LLM token-streaming pipeline on iOS or Android clients. Defines buffering rules, reconnection logic, RTL rendering constraints, and mobile-specific UX patterns for streaming legal AI responses — including how to handle long-form document drafts that arrive over slow or intermittent mobile connections.
license: MIT
metadata: " id: eng.streaming-response-rules-mobile category: eng jurisdictions: [__multi__] priority: P2 intent: [__eng__, streaming, mobile, sse, real-time] related: [eng-supabase-edge-functions-patterns, eng-token-budget-by-tier, eng-remotion-explainer-video-generator] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Registered as a flat plugin skill.
-->


# Streaming Response Rules — Mobile

## What it does

Streaming LLM responses (Server-Sent Events or chunked HTTP) requires careful handling on mobile clients. A chat response for a 5-page NDA draft may be 3,000+ tokens; on a 3G connection in a MENA market that can take 15–30 seconds. Without correct buffering, reconnection logic, and RTL-aware rendering, the user experience degrades significantly. This skill defines the rules mobile engineers must follow when implementing the streaming layer.

## Setup / auth

The backend streaming endpoint:
- `POST /api/chat/stream` — returns `Content-Type: text/event-stream`
- Requires `Authorization: Bearer <session_token>`
- Emits SSE events: `data: { type: "delta", content: "..." }` per token chunk, then `data: { type: "done", usage: {...} }`

For React Native, use `fetch` with `ReadableStream`; do **not** use `EventSource` (React Native does not implement it natively — use `react-native-sse` or a polyfill).

For Flutter, use `http.Client.send()` with a `StreamedResponse`.

## Capabilities

### Buffering rules

| Rule | Reason |
|---|---|
| Buffer incoming delta chunks into a string accumulator; render to UI every 50 ms (not on every token) | Prevents excessive React re-renders on fast connections |
| Flush buffer immediately on `\n\n` (paragraph break) | User sees complete paragraphs progressively, not mid-sentence |
| Flush buffer immediately on `---` (Markdown HR) | Section breaks in legal docs should be visible early |
| Never flush mid-word | Partial words in legal text look like garbled output |
| On `type: "done"`, flush remaining buffer and mark response as complete | Ensures the last partial paragraph is displayed |

### Reconnection logic

Mobile connections drop. The streaming endpoint must support reconnection:

1. On every SSE event, emit `id: <sequence_number>`.
2. Client stores `lastEventId` in memory (not persisted — session-scoped).
3. On disconnect, client waits 1s then reconnects with `Last-Event-ID: <lastEventId>` header.
4. Server resumes from that sequence number (buffer the last 200 events in Redis/memory for 5 min).
5. Maximum 3 reconnection attempts; after 3 failures, display an error with a "Resume" button that re-triggers the full request.

Do not attempt to resume a stream that has been idle > 5 minutes — the session context may have expired.

### RTL rendering for Arabic responses

- Arabic LLM output is detected by the presence of Arabic Unicode characters in the first 30 chars of the buffer.
- On detection, set `writingDirection: "rtl"` on the text container **before** appending further tokens. Switching direction mid-stream causes visual glitching.
- Use a dedicated `<RTLTextView>` (React Native) or `Text(textDirection: TextDirection.rtl)` (Flutter) that is pre-configured; do not set direction dynamically on a shared component.
- Arabic legal text requires `lineHeight` ≥ 1.8× the font size; ensure this is set before streaming begins.
- Do not apply `textAlign: "right"` independently of `writingDirection`; they interact and can produce double-alignment bugs.

### Mobile-specific UX rules

| Rule |
|---|
| Show a typing indicator for the first 500 ms before any tokens arrive |
| Show a "Stop generating" button that calls `DELETE /api/chat/stream/<requestId>` |
| Long-form document drafts (>1000 tokens): show a progress indicator ("Drafting clause 3 of 7…") derived from heading-detection in the stream |
| Do not auto-scroll while the user is scrolling upward; resume auto-scroll when they scroll back to the bottom |
| On background (app minimized): pause rendering updates; on foreground: replay from buffer — do not drop tokens |
| Haptic feedback on stream completion (iOS: `UIImpactFeedbackGenerator`, Android: `Vibrator`) |

### Token budget display

Integrate with [[eng-token-budget-by-tier]]:
- Display remaining token budget in a small pill near the input bar: "~2,400 tokens remaining this month".
- When budget < 20%, show warning color.
- When budget = 0, disable the send button before the request is made (don't let the user send and get an error mid-stream).

### Network quality adaptation

| Signal | Action |
|---|---|
| Connection type = `2g` or `slow-2g` | Warn user: "Slow connection detected — response may take longer" |
| `RTT > 500 ms` (from Network Information API) | Increase reconnection backoff to 3 s |
| `downlink < 0.5 Mbps` | Suggest switching to "Summary mode" (shorter output) |

## Permissions & safety

- The streaming endpoint must validate the session token on every reconnection, not just the initial connection. A session revoked mid-stream must result in a `401` event and stream termination.
- Never cache streaming responses in HTTP caches. Set `Cache-Control: no-store`.
- Do not log the full streamed content on the client. Log only `{ requestId, tokensReceived, latencyMs, reconnections }`.

## Failure modes

| Failure | Impact | Mitigation |
|---|---|---|
| No `lastEventId` support on server | User gets duplicate content on reconnect | Implement sequence numbers from day one |
| Direction not set before Arabic tokens arrive | Visual RTL flip mid-sentence | Detect language in first 30 chars; set direction pre-emptively |
| Buffer flushed on every token | UI janks at 30 fps on low-end Android | 50 ms flush interval via `setInterval` |
| Stream hangs after `type: "done"` never arrives | UI stuck in "thinking" state | Set a 60 s hard timeout; if no `done` after 60 s, mark complete and show retry |
| Stop button ignored | User can't cancel long draft | Implement `AbortController` on the fetch; send DELETE to cancel server-side LLM call |

## Related skills

- [[eng-supabase-edge-functions-patterns]] — the Edge Function that serves the streaming endpoint
- [[eng-token-budget-by-tier]] — token budget integration in the streaming UI
- [[eng-remotion-explainer-video-generator]] — alternative output format for long explanations
