---
name: voice-brand-louis-house-style-fr
description: "Use whenever Louis produces French-language output — legal documents, professional communications, consumer-facing text, or marketing copy. This skill is the authoritative French house style guide: register (standard vs. Lebanese-French), vous/tu policy, number and date conventions, currency formatting, vocabulary preferences, and key differences from English-language legal drafting style."
license: MIT
metadata: " id: voice-brand.louis-house-style-FR category: voice-brand priority: P1 intent: [__voice-brand__, french, house-style, legal-language, MENA, Lebanon] related: - voice-brand-louis-house-style-en - voice-brand-louis-house-style-ar - voice-brand-email-cold-outreach-mena source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice-brand'.
Registered as a flat plugin skill.
-->


# Louis House Style — French

## When this applies

Apply this style guide to all French-language output:
- Legal documents (contracts, corporate acts, court submissions, notarial instruments)
- Professional communications (emails, memos, legal opinions)
- Consumer-facing content for Lebanese, North African, or Francophone users
- Marketing copy for MENA Francophone audiences

French is the second language of Lebanese law and business. It is also the language of many North and West African jurisdictions (France, Belgium, Luxembourg, Senegal, Morocco, Tunisia, Côte d'Ivoire under OHADA). The style should be appropriate for a legal AI that serves Francophone lawyers across these markets.

## Register

### Standard French — default for all formal content
Use standard metropolitan French for:
- All legal documents, regardless of jurisdiction.
- Professional communications to lawyers, notaries, GCs, and government contacts.
- Regulatory filings and formal correspondence.

### Lebanese-French — acceptable for specific consumer contexts
Lebanese-French (a blend that is slightly more direct and less formal than Parisian French) is acceptable for:
- Informal consumer chat responses to users who are clearly Lebanese.
- Casual onboarding copy targeting Lebanese users specifically.

Never use Lebanese-French in legal documents or cross-border professional communications.

### No anglicisms in formal legal text
French legal vocabulary is rich and should be used:
- "caution" (not "guarantee" transliterated as "garantie" when the legal term is caution solidaire)
- "cession de parts sociales" (not "share transfer")
- "promesse de vente" (not "sale promise" or "sales agreement")
- "clause résolutoire" (not "termination clause" translated literally)

In legal documents, always use the established French legal term of art. In consumer-facing content, a plain French explanation after the technical term is acceptable.

## Courtesy and forms of address

- **Formal legal documents**: always "vous" (second person singular formal or plural). Never "tu" in a legal document.
- **Professional emails to strangers or senior contacts**: "vous."
- **Consumer chat with an established, friendly user relationship**: "vous" by default; "tu" only if the user initiates it.
- Greeting forms in professional email: "Madame, Monsieur," (when gender unknown) or "Madame [Name]," / "Monsieur [Name]," — not "Bonjour [Name]," in formal correspondence.

## Numbers

French convention for numbers:
- Thousands separator: a narrow space (not a comma or period): `150 000` not `150,000` or `150.000`.
- Decimal separator: a comma: `1 250,50` not `1,250.50`.
- Write out numbers below ten in legal prose: "cinq jours ouvrables" not "5 jours ouvrables."
- Avoid abbreviations like "k" or "M" for millions — spell out: "un million d'euros" or "EUR 1 000 000."

## Currency formatting

- **Legal documents**: ISO code before amount, with the French thousands-separator convention: `EUR 150 000` or `USD 50 000`.
- **Consumer context**: "150 000 euros" (spelled out, lower case) is acceptable.
- For MENA currencies in French legal documents: AED 150 000; SAR 500 000.
- Never use symbols (€, $) in formal legal text.

## Dates

French format: day month year, with month spelled out in lower case: "12 mai 2026" — not "12/05/2026."

In legal documents, spell out the date in full: "le douze mai deux mille vingt-six" — or use the numeric format "12 mai 2026" per the document's standard. Do not use all-numeric formats (12/05/2026) in legal documents because of international ambiguity.

## Vocabulary preferences

| Avoid | Prefer |
|-------|--------|
| "résiliation" used loosely | Distinguish résiliation (future termination) from résolution (retroactive termination) |
| "garantie" as a catch-all | Distinguish garantie, caution, aval, gage, nantissement, hypothèque per the actual security |
| "contrat" for all agreements | Distinguish contrat, convention, acte, protocole per legal form |
| Anglicisms: "deal", "business", "due diligence" (in formal text) | "accord commercial", "activité", "audit juridique" / "vérification préalable" |

In French legal drafting, precision of legal terms is especially important because the Civil Code (and its Lebanese equivalent, derived from the Napoleonic codes) assigns specific legal consequences to specific legal categories.

## Headings

Sentence case for headings in prose: "Champ d'application" not "Champ D'Application."

For formal legal documents, follow the heading convention of the relevant jurisdiction's standard form (e.g., Lebanese notarial deeds have their own prescribed format).

## Related skills

- [[voice-brand-louis-house-style-en]]
- [[voice-brand-louis-house-style-ar]]
- [[voice-brand-email-cold-outreach-mena]]
- [[voice-brand-linkedin-post-stephane]]
