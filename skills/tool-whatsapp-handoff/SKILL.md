---
name: tool-whatsapp-handoff
description: Use when a MENA user wants to continue a legal AI conversation on WhatsApp rather than in the web or mobile app — for example, to follow up with their lawyer, share a document, or get a chat summary on the platform they use every day. Generates a WhatsApp Business deep-link prefilled with a session summary, allowing a seamless handoff from the Louis interface to a WhatsApp thread. Particularly relevant for MENA users where WhatsApp is the dominant business communication channel.
license: MIT
metadata: " id: tool.WhatsApp-handoff category: tool jurisdictions: [__multi__] priority: P2 intent: [whatsapp, channel-handoff, mobile, mena-communication] related: [tool-web-search-orchestrator, conversation-empathy-b2c, onboarding-welcome] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# WhatsApp Handoff

## What it does

This tool generates a WhatsApp Business deep-link that carries the current conversation summary into a WhatsApp thread, enabling a seamless channel handoff. The user clicks "Continue on WhatsApp" and lands in a pre-seeded WhatsApp conversation that summarizes what was discussed, what documents were reviewed, and what the next steps are.

## Why this matters in MENA

WhatsApp is the dominant professional and personal communication channel across the MENA region:
- In Lebanon, UAE, KSA, Egypt, and most GCC states, business communication heavily relies on WhatsApp
- Lawyers, clients, and counterparties exchange draft contracts, comments, and signing instructions on WhatsApp
- Many MENA users access Louis on mobile and expect WhatsApp-level friction for follow-ups
- A web-app session that ends without a handoff record creates context loss when the user returns via WhatsApp

The handoff bridges the gap between the AI session and the user's natural working environment.

## When to offer this

Offer the WhatsApp handoff in the following situations:

1. **Session close** — user says "I'll continue later" or shows signs of ending the session
2. **Lawyer handoff** — user needs to share a draft or summary with their attorney for review
3. **Counterparty communication** — user needs to forward a negotiated position summary to the other party
4. **Document receipt** — user wants a reminder link to upload a document they've promised to send
5. **Explicit request** — user says "Send this to WhatsApp" or "Can I get this on WhatsApp?"

**Do not offer** when:
- The conversation contains highly confidential matter details that should not leave the platform
- The user is in a jurisdiction or firm with a WhatsApp communication policy that prohibits business use
- The user has indicated they don't use WhatsApp

## Setup / auth

| Parameter | Description | Required |
|-----------|-------------|----------|
| `waBusinessNumber` | WhatsApp Business API phone number (tenant-configured) | Yes |
| `waApiKey` | WhatsApp Business API key (Meta / third-party provider) | Yes |
| `userPhone` | User's registered WhatsApp phone number | Optional — can be entered at handoff |
| `summaryText` | Pre-generated session summary (max 4096 chars) | Yes |
| `deepLinkOnly` | Generate only the wa.me deep-link (no API call) | Default: false |

If `deepLinkOnly` is true, the tool generates a `wa.me` link with a URL-encoded pre-filled message. No WhatsApp API credentials needed for this mode. The user clicks the link which opens their WhatsApp app with the message pre-typed.

### Deep-link format (no API required)
```
https://wa.me/<phone_number>?text=<url_encoded_summary>
```
Example: `https://wa.me/96171234567?text=Session+summary:+Reviewed+NDA+draft...`

### API-triggered message (requires WhatsApp Business API)
Sends the summary as a template message to the user's WhatsApp number. Requires pre-approved message template with Meta.

## Summary generation

Before generating the handoff, the tool compiles a session summary:

```
Session Summary — [Date] [Time]

What we worked on: [1-2 sentence description]
Document reviewed: [document name if applicable]
Key findings:
- [bullet 1]
- [bullet 2]
Next steps:
- [action 1 for user]
- [action 2 for user]

Continue on Louis: [session link]
```

The summary is trimmed to fit within WhatsApp's message length limits (4096 chars). If the session was very long, the summary prioritizes next steps and key findings over detail.

## Privacy considerations

Before generating the handoff:

1. **Check document sensitivity**: if the session involved documents marked confidential or containing client PII, warn the user that forwarding a summary to WhatsApp may carry the information outside the secure platform.
2. **Strip PII from summary**: by default, remove specific party names, amounts, and identifying details from the WhatsApp summary — replace with `[Party A]`, `[Amount]` — unless the user explicitly approves full detail.
3. **No document attachments**: the handoff sends a text summary only, never the actual documents. Users who want to share documents should use the platform's secure sharing features.
4. **Data retention**: WhatsApp messages are stored by Meta and may not comply with the firm's data retention and confidentiality policies. Note this in the handoff UI.

## Deep-link generation example

```python
import urllib.parse

summary = """
Louis Session Summary — 14 May 2026

Reviewed: NDA draft from Acme Corp
Key findings:
- IP assignment clause missing
- Governing law should be DIFC, not UAE onshore
Next steps:
- Request revised draft from counterparty
- Confirm governing law preference

Continue: https://louis.app/session/abc123
"""

phone = "+96171234567"
link = f"https://wa.me/{phone.replace('+','')}?text={urllib.parse.quote(summary)}"
```

## UI behavior

When this tool is invoked:
1. Generate the session summary
2. Show the user a preview of what will be sent
3. Ask for their WhatsApp number if not already on file (or offer "send to my number" if registered)
4. Display a "Continue on WhatsApp" button
5. On click: open the wa.me deep-link (or trigger API send if configured)
6. Confirm: "Summary sent to WhatsApp"

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| No WhatsApp number on file | Cannot auto-fill deep-link | Prompt user to enter number |
| WhatsApp API error | 400/500 from Meta Business API | Fall back to deep-link; log error |
| Summary too long | Truncated in WhatsApp | Trim to key findings + next steps |
| User phone not WhatsApp | Message not delivered | Note delivery failure; suggest email fallback |
| Confidential content flagged | PII detected in summary | Strip PII before sending; warn user |

## Related skills

- [[tool-web-search-orchestrator]] — if the handoff needs to include a live link to a search result
- [[conversation-empathy-b2c]] — tone calibration for the summary message (warm, not robotic)
- [[onboarding-welcome]] — the onboarding flow that captures the user's WhatsApp number for later handoff
