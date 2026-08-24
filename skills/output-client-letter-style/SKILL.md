---
name: output-client-letter-style
description: Use when formatting a legal AI output as a formal client letter — covering the structure (letterhead, greeting, analysis, recommendation, sign-off), the voice rules (professional peers, calibrated confidence, plain English), and the mandatory cautions (privilege markings, reservation of rights, scope references, avoiding outcome promises). Applies to law firm client communications in all jurisdictions covered by the platform.
license: MIT
metadata: " id: output.client-letter-style category: output priority: P0 intent: [client-letter, formatting, professional-communication, privilege] related: [output-executive-summary-first, output-creac-structure, output-bilingual-formatting, conversation-disclaimer] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'output'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Client Letter Style

## When to use this

Apply this style whenever the output is a formal letter from a lawyer (or law firm) to a client. This covers:
- Opinion letters (legal opinions, tax opinions)
- Advice letters (advice on a specific legal question)
- Update letters (status of a matter)
- Demand letters (claims, default notices)
- Transmittal letters (covering document transmittal)
- Engagement letters (scope of retainer)

Do **not** apply this style for:
- Internal memos (use CREAC or BLUF structure)
- Court filings or pleadings (use court-specific formatting)
- Informal email updates (those have a lighter structure)

## Document structure

### 1. Letterhead block

```
[Firm Name]
[Address Line 1]
[City, Country]
[Date — written out: 14 May 2026]
[Reference / Matter number]

RE: [Subject line — concise, 1 line]
```

In MENA formal practice, the date is often written in full (`14 May 2026` not `14/05/2026`) to avoid ambiguity between day-first and month-first conventions.

For bilingual letters (Arabic + English), mirror the letterhead block in both languages.

### 2. Salutation

```
Dear [Name],
```

In formal firm practice:
- Use the client's full name on first reference (`Dear Ms Al-Rashid,`).
- For a firm or company, use the company name (`Dear Team at [Company Name],` or more formally `Dear Sir/Madam,`).
- In MENA contexts: for Arabic-speaking clients, `Dear Mr/Ms [First name]` is appropriate in English letters; in Arabic letters, use the appropriate honorific (`عزيزي/عزيزتي [اللقب + الاسم]`).

### 3. Opening paragraph

State in one paragraph:
- What matter or question this letter addresses
- The instruction or request received (briefly)
- The purpose of the letter

> We write further to your instruction of [date] requesting our advice on the enforceability of the non-competition clause in the Employment Agreement between [Employee] and [Company] (the "Agreement").

### 4. Analysis / advice body

This is the substance of the letter. Structure it with clear headings if it covers multiple legal issues. Rules:
- Translate technical legal terms into plain English on first use: `"penalty clause (a clause that imposes a pre-agreed sum payable on breach)"`.
- Cite authority in footnotes or parenthetical references — do not clutter the prose with long citations.
- Use numbered points or short headings for multiple issues.
- Present the analysis before the conclusion within each section — lead with context, then the legal rule, then the application to the client's facts.

Exception: if the letter opens with a BLUF summary per [[output-executive-summary-first]], the conclusion appears first at the top.

### 5. Recommendation and next steps

Close the analysis with clear action items:
```
**Recommendations**
1. Revise the non-compete clause to reduce the geographic scope to the UAE (from "MENA-wide").
2. Reduce the duration from 24 to 12 months to align with recent MOHRE guidance.
3. Confirm the legitimate interest the non-compete is designed to protect, which must be documented to withstand challenge.

**Next steps**: we recommend scheduling a call to discuss the revised clause before the employment contract is signed. We can prepare a redlined version of the clause for your review.
```

### 6. Closing and signature block

```
We remain at your disposal for any further questions.

Yours sincerely / Yours faithfully,

[Signatory Name]
[Title]
[Firm Name]
[Direct telephone]
[Email]
```

Use "Yours sincerely" when the letter begins with the client's name (`Dear Ms Al-Rashid`); use "Yours faithfully" when it begins `Dear Sir/Madam`.

## Voice

| Do | Do not |
|----|--------|
| Address the client as a professional peer | Use customer-service softening ("I hope you're doing well") |
| Use plain English with technical terms explained | Use unexplained Latin maxims or unexplained acronyms |
| Be confident but calibrated ("the clause is likely unenforceable") | Overpromise ("we will win") |
| State the limits of your advice clearly | Imply comprehensive coverage when you only addressed a specific question |
| Use active voice | Bury the recommendation in passive constructions |

## Mandatory cautions

### Privilege marking
If the letter contains legal advice (almost always), mark it at the top:

```
PRIVILEGED AND CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION
```

In DIFC/ADGM/UK contexts, the equivalent is:

```
LEGALLY PRIVILEGED AND CONFIDENTIAL
```

In Lebanon and UAE civil-law contexts, legal privilege exists but is narrower than in common-law systems. Include the marking but note to the supervising lawyer that privilege scope should be confirmed.

### Reservation of rights
In demand letters and default notices:

```
Nothing in this letter constitutes a waiver of any of our client's rights, all of which are expressly reserved.
```

### Reference to engagement letter
For opinions and advice letters:

```
This advice is given within the scope of our retainer as defined in our engagement letter dated [date]. It does not extend to [any matters not covered].
```

### Avoiding outcome promises

Never state:
- "We will succeed" / "You will win"
- "There is no risk"
- "This is definitely enforceable"

Use calibrated language:
- "The clause is likely enforceable if..."
- "We consider there to be a strong argument that..."
- "Based on current law, the risk of...is low, but cannot be eliminated."

## Jurisdiction-specific considerations

| Jurisdiction | Notes |
|---|---|
| UAE (onshore) | Letters to government entities should be in Arabic or bilingual (Arabic + English). Use formal Arabic titles. |
| KSA | Arabic-only or Arabic-primary for most formal correspondence. English version may be attached as a courtesy. |
| DIFC / ADGM | English is standard. Privilege rules follow English common law. |
| Lebanon | French or Arabic formal letters are common; English accepted in international practice. |
| Egypt | Arabic is required for official correspondence; English used in international commercial matters. |

## Related skills

- [[output-executive-summary-first]] — BLUF opening for partner/client letters where the bottom line comes first
- [[output-creac-structure]] — the analytical structure within the body of the letter
- [[output-bilingual-formatting]] — for bilingual Arabic-English letters
- [[conversation-disclaimer]] — whether and where to include legal advice disclaimers
