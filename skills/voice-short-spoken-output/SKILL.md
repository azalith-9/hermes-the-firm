---
name: voice-short-spoken-output
description: Use when the platform surface is voice (smart speaker, phone call, driving mode, accessibility TTS) and the response must be optimized for spoken delivery rather than reading. This P0 format skill enforces prose-only output, a 150-word ceiling, short sentences, spelled-out numbers, expanded acronyms, and pause-friendly punctuation — overriding all default markdown and list-based output conventions.
license: MIT
metadata: " id: voice.short-spoken-output category: voice priority: P0 intent: [__format__, voice-output, spoken, TTS, accessibility] related: - voice-voice-friendly-short - router-platform-aware - output-mobile-friendly-short source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Voice — Short Spoken Output

## When this applies

Apply this skill when the output surface is a voice interface: smart speaker (Amazon Alexa, Google Home), text-to-speech on mobile, in-car mode, phone call integration, or any accessibility setting that reads responses aloud.

The router signals this context via a platform flag. When present, this skill takes P0 precedence and overrides all default formatting — no exceptions.

## Hard format rules

These rules are non-negotiable when the surface is voice:

| Rule | Reason |
|------|--------|
| **Prose only** — no bullets, no markdown, no headings | Screen-reader and TTS engines read markdown syntax as literal characters ("asterisk asterisk important asterisk asterisk") |
| **Maximum ~150 words** (≈60 seconds spoken at natural pace) | Beyond 60 seconds, voice listeners lose the thread |
| **Sentences of ≤15 words** preferred | Long sentences are hard to follow aurally; listeners cannot re-read |
| **No inline citations** | Read aloud, citations break the flow; collect at the end if needed |
| **No tables, no code blocks** | Cannot be rendered meaningfully in voice |
| **No URLs** | URLs read aloud ("h t t p s colon slash slash...") are unusable |
| **Numbers spelled out** | "thirty days" not "30 days"; "fifteen percent" not "15%"; exception: years ("2026" is fine) |
| **Acronyms expanded on first use** | "anti-money laundering, or AML" — the full form first, then the abbreviation |

## Punctuation for speech

Voice output must be punctuated not for grammar alone, but for the speaker's breathing and pacing:
- Commas where a natural pause should occur.
- Periods at every sentence end — no run-ons, even if they are grammatically joined clauses.
- Em dashes or dashes for asides: "The payment — which was due last week — has not arrived."
- Avoid colons and semicolons: they are visually meaningful but spoken awkwardly.

## Citation handling

If the response requires citing legal authority:
- Do not embed the citation inline ("...under UAE Federal Decree-Law 33/2021 Article 10...").
- Instead, integrate the substance and attribute it simply: "Under UAE employment law, the rule is..."
- If the user needs the precise citation, add after the spoken response: "Sources: UAE Federal Decree-Law 33 of 2021. Do you want me to send those to you?"

## Avoiding lists

If the content is naturally list-shaped, convert to prose with explicit sequence markers:
- "There are three main points. First, the payment is overdue. Second, the contract gives you fourteen days to cure. Third, after that window, the counterparty may terminate."

Keep the list short (three to five items maximum in voice). More than five items requires either a follow-up screen interaction or a summary: "There are seven conditions — would you like to hear the most important three now and the rest later?"

## Closing convention

End each voice response with a question or a natural invitation to continue:
- "Does that answer your question, or would you like more detail on the payment clause?"
- "Let me know if you want me to check anything else."

This keeps the voice dialogue active and signals to the user that the response is complete.

## What to skip

When the full answer would require:
- A multi-jurisdiction comparison table
- A long clause-by-clause analysis
- Multiple document extracts

Defer to a follow-up: "That's a detailed question — I can send you a full written answer. For now, the short version is..."

Then give the short version.

## Relationship to voice-voice-friendly-short

[[voice-voice-friendly-short]] is the stricter variant: 80 words maximum, one main point, no exceptions. That skill applies when the user is confirmed to be in a hands-free, screen-free context (driving, smart speaker). This skill (150 words) applies when the surface is voice but the user may have occasional glances at a screen.

When in doubt, use the stricter 80-word limit.

## Related skills

- [[voice-voice-friendly-short]]
- [[router-platform-aware]]
- [[output-mobile-friendly-short]]
- [[voice-dictation-cleanup]]
