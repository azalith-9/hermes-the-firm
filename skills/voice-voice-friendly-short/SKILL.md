---
name: voice-voice-friendly-short
description: "Use when the user is confirmed to be in a hands-free, screen-free context — driving mode, smart speaker, accessibility mode, or phone call — and every response must fit within 80 words (approximately 30 seconds spoken). This skill is the strict variant of voice-short-spoken-output: one main point, plain English, no lists, no citations, no URLs, pause-friendly punctuation, and a bottom-line-first structure with a concrete recommendation."
license: MIT
metadata: " id: voice.voice-friendly-short category: voice priority: P1 intent: [__format__, voice-friendly, spoken-output, hands-free, driving-mode] related: - voice-short-spoken-output - router-platform-aware source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Voice-Friendly Short Output

## When this applies

Invoke this skill (instead of [[voice-short-spoken-output]]) when the user is confirmed to be in a context where they cannot look at a screen:
- Driving mode (confirmed by the platform or by the user stating "I'm driving")
- Smart speaker (Amazon Alexa, Google Home, Apple HomePod)
- Accessibility setting (screen-reader mode, voice-only interface)
- Phone call integration

This is the strictest output format in the platform. When activated, it overrides all other format defaults including [[voice-short-spoken-output]].

## Hard rules

| Rule | Limit |
|------|-------|
| Maximum length | 80 words (≈30 seconds at natural speaking pace) |
| Main points per response | 1 — pick the most important thing |
| Lists | Never — convert to prose |
| Bullets | Never |
| Markdown | Never |
| URLs | Never |
| Citations inline | Never |
| Jargon | Never — plain English only |

If the answer genuinely cannot be given in 80 words, give the bottom line in 80 words and offer to continue: "There's more to say — want me to keep going?"

## Structure

Every voice-friendly response follows this exact pattern:

1. **Bottom line first** — state the conclusion or answer in the first sentence.
2. **One reasoning step** — one sentence explaining why.
3. **Concrete recommendation** — what the listener should do.
4. **Optional: prompt for follow-up** — a question to keep the dialogue alive.

## Examples

### The wrong way (text-optimized, ≈80 words)

> "Under UAE Federal Decree-Law 33/2021 Article 10, your non-compete is enforceable only if it's limited in scope, geography, time, and necessary for a legitimate interest. Cabinet Decision 1/2022 narrowed this further. Your two-year MENA-wide restriction is likely too broad. A court would probably narrow it to twelve months and to specific emirates."

This is a good written answer. Spoken aloud, the citation and statute numbers are useless to a driver. The structure buries the conclusion.

### The right way (voice-optimized, ≈60 words)

> "Your non-compete probably won't hold up as written. UAE law requires it to be narrow — limited time, limited area, and only what's strictly necessary. Two years across all of MENA is too much. A court would likely cut it to twelve months and to specific emirates. Worth re-drafting with tighter scope. Want me to draft a revised version?"

### Legal Q&A example (voice-optimized)

User: "Does the counterparty have to give me notice before terminating?"

> "Yes, under a standard UAE contract. They typically need to give you thirty days' written notice before they can terminate. Check your specific contract for the exact number. If they terminate without notice, you may have a claim. Want me to pull up the exact clause?"

## Converting longer answers to voice format

When the full answer requires more than 80 words:

1. Identify the single most actionable conclusion.
2. State it in one sentence.
3. Give the minimum context needed to understand it.
4. Offer to elaborate: "I can give you more detail — say 'keep going' or check the full answer when you're at a screen."

Do not attempt to compress a complex legal analysis into 80 words by leaving out essential qualifications. If the qualifications matter, say "This is a simplified answer — please check the full version before acting on it."

## Language
Plain English (8th grade equivalent). No Latin phrases (habeas corpus, res judicata) unless they are the only way to identify the concept. No acronyms without expansion on first use. Numbers as words: "thirty days", not "30 days".

## Relationship to voice-short-spoken-output

[[voice-short-spoken-output]] allows 150 words and is appropriate when the user has a screen available but is using voice input. This skill (80 words) applies when there is no screen. Use the stricter limit whenever in doubt about which applies.

## Related skills

- [[voice-short-spoken-output]]
- [[router-platform-aware]]
- [[voice-dictation-cleanup]]
