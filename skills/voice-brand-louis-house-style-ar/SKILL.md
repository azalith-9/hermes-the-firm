---
name: voice-brand-louis-house-style-ar
description: "Use whenever Louis produces Arabic-language output — legal documents, client-facing text, UI strings, or in-product communications. This skill defines the authoritative Arabic house style: register selection (MSA vs. dialect), numeral conventions, currency formatting, punctuation marks, diacritics policy, bilingual cross-referencing, and the translation standard required for legal documents."
license: MIT
metadata: " id: voice-brand.louis-house-style-AR category: voice-brand priority: P1 intent: [__voice-brand__, arabic, house-style, legal-language, MENA] related: - voice-brand-louis-house-style-en - voice-brand-louis-house-style-fr - voice-brand-email-cold-outreach-mena source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice-brand'.
Registered as a flat plugin skill.
-->


# Louis House Style — Arabic

## When this applies

Apply this style guide to any Arabic-language output produced by Louis:
- Legal documents (contracts, opinions, court submissions, notarial deeds)
- In-product UI text (button labels, tooltips, onboarding copy)
- Client-facing communications (emails, reports, summaries)
- Marketing copy (MENA-facing landing pages, social posts)

This guide governs the **form** of Arabic output; the legal substance is governed by the relevant practice-area or drafting skills.

## Register

### Modern Standard Arabic (MSA) — default for all formal content
Use MSA (الفصحى) for:
- All legal documents and court-ready text.
- Professional communications to lawyers, GCs, government contacts.
- Regulatory filings and correspondence.
- Published reports and whitepapers.

MSA is the only appropriate register for legal documents. Dialect in a contract creates ambiguity about terminology, looks unprofessional, and may be rejected by courts or notaries.

### Dialect — permitted for consumer-friendly casual contexts
Levantine Arabic (Lebanese/Syrian) is acceptable for:
- Consumer-facing conversational responses to users who are clearly Lebanese or Levantine.
- Informal tooltips or in-product copy specifically adapted for a Lebanese consumer audience.

Gulf Arabic (Emirati/Saudi/Kuwaiti) is acceptable for:
- Informal consumer-facing copy for a Gulf audience only.
- Never use for legal or formal documents even in UAE/KSA contexts — MSA is required.

When in doubt, use MSA. Defaulting to the formal register is never wrong; defaulting to dialect in a formal context is.

## Numeral convention

Use **Western Arabic numerals** (0, 1, 2, 3…) throughout, not Eastern Arabic (٠, ١, ٢, ٣…).

Rationale: Western numerals are the norm in printed legal documents across UAE, KSA, Lebanon, and Egypt for contracts and commercial documents. Eastern numerals appear in Quranic text and some government-internal documents but are not standard in commercial legal practice.

## Currency formatting

Use **ISO 4217 currency codes**, not symbols:
- AED (not د.إ)
- SAR (not ﷼)
- LBP (not ل.ل)
- EUR (not €, in Arabic context)
- USD (not $, in Arabic context)

Format: `AED 150,000` (code before amount, space separator).

Exception: in bilingual documents where the English section uses symbols, the Arabic section should still use codes for consistency and to avoid encoding issues.

## Punctuation

Use Arabic-specific punctuation characters:
- Arabic comma: ، (not ,)
- Arabic semicolon: ؛ (not ;)
- Arabic question mark: ؟ (not ?)
- Period: . (period is the same in both scripts)
- Parentheses: () (standard Unicode parentheses are correct)

Do not substitute Latin punctuation in Arabic text. Unicode rendering in most legal document formats handles Arabic punctuation correctly.

## Diacritics (تشكيل)

| Context | Diacritics policy |
|---------|------------------|
| Formal legal documents (contracts, judgments) | Full diacritics where ambiguity exists in defined terms and obligations |
| Professional communications (emails, reports) | No diacritics required unless clarifying a specific term |
| Consumer-facing text | No diacritics (adds visual clutter for native readers) |
| Quoted statutory text | Reproduce exactly as in the official Arabic legal source |

Legal terms of art may require diacritics to prevent misreading (e.g., distinguishing مَلك from مُلك). When drafting legal documents, apply diacritics to all defined terms on first use.

## Bilingual cross-referencing

In bilingual documents (Arabic-English contract or report):
- Include both Arabic and English versions of defined terms on first use: e.g., "المتعاقد (the Contractor)".
- Use consistent English equivalents throughout — do not switch between "Contractor" and "Vendor" in the English column for the same Arabic term.
- Where a legal concept has no clean Arabic equivalent (e.g., "escrow", "step-in rights"), transliterate and explain in parentheses, then use the transliteration consistently.

## Sworn translation standard

For documents that will be used in court, notarized, or submitted to government authorities:
- Output must meet the standard required for certified translation in the relevant jurisdiction.
- In UAE: must be suitable for a licensed legal translator's certification — no colloquialisms, no ambiguous phrasing, precise legal terminology.
- In Lebanon: text should conform to the standard expected by the Beirut Bar Association's translation norms.
- Flag to the user if the output was generated for review purposes and has not been reviewed by a certified sworn translator.

## Related skills

- [[voice-brand-louis-house-style-en]]
- [[voice-brand-louis-house-style-fr]]
- [[voice-brand-email-cold-outreach-mena]]
- [[voice-multimodal-scanned-pdf-handler]]
