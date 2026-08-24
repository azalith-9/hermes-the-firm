---
name: heuristic-party-names-consistency
description: Use as a post-draft quality check on any multi-party legal document. Enforces consistent use of party names and defined terms throughout a document and across schedules — correct introduction in the parties block, single consistent short-form, consistent capitalization, and cross-document alignment. Party name inconsistencies are a common drafting error that creates ambiguity, undermines enforceability, and signals low-quality drafting to opposing counsel.
license: MIT
metadata: " id: heuristic.party-names-consistency category: heuristic priority: P1 intent: [__core__, defined-terms, parties, drafting-quality, post-draft] related: [heuristic-numbers-and-dates-double-check, review-definitions-consistency, heuristic-bilingual-ar-en-mirror-clauses, heuristic-always-state-jurisdiction-first] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'heuristic'.
Registered as a flat plugin skill.
-->


# Party Names Consistency

## When this applies

Run this check after drafting any legal document that involves two or more parties. It applies to: commercial contracts, shareholder agreements, employment agreements, NDAs, real estate instruments, corporate resolutions, loan agreements, and any multi-party instrument.

Party name inconsistencies are among the most common and most visible drafting errors. They signal careless drafting to opposing counsel and can, in contested interpretations, create genuine ambiguity about which entity is bound by a given obligation.

## The standard pattern

### In the parties block (introduction)

Introduce every party with:
1. **Full legal name**: the exact name as it appears on the entity's incorporation certificate or official registration.
2. **Entity type and jurisdiction**: "(a company incorporated in Dubai under the Dubai Commercial Companies Law)"; "(a partnership registered in Lebanon)".
3. **Defined short form**: *(hereinafter "Provider")*, *(hereinafter the "Company")*, *(hereinafter "Lender")*.

**Example:**
> *"Acme Technology LLC, a limited liability company incorporated under the laws of the Dubai International Financial Centre (DIFC), with registered number [XXXXX] (hereinafter "the Company");"*

### Throughout the document

- Use **only the defined short form** for all subsequent references to the party.
- **Do not alternate** between the short form and the full name, or between two informal variants.
- **Capitalize consistently**: if the short form is "Provider" (capitalized), always write "Provider" — not "provider" or "service provider."

## Common errors

| Error type | Example | Risk |
|---|---|---|
| Switching between short form and full name | "The Provider shall…" in clause 3; "Acme Technology" in clause 7 | Ambiguity; suggests different entities |
| Alternating short forms | "Provider" and "Service Provider" used interchangeably | Creates argument that different parties are intended |
| Inconsistent capitalization | "the Provider" in some clauses; "the provider" in others | Minor ambiguity; signals careless drafting |
| Short form used before being defined | "The Supplier agrees to deliver…" in recitals without prior definition | Potentially invalidates the recital; creates interpretation dispute |
| Cross-document mismatch | Main agreement calls the party "Supplier"; schedule calls them "Vendor" | Schedule obligations may not clearly bind the defined party |
| Typo in the full legal name | "Acme Technologies LLC" vs "Acme Technology LLC" (the actual entity) | Serious: the wrong entity may be named; the contract may be with the wrong party |

## MENA-specific considerations

### Arabic-language party names

In bilingual documents, the Arabic-language version of the party's name must:
- Be the entity's **registered Arabic trading name** (not a transliteration), if the entity has an Arabic registration.
- Be consistent throughout the Arabic version of the document.
- Be defined with an Arabic short form that mirrors the English short form consistently.

**Trap**: Arabic names sometimes have multiple conventional transliterations into English (e.g., "Ahmad" vs "Ahmed"; "Muhammad" vs "Mohammed"). The name in the contract must match the entity's or individual's official documents exactly — use the passport, commercial registration, or other official document as the reference.

### Matching registration names

In MENA jurisdictions, a company's commercial registration name may differ from its trading name, its Arabic name, and its English name as they appear in different official documents. Before finalizing the parties block:
1. Obtain the commercial registration certificate.
2. Match the name exactly as it appears on the certificate.
3. Note any discrepancy between the Arabic and English versions of the name on the certificate.

### UAE freezones and mainland

A company can be: "Acme LLC (mainland)", "Acme FZE (JAFZA)", and "Acme DMCC (DMCC)" — three different legal entities even with similar names. Confirm which entity is the contracting party.

### KSA companies

Saudi commercial registrations have both Arabic names (mandatory) and English trading names (optional). The Arabic name on the commercial registration is the authoritative name for KSA legal purposes.

## The checking process

After drafting, run this systematic check:

1. **Extract the parties list**: list every party defined in the parties block, with their short forms.
2. **Search for each party**: scan the document for all references to each party — short form, long form, and any informal variant.
3. **Verify single short form**: confirm only one short form is used for each party throughout.
4. **Verify capitalization**: confirm the capitalization of each short form is consistent.
5. **Check cross-document**: if there are schedules, side letters, or ancillary agreements, verify that the same short forms and the same full legal names are used.
6. **Verify the parties block against source documents**: confirm the full legal name and entity type match the commercial registration or equivalent.

## In Louis

The Louis document workspace surfaces a right-rail "Parties" accordion that lists all defined parties and highlights instances where a party is referred to by a different name or variant. Use [[review-definitions-consistency]] for a broader check of all defined terms, not just party names.

## Related skills

- [[heuristic-numbers-and-dates-double-check]]
- [[review-definitions-consistency]]
- [[heuristic-bilingual-ar-en-mirror-clauses]]
- [[heuristic-always-state-jurisdiction-first]]
