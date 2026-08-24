---
name: router-language-detector
description: Use to detect the input language(s) of a user message and determine the correct output language for the response. Supports English, Arabic (MSA, Levantine, Gulf), French, and code-switched mixes. Handles MENA legal practice where Arabic-English and Arabic-French code-switching is common. Determines the legally controlling language for bilingual document drafting contexts. Outputs a JSON object consumed by the output formatter and persona selector.
license: MIT
metadata: " id: router.language-detector category: router priority: P0 intent: [__router__] related: [router-intent-detection, router-jurisdiction-detector, router-persona-selector, router-platform-aware] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'router'.
Registered as a flat plugin skill.
-->


# Language Detector & Output Matcher

## Purpose

Language detection in a legal AI for MENA is more nuanced than simple ISO language code detection. Lawyers in the region routinely write in code-switched Arabic-English or Arabic-French — using Arabic sentence structure with English legal terms, or English sentences with Arabic clauses inserted. The response must match the input language without breaking the user's register or making the output feel foreign.

Additionally, for document drafting, the question is not just "what language did the user write in" but "what language should the document be drafted in, and which version is legally controlling?" — these are different questions.

## Supported Language Modes

| Mode | Description |
|---|---|
| `en` | English (monolingual) |
| `ar-msa` | Arabic, Modern Standard Arabic (الفصحى) — formal legal and documentary Arabic |
| `ar-levantine` | Arabic, Levantine dialect (Lebanese/Syrian) — used in informal conversation; not for formal legal documents |
| `ar-gulf` | Arabic, Gulf dialect (KSA/UAE/Kuwait/Qatar/Bahrain) — used in informal conversation |
| `fr` | French (used in Lebanon, Morocco, Tunisia, Algeria) |
| `ar-en` | Code-switched Arabic-English (most common in MENA legal practice) |
| `ar-fr` | Code-switched Arabic-French (Lebanon, Morocco) |
| `en-fr` | Code-switched English-French (less common; occasional in LB legal practice) |

## Detection Rules

### Rule 1 — Match the User's Language

The primary rule: respond in the language the user wrote in.

- If the user wrote in English → respond in English
- If the user wrote in Arabic (any dialect) → respond in Arabic
- If the user wrote in French → respond in French
- **Never switch languages without instruction**

### Rule 2 — Mixed Input

If the input is code-switched:

- **Dominant language rule**: if one language is clearly dominant (>70% of the message), respond in the dominant language. Use the minority-language terms naturally where they are more precise.
- **Roughly equal split (~50/50)**: prefer English as the response language; use key terms in both languages where helpful. Rationale: English is the more commonly understood written language in MENA legal professional practice; Arabic-speaker users writing 50% English are typically comfortable receiving English output.
- **Legal terms inserted in English within an Arabic message**: keep those terms in English in the response (e.g., "indemnification", "force majeure", "EBITDA" need not be translated when the user already used the English form)

### Rule 3 — Document Drafting Language

For document drafting requests, language matching is not sufficient — the practitioner needs to know which language to draft in and which version will be legally controlling.

Ask explicitly when the jurisdiction is bilingual and legal control matters:

- **Lebanon**: "Should the document be in Arabic, French, or bilingual (Arabic/French)? In Lebanon, both are official languages. For commercial contracts, which language should be the controlling version?"
- **UAE**: "Should the contract be in Arabic (which is the official language recognized by UAE courts), English (common in international commercial practice), or bilingual Arabic-English? For UAE court proceedings, the Arabic version is typically required."
- **KSA**: "Should the document be in Arabic? Saudi law requires Arabic for most official documents; an English translation may be provided for the counterparty's convenience but the Arabic version will govern."
- **DIFC / ADGM**: "Should the document be in English? DIFC and ADGM operate in English; Arabic is optional."

If the user has already specified a language for the document, use that language without re-asking.

### Rule 4 — Voice Surface

On voice input (speech-to-text):
- Do not rely solely on the STT-transcribed text language for detection — code-switching in speech often produces mixed-language transcripts
- Use the STT confidence score by language alongside the text analysis
- For voice responses: always respond in prose (no markdown, no bullets, no tables — see [[router-platform-aware]])

### Rule 5 — Formal vs Informal Register

Within Arabic, the formality level matters:
- **Formal legal Arabic (فصحى قانونية)**: for documents, legal memos, formal correspondence
- **Modern Standard Arabic**: for clear explanations, consumer-facing responses
- **Dialect**: only in informal chat contexts; never in legal documents or formal advice

Match the user's register as closely as possible. If the user wrote in a dialect but needs a formal document, produce the document in formal Arabic and acknowledge the switch ("I'll draft the contract in formal legal Arabic (الفصحى القانونية)").

## Document Controlling Language — MENA Context

| Jurisdiction | Official language | Controlling language for contracts | Common practice |
|---|---|---|---|
| KSA | Arabic | Arabic governs; English for convenience | Arabic drafts; English translation attached |
| UAE (onshore) | Arabic | Arabic governs in UAE courts | Bilingual; Arabic version stated to govern |
| UAE DIFC | English | English governs | English primary; Arabic optional |
| UAE ADGM | English | English governs | English primary; Arabic optional |
| Lebanon | Arabic + French | Parties choose; state in contract | Bilingual; often French-English in commercial |
| Egypt | Arabic | Arabic governs | Arabic primary; English translation common |
| Qatar (QFC) | English | English for QFC contracts | English primary |
| Jordan | Arabic | Arabic | Arabic primary |
| Morocco | Arabic + French | Arabic governs officially; French widely used | Often French in commercial practice |

## Output

```json
{
  "input_lang": "<language mode from supported set>",
  "output_lang": "<language mode>",
  "mixed": true/false,
  "dominant_language": "<en|ar|fr|null>",
  "register": "formal|standard|informal|dialect",
  "controlling_lang_for_doc": "<en|ar|fr|null — only relevant for drafting requests>",
  "ask_about_controlling_language": true/false,
  "asking_question": "<if ask_about_controlling_language, the question to ask>"
}
```

## Related Skills

- [[router-intent-detection]]
- [[router-jurisdiction-detector]]
- [[router-persona-selector]]
- [[router-platform-aware]]
- [[review-translation-quality-ar-en]]
