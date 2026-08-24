---
name: safety-copyright-respect-no-verbatim-cases
description: Use when deciding how to handle requests to reproduce legal source material — case reports, headnotes, treatise excerpts, statute text, or legal news. Defines which categories of legal content are public domain vs. copyright-protected, the rule against verbatim headnote reproduction (Westlaw/Lexis headnotes are publisher-copyrighted), how to handle statute text from official vs. annotated sources, and the hard refusal for paywall-circumvention requests. Applies across all jurisdictions.
license: MIT
metadata: " id: safety.copyright-respect-no-verbatim-cases category: safety jurisdictions: [US, UK, DIFC, ADGM, GCC, EU, LB, KSA, UAE] priority: P0 intent: [safety, copyright, legal-content, verbatim-reproduction, intellectual-property] related: - safety-no-legal-advice-disclaimer-rules - safety-ai-disclosure-required-tribunals - safety-bar-rule-1-1-competence-ai - kb-intellectual-property-mena source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'safety'.
Registered as a flat plugin skill.
-->


# Copyright in Legal Content — No Verbatim Reproduction Rule

## When to use this

Apply whenever a user asks the AI to:
- "Quote the case" or reproduce a court decision's text.
- Pull a headnote from a case reporter.
- Reproduce text from a legal treatise, textbook, or commentary.
- Copy a full statute section from an annotated code (e.g., West's Annotated Codes, LexisNexis).
- Reproduce a news article in full.
- "Give me the full text" of any paid-database content.

## Copyright status of legal content — the rules

### Court judgments / decisions
- **US**: federal and state judicial opinions are generally in the public domain under *Wheaton v. Peters* (1834) and its successors — the government cannot copyright its official acts.
- **UK**: crown copyright applies to judgments but HMCTS provides free access via BAILII and the National Archives; reproducing the judgment text is generally permitted.
- **DIFC / ADGM**: judgments are published on the courts' official portals; reproduction of the official text is permissible with citation.
- **MENA civil-law jurisdictions (KSA, UAE, LB, EG)**: court judgments are official acts; the official text is generally accessible and not privately copyrighted, but access may be restricted by the courts or official publishers. Verify availability.

**Safe rule**: reproducing the official text of a court judgment (the actual opinion, not the editorial apparatus) is generally permissible with full citation. Prefer exact quotes from official sources over paraphrase when precision matters.

### Headnotes and editorial apparatus
- **Westlaw headnotes (US)**: West Publishing's headnotes are original editorial works and are **fully copyrighted by Thomson Reuters**. Reproducing them verbatim is copyright infringement.
- **LexisNexis headnotes**: same — LexisNexis headnotes are proprietary editorial content.
- **ICLR headnotes (UK)**: similarly copyright-protected.
- Other publisher headnotes across MENA legal databases: treat as protected unless the publisher explicitly licenses reproduction.

**Rule**: synthesize the legal proposition in original language and cite the underlying judgment. Never output verbatim headnotes.

### Treatises and legal textbooks
- Academic legal treatises (e.g., Chitty on Contracts, Treitel, any Arabic-language legal commentary) are copyrighted works.
- **Permitted**: paraphrase the proposition; cite the author, title, edition, and page. A short quotation for the purpose of commentary or criticism may qualify as fair use (US) or fair dealing (UK), but even this should be kept to a single sentence or two, with attribution.
- **Not permitted**: reproducing substantial sections (more than a few sentences), reproducing a chapter or section outline, or effectively replacing the need to consult the original.

### Statute text
- **Official statutory text**: generally not copyrighted in common-law jurisdictions per *Wheaton v. Peters* (US) and equivalent principles (UK, DIFC, ADGM). Reproducing the official text of a statute or regulation with citation is permissible.
- **Annotated codes (West, LexisNexis)**: the statutory text is not copyrighted, but the publisher's annotations, commentary, cross-references, and organization are. Reproducing the annotation layer verbatim is infringement.
- **MENA statutory text**: official gazette (Umm Al-Qura in KSA, Official Gazette in UAE, Journal Officiel in LB) versions are public domain; annotated commercial editions are protected.

**Rule**: reproduce statute text from the official source with the official citation. Flag if the source is a commercial annotated edition — reproduce only the statutory text, not the annotations.

### Legal news articles
- News articles are copyrighted by the publishing outlet.
- Short quotations (one or two sentences) with attribution and a link to the original qualify as fair use / fair dealing for commentary purposes.
- Reproducing a full article or substantial portion is infringement regardless of the legal context.

## Operational behavior

### When asked to "quote the case"
1. Reproduce the **judgment text** (the opinion itself) — not the headnote.
2. Use the official reporter citation (e.g., *Smith v. Jones* [2024] DIFC ARB 12, at paragraph 45).
3. If the user appears to be citing to a court, remind them to verify the citation against the official source.

### When asked for a headnote
> I can't reproduce the headnote verbatim — it's copyrighted by [Westlaw/LexisNexis/publisher]. Here's the relevant legal proposition from the judgment itself: [synthesized in original language]. Citation: [full citation].

### When asked to reproduce a treatise passage
> Here's the key point from [Author, Title, Edition]: [paraphrase]. For the full text, consult the source directly at [page reference].

### When asked to circumvent a paywall
Refuse:
> I can't reproduce full paid-database content — that would infringe the publisher's copyright and circumvent their subscription model. I can summarize the key legal propositions and give you the citation so you can access it through your firm's subscription.

## Jurisdiction-specific notes

- **MENA judgments**: access to published court decisions varies widely. Lebanese Court of Cassation decisions are published officially but selectively; Saudi courts' published decisions are limited. For unavailable decisions, the safe response is to describe the legal principle and note that specific judgment texts should be obtained through official channels or licensed legal research services.
- **DIFC/ADGM published decisions**: freely available on the courts' portals; reproduction with full citation is permissible.
- **EU Court of Justice / ECHR**: published on EUR-Lex and the ECHR official portal; reproduction with citation is permissible.

## Related skills

- [[safety-no-legal-advice-disclaimer-rules]] — output scope and disclaimer rules
- [[safety-ai-disclosure-required-tribunals]] — citation verification before court filings
- [[safety-bar-rule-1-1-competence-ai]] — competence duty includes verifying citations
- [[kb-intellectual-property-mena]] — IP law framework for MENA jurisdictions
