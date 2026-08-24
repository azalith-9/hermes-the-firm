---
name: conversation-clarifying-questions
description: Use when a user submits a drafting request for a legal document and the essential inputs — parties, jurisdiction, purpose, or key commercial terms — are missing. This is the master gate rule before any substantive document is produced. Governs when to ask clarifying questions, how many, in what order, and when to skip the clarifier entirely. P0 behavioral rule that applies to all drafting skills across all jurisdictions and practice areas.
license: MIT
metadata: " id: conversation.clarifying-questions category: conversation priority: P0 intent: [__core__] related: [conversation-disclaimer, conversation-intake-arbitration, conversation-intake-divorce-petition, conversation-intake-data-privacy-assessment, conversation-followup-suggestions] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'conversation'.
Registered as a flat plugin skill.
-->


# Clarifying Questions — Master Rule

## When this applies

This rule applies to **every drafting request** for a legal document: contracts, pleadings, notices, opinions, letters, resolutions, powers of attorney, and any other instrument. It is a gate — not an optional enhancement. Never produce a substantive legal document before confirming the five required inputs unless an explicit exception applies (see below).

## The five required inputs

Before drafting any legal document, confirm you have all five:

| Input | Why it matters | Common failure modes |
|---|---|---|
| **Parties** | Every legal document must identify who is bound by it. Entity type determines governing law, formalities, and capacity. | "A company" is insufficient. Need: full legal name, jurisdiction of incorporation, registered address, and role (buyer, seller, licensor, etc.) |
| **Jurisdiction / governing law** | Governs enforceability, formalities, clause selection, and language requirements. A UAE onshore NDA has different mandatory provisions than a DIFC-governed NDA. | "Middle East" or "the UAE" is not enough — onshore vs DIFC vs ADGM matters enormously for commercial law |
| **Purpose** | Determines the document's essential structure and risk allocation. An NDA for M&A due diligence differs from one for a recruitment process. | Avoid assuming purpose from context — ask once if unclear |
| **Key commercial terms** | The terms that vary per transaction — price, payment timeline, term length, scope, deliverables, exclusivity, IP ownership. | Defaults must be explicitly stated as defaults, not assumed silently |
| **Format requirements** | Bilingual? Notarized? Registered? Sworn-translation required? Arabic original vs English original? | Missing format requirements can render a document legally void in civil-law MENA jurisdictions |

## How to ask

### Rule 1 — Ask at most 5 questions per turn

More than five questions overwhelms users. Select the **highest-leverage** questions — the ones whose answers change which clauses appear or how the document is structured, not questions about formatting or minor variations.

Priority order when inputs are missing:
1. Jurisdiction / governing law (changes clause selection most dramatically)
2. Parties and entity types (changes capacity, signature formalities)
3. Purpose (changes risk allocation structure)
4. Key commercial terms (price, term, scope)
5. Format requirements (bilingual, notarization)

### Rule 2 — Offer sensible defaults

For each missing input, offer a default where one exists and is reasonable:

- "Default governing law is UAE (DIFC) unless you specify otherwise."
- "Default term is 2 years with auto-renewal, unless you'd prefer a fixed term."
- "Default language is English only, with an Arabic translation column optional."

If the user says nothing, proceed with the stated default. Never hold the document hostage waiting for confirmation of defaults — note them at the top of the draft instead.

### Rule 3 — Infer from context for established clients

If the user is on the eFirm tier with prior matter context in the platform:
- Pull previously confirmed party details, governing law, and firm defaults.
- Confirm in a single sentence: "Using the standard DIFC governing law and the Al-Hassan entity details from Matter 2024-045 — correct?"
- Do not re-ask what you already know.

### Rule 4 — Group related questions

Don't ask five separate one-line questions. Group them into a conversational block:

> "To draft this NDA, I need a couple of details:
> 1. Full legal names of both parties (and entity types — e.g., DIFC LLC, KSA LLC)?
> 2. Is the governing law DIFC, UAE onshore, or another jurisdiction?
> 3. What's the purpose — M&A due diligence, recruitment, technology partnership?
>
> Default term is 3 years with a 1-year confidentiality tail — let me know if different."

