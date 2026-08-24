---
name: output-voice-friendly-short
description: Use when the agent must produce output optimised for voice delivery or screen-reader consumption — short sentences, no nested clauses, no footnotes, no tables, no inline citations. Applies across all jurisdictions. Triggers when a voice interface, voice assistant integration, or accessibility context is active, or when the user explicitly requests a spoken-format answer.
license: MIT
metadata: " id: output.voice-friendly-short category: output jurisdictions: ['__multi__'] intent: ['__output__', 'voice', 'accessibility', 'short-form', 'spoken'] related: - output-mobile-friendly-short - output-partner-memo-style - output-irac-structure priority: P2 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'output'.
Registered as a flat plugin skill.
-->


# Voice-Friendly Short Output

Voice output has strict constraints that written legal output does not: the listener cannot re-read a sentence, cannot scan a table, and loses the thread if a clause nests more than two levels deep. Legal AI on voice interfaces — whether read aloud by a screen reader or delivered through a voice assistant — must adapt to those constraints without sacrificing accuracy.

## When this applies

Activate when:
- The output will be read aloud by a text-to-speech system
- A screen reader is the primary access mode
- The user requests a "spoken" or "voice" format answer
- The interface signals a voice or accessibility context
- A quick verbal briefing is requested ("give me a 30-second summary")

Do **not** activate for:
- Formal written deliverables (memos, opinions, contracts)
- Outputs that will be printed or reviewed on screen
- Complex multi-issue analysis requiring parallel structure

## Behaviour — the four rules

### 1. Short sentences

Maximum 15 words per sentence. If a legal rule requires a longer sentence, break it at the conjunction:

**Before:** "Under UAE Federal Decree-Law 33/2021, a non-compete clause must be proportionate in scope, limited in geography, limited in duration, and necessary to protect a legitimate employer interest."

**After:** "A non-compete in the UAE must meet four tests. It must be proportionate in scope. It must be limited to a specific geography. It must not exceed two years. And it must protect a real business interest. That's UAE law, Decree-Law 33 of 2021."

### 2. No nested clauses

Flatten any clause that qualifies a qualification:

**Before:** "The obligation, which arises unless the employee (who was not a signatory to the original NDA, having joined after its execution) can demonstrate..."

**After:** "The obligation arises by default. One exception: if the employee joined the company after the NDA was signed, they may argue they were never bound by it."

### 3. No footnotes, tables, or inline citations

Citations are spoken as plain text at the end, in a short "sources" statement:

**Inline format (written):** "…(UAE FDL 33/2021 art 10)…"
**Voice format:** "…under Article 10 of the UAE employment law…" [citations delivered at the end: "Source: UAE Federal Decree-Law 33 of 2021, Article 10."]

Tables become a brief comparative statement: "In the UAE, notice is 30 days. In KSA, it is also 30 days. In Lebanon, it depends on the contract."

### 4. Confidence signal by phrase, not icon

Mobile output uses emoji confidence signals (✅/⚠️/🚫). Voice output uses spoken equivalents:
- "This is well-established law." (high confidence)
- "This is generally the rule, but it depends on the specific facts." (moderate)
- "This area is uncertain — you should check with a lawyer before acting." (low)

## Structure for voice delivery

```
[One-sentence answer]
[Brief explanation — 2–4 sentences maximum]
[One key caveat if needed]
[Source reference — plain language]
[Offer to expand]
```

Example:

> "Under UAE law, a maximum notice period of 30 days applies for employees with under five years of service. The rule is in the 2021 employment law. If the contract says more, the contract governs. Source: UAE Federal Decree-Law 33 of 2021, Article 43. Want the full breakdown?"

## Length limits

| Content type | Voice limit |
|---|---|
| Direct answer to a legal question | 60–90 seconds of speech (~150–225 words) |
| Summary of a document | 90–120 seconds (~225–300 words) |
| Full advice (voice briefing) | 3 minutes maximum (~450 words); offer a written follow-up |

Beyond these limits, pause and ask: "Want me to continue, or would a written version be more useful?"

## Arabic / multilingual voice output

For Arabic-language voice delivery:
- Use formal Modern Standard Arabic (MSA), not colloquial
- Avoid transliterated legal terms where Arabic equivalents exist
- Number articles in spoken form: "Article Ten" not "Art. 10"
- Dates: read in Gregorian format unless the audience specifically expects Hijri

## Do not

- Do not read out Markdown formatting ("double asterisk bold double asterisk")
- Do not list multiple citations inline — consolidate at the end
- Do not use acronyms without first spelling them out: "the DIFC — that's the Dubai International Financial Centre"
- Do not deliver tables as tables — convert to spoken comparisons

## Related skills

- [[output-mobile-friendly-short]]
- [[output-partner-memo-style]]
- [[output-irac-structure]]
- [[output-inline-citations-with-pinpoints]]
