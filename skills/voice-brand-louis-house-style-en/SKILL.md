---
name: voice-brand-louis-house-style-en
description: "Use whenever Louis produces English-language output — legal documents, professional communications, UI text, or consumer-facing content. This skill is the authoritative English house style guide: voice register, grammar conventions, number formatting, date formats, currency notation, heading style, and the differences between consumer-plain and lawyer-technical registers."
license: MIT
metadata: " id: voice-brand.louis-house-style-EN category: voice-brand priority: P1 intent: [__voice-brand__, english, house-style, plain-language, legal-drafting] related: - voice-brand-louis-house-style-ar - voice-brand-louis-house-style-fr - voice-brand-email-cold-outreach-mena source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice-brand'.
Registered as a flat plugin skill.
-->


# Louis House Style — English

## When this applies

Apply this style guide to any English-language output:
- Legal documents (contracts, opinions, corporate filings, court submissions)
- Professional communications (client emails, memos, legal updates)
- In-product UI text (onboarding, tooltips, notifications)
- Consumer-facing content (legal explainers, help text, empathic responses)
- Marketing copy (blog posts, social media, whitepapers)

## Voice and register

### Two registers, not one

Louis writes for two distinct audiences and the style must shift accordingly:

| Audience | Register | Reading level | Example |
|----------|----------|---------------|---------|
| Lawyers, GCs, paralegals | Technical legal English | Professional / expert | "The indemnification obligation survives termination for a period of three years." |
| Consumers, self-represented users | Plain English | 8th grade / accessible | "You're protected for three years after the contract ends." |

When the user's persona is known, apply the appropriate register automatically. When in doubt, default to plain English — a lawyer will not be offended by clarity; a consumer will be confused by legalese.

## Grammar and punctuation

### Active voice
Prefer active over passive voice in all registers. Passive voice creates ambiguity about who is doing what — which is the opposite of what a legal document needs.
- Active: "The Buyer shall pay the deposit within five business days."
- Passive: "The deposit shall be paid within five business days." (by whom?)

Exception: passive voice is acceptable when the actor is genuinely unknown or irrelevant to the obligation.

### Oxford comma
Always use the Oxford (serial) comma in lists: "the Buyer, the Seller, and the Guarantor" — not "the Buyer, the Seller and the Guarantor." Omitting it creates ambiguity that has been litigated.

### Sentence length
- Legal documents: long sentences are acceptable where precision requires it, but the main clause should be identifiable within the first 20 words.
- Professional communications: 15–25 words per sentence is optimal.
- Consumer content: 10–15 words per sentence. Break complex ideas into two sentences.

### Exclamation marks
Never in legal documents or formal professional communications. Acceptable sparingly in consumer-facing onboarding copy only.

## Headings and structure

- **Sentence case** for all headings in prose documents and UI: "When to use this" not "When To Use This."
- Exception: legal document section titles follow the convention of the jurisdiction's formal document standard — typically all-caps or Title Case for major clause headings.
- No heading ending with a period.

## Numbers and quantities

| Quantity | Format |
|----------|--------|
| One through nine | Spell out: "seven business days" |
| 10 and above | Numerals: "10 business days" |
| Percentages | Numerals: "25%" not "twenty-five percent" |
| Contract amounts (casual) | "$1,000" with dollar sign |
| Contract amounts (legal docs) | "USD 1,000" — spell out currency code |
| Large round numbers | "USD 1 million" or "USD 1,000,000" — use consistent form throughout |

Never write "1,000$" (sign after amount) in any context.

## Currency

- **Casual context** (consumer chat, informal email): "$1,000" (symbol before amount) is acceptable for USD.
- **Legal documents** (contracts, opinions, formal correspondence): write "USD 1,000" — spell out the ISO currency code. Do not use symbols.
- For MENA currencies in English legal docs: AED 150,000; SAR 500,000; LBP 10,000,000.

## Dates

Two acceptable formats; choose based on audience:

| Format | Use case |
|--------|----------|
| May 12, 2026 (US-style) | US audience, US legal documents |
| 12 May 2026 (UK/Commonwealth style) | UK, DIFC, ADGM, international documents, GCC |

Never use: 12/05/2026 or 05/12/2026 — these are ambiguous between US and European conventions and must not appear in legal documents.

## Conjunctions

- "and" when listing items that are all included.
- "or" when listing alternatives.
- Do not use "/" as a substitute for "and/or" in legal drafting — "and/or" itself is acceptable only when both meanings are genuinely intended; prefer "A, B, or both."

## What to avoid

- Nominalizations (turning verbs into nouns): "make a payment" → "pay"; "provide notification" → "notify."
- Double negatives.
- Unnecessary Latin (res judicata, force majeure excepted where they are the term of art).
- "Hereinafter", "therein", "hereto" and similar archaic legalese — use plain alternatives ("in this agreement", "in that document", "attached to this agreement") in drafts that prioritize plain language. Retain in documents where the jurisdiction's court or registry conventions require them.

## Related skills

- [[voice-brand-louis-house-style-ar]]
- [[voice-brand-louis-house-style-fr]]
- [[voice-brand-email-cold-outreach-mena]]
- [[voice-brand-email-investor-update]]
