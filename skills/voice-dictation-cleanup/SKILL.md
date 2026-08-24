---
name: voice-dictation-cleanup
description: Use when a lawyer or legal professional has dictated text via voice-to-text (STT) and the raw transcript needs to be cleaned into polished, formal written output. This skill governs filler removal, STT error correction, punctuation reconstruction, defined-term formatting, and the strict constraints on what must not be changed — preserving legal substance and numeric precision exactly while removing transcription artifacts.
license: MIT
metadata: " id: voice.dictation-cleanup category: voice priority: P1 intent: [dictation cleanup, speech-to-text, transcription, voice input] related: - voice-short-spoken-output - voice-voice-friendly-short - voice-image-of-contract-page-handler source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Dictation Cleanup

## When to use this

Invoke this skill when:
- The user pastes raw STT (speech-to-text) transcript and asks for it to be cleaned.
- The input text shows clear dictation artifacts: run-on sentences, missing punctuation, filler words, number words that should be digits (or vice versa), homophone errors.
- The user's message is "clean this up" / "fix my dictation" / "format this memo" when the input has dictation-quality characteristics.

The canonical use case: a lawyer dictates a memo on their phone while commuting. Louis cleans it into a draft the lawyer can review and send.

## What to clean

### 1. Remove filler words
Filler words are artifacts of spoken language that should not appear in written legal text:
- Remove: "um", "uh", "like" (used as a filler), "you know", "I mean", "so basically", "right", "okay so"
- Do not remove: "like" when used as a genuine comparison word ("similar to", "such as"); "right" when used as an adjective or as part of a phrase like "right of first refusal."

### 2. Fix STT recognition errors
Common misrecognitions to correct:

| STT output | Likely intended |
|-----------|----------------|
| "their" / "there" / "they're" | Correct per context |
| "its" / "it's" | Correct per context |
| "statute" → "statue" | Correct when legal context is clear |
| "clause" → "claws" | Correct in legal context |
| "indemnify" → "in dim a fy" | Re-merge recognized segments |
| Numbers as words: "twenty twenty four" | Convert: "2024" |
| Partial proper noun: "dee eye ef see" | Reconstruct: "DIFC" |
| Run-together entities: "uae federal" | Restore capitalization: "UAE Federal" |

Be conservative with STT error correction — when the correct word is ambiguous, flag it with `[??]` rather than guessing.

### 3. Reconstruct punctuation
STT outputs are typically unpunctuated run-ons. Apply:
- Sentence-ending periods where the speaker's cadence, topic shift, or completed thought indicates a sentence boundary.
- Commas where the speaker's pause marks a clause boundary.
- Quotation marks around anything that was clearly quoted material.
- Paragraph breaks where the speaker shifts to a new topic.

Do not over-punctuate. If in doubt, use a period and start a new sentence.

### 4. Correct capitalization
- Sentence starts.
- Proper nouns: jurisdiction names (UAE, Lebanon, KSA), party names, defined terms.
- Defined terms: once identified, ensure consistent capitalization throughout (e.g., "the Agreement", "the Buyer").

### 5. Standardize numbers and dates
| Dictated | Written form |
|----------|-------------|
| "twenty-twenty-four" or "twenty twenty four" | 2024 |
| "thirty days" (in a legal obligation) | 30 days |
| "three million dollars" | USD 3,000,000 (in legal docs) or $3 million (in casual memo) |
| "the twelfth of May" | May 12, 2026 (or 12 May 2026 per house style) |
| "ninety percent" | 90% |

Preserve the lawyer's chosen number format if they stated it explicitly ("I want to write it out as thirty days" should remain "thirty days").

### 6. Detect and format defined terms
When the speaker uses a term multiple times and it is clearly a defined contractual term (party name, document title, key concept), capitalize it consistently:
- "the buyer" (first use) → detect pattern → "the Buyer" throughout.
- "the lease" when clearly referring to a specific document → "the Lease."

Flag new defined terms with a comment: `[Note: "the Seller" treated as a defined term — confirm capitalization is correct.]`

## What to preserve

These elements must not be changed:

- **Substantive legal content**: do not add, remove, or restate obligations, conditions, or facts that the speaker expressed. Even if it seems like a logical omission, do not fill it in.
- **Numbers and amounts**: copy exact figures verbatim after standardizing format. Do not round, estimate, or substitute.
- **Specific case citations**: if the speaker cited a case or statute, reproduce it exactly as given. If it appears garbled, flag it with `[??]` — do not reconstruct a plausible citation.
- **Speaker's conclusion**: do not soften, strengthen, or reframe legal opinions the speaker expressed.
- **Structure**: if the speaker clearly said "first... second... third...", preserve that list structure.

## Output options

Provide the cleaned text as the primary output.

Optionally, include a **change-tracked version** that shows what was modified — this is valuable when the lawyer wants to verify every change before signing off. Format as:
```
[REMOVED: "um"] / [CHANGED: "twenty twenty four" → "2024"] / [ADDED PUNCT: "."]
```

Or use markdown strikethrough and inline additions if the rendering surface supports it.

## Limits

- Do not correct substantive legal errors in the dictation (e.g., the lawyer cited the wrong law). Flag them: `[Note: you may want to verify the statute reference here.]`
- Do not translate the text into a different language unless explicitly asked.
- Do not convert the text into a formal document structure (headings, numbered clauses) unless the lawyer asked for that — cleanup and reformatting are different tasks.

## Related skills

- [[voice-short-spoken-output]]
- [[voice-voice-friendly-short]]
- [[voice-image-of-contract-page-handler]]
- [[voice-multimodal-scanned-pdf-handler]]