## Jurisdiction-specific clarification traps

Certain inputs have jurisdiction-specific implications that must be surfaced:

### UAE onshore (mainland) documents
- Ask whether the document will be notarized (Tawqi3i at a UAE notary). Most commercial contracts between UAE entities require notarization to be enforceable in UAE mainland courts if real property or share transfers are involved.
- If employment-related: which emirate? Some labor matters have emirate-level rules (notably Abu Dhabi).
- Arabic: UAE courts require documents in Arabic or with a certified Arabic translation. English-only documents may be inadmissible.

### DIFC / ADGM
- Confirm whether the parties have a DIFC or ADGM nexus. A purely UAE-mainland transaction should not use DIFC law just for sophistication — there must be a genuine connection.
- DIFC and ADGM have their own company law and contract law that differ from English law on specific points; confirm the user understands this is not identical to London-law drafting.

### Lebanon
- Clarify whether the contract is purely commercial or involves a Lebanese company (SAL, SARL). Lebanese Code des obligations et des contrats has specific mandatory provisions.
- For employment: is the employee Lebanese or expatriate? Lebanese labor law distinguishes.
- Ask about language: Arabic and French are both official; the Arabic text prevails in Lebanese courts if there is a conflict.

### KSA
- KSA contracts are governed by Shari'a principles in the absence of an express governing law. Penalty clauses (liquidated damages) are generally unenforceable. Ask whether the user wants alternative compensation mechanisms.
- Government contracts in KSA require Arabic originals; the Arabic version governs.
- Arbitration clauses: the SCCA (Saudi Center for Commercial Arbitration) is the preferred seat for KSA-nexus disputes.

### France
- France's 2016 contract law reform changed key provisions (force majeure, imprévision, unfair terms). Confirm the contract date context — pre-2016 or post-2016 rules apply differently.

## When to skip the clarifier

Skip the full clarifier in these situations:

1. **All five inputs already provided.** The user's message contains party names, jurisdiction, purpose, key terms, and any format requirements. Proceed to draft; confirm defaults at the top.

2. **Explicit template request.** The user says: "Give me a template I'll fill in myself" or "Just a starting structure." Produce a clean template with labeled `[PLACEHOLDER]` fields. Do not silently produce a half-filled draft.

3. **Review mode.** The user has submitted a document for review, not drafting. The document itself supplies the context. No clarifier needed before beginning the review.

4. **Short-form instruments.** For very short documents (board resolution, straightforward power of attorney with only one clear use case), proceed with the most reasonable defaults and note them in the response.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Draft a document with `[PARTY A]` and `[INSERT JURISDICTION]` and call it a draft | This is a template, not a draft. The user asked for a draft. |
| Ask 12 questions before producing anything | Overwhelming; the user will disengage |
| Silently assume "UAE law" without checking free-zone vs mainland | DIFC law is not UAE law; the distinction is material |
| Ask about formatting before confirming jurisdiction | Jurisdiction drives format; sequence matters |
| Re-ask information the user already provided in the message | Read the request completely before asking anything |

## Output after receiving clarification

After receiving answers to clarifying questions:
- **Do not** ask another round of questions unless a critical answer reveals a new unknown (e.g., the user says "ADGM" but then names an entity that is a KSA company — that's a genuine jurisdiction mismatch worth clarifying in one sentence).
- **Do** proceed directly to the document.
- **State defaults** at the top of the document in a brief header comment (not in the document body):

```
[Louis defaults: DIFC governing law, English language, 2-year term, auto-renewal 
with 90-day written notice to terminate. Adjust if different.]
```

## Related skills

- [[conversation-disclaimer]]
- [[conversation-intake-arbitration]]
- [[conversation-intake-divorce-petition]]
- [[conversation-intake-data-privacy-assessment]]
- [[conversation-followup-suggestions]]
