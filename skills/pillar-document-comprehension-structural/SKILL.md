---
name: pillar-document-comprehension-structural
description: Internal architectural principle establishing that Louis treats legal documents as structured abstract syntax trees (Sections, Clauses, Defined Terms, Cross-references) rather than text blobs. Use when designing document review, redlining, comparison, or drafting features to understand how documents are parsed and queried.
license: MIT
metadata: " id: pillar.document-comprehension-structural category: pillar jurisdictions: [__multi__] priority: P3 intent: [__internal__] related: [pillar-architectural-bet-no-fine-tuning, pillar-context-across-apps, pillar-legal-skills-authoring, eng-document-parser, review-contract-general] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'pillar'.
Registered as a flat plugin skill.
-->


# Architectural Pillar: Structural Document Comprehension

## Scope

This pillar establishes that Louis must treat legal documents as **structured objects**, not flat text. A contract is not a string of characters — it is a hierarchy of sections, clauses, sub-clauses, defined terms, cross-references, schedules, and exhibits, each with specific legal function and meaning.

Structural comprehension enables capabilities that flat text parsing cannot: precise cross-reference validation, redline at clause level, definition tracking, obligation extraction, and comparison across document versions.

---

## The principle

> Louis treats docs as ASTs (Sections / Clauses / Defined-terms), not text blobs. Enables cross-ref, redline, compare.

AST here is used in the software sense — Abstract Syntax Tree — as a metaphor for a hierarchical, typed representation of the document's structure.

---

## Why structural comprehension matters

### Legal meaning is structural, not textual
A sentence in §14(b)(ii) means something different depending on whether §14 is an indemnification clause, a limitation of liability, or an IP ownership provision. The structure is load-bearing. Flat text parsing discards this structural context.

### Cross-references are a first-class legal artifact
Legal documents are dense with cross-references: "subject to §12.3", "as defined in Schedule A", "notwithstanding the foregoing in §8". These cross-references create legal obligations and qualifications. A system that cannot resolve cross-references cannot understand the document.

### Defined terms govern interpretation
Legal agreements define their own vocabulary. "Business Day" may mean something different in a UAE contract than in a UK contract. "Affiliate" is frequently defined to include or exclude certain types of entities. A system that does not track defined terms will misread the document.

### Redline and comparison require structural alignment
Comparing two versions of a document at the clause level — which clauses changed, which were added, which were deleted — requires a structural representation. Character-level diff is unreadable and unhelpful to a lawyer.

---

## Document AST structure

The parsed document is represented as a nested object:

```
Document
├── metadata
│   ├── title
│   ├── date
│   ├── parties [list]
│   ├── governing_law
│   ├── language
│   └── document_type [contract / court_filing / regulation / …]
├── defined_terms [dictionary: term → definition + location]
├── cross_references [map: source_location → target_location]
├── sections [list]
│   ├── Section
│   │   ├── id        [e.g., "§14"]
│   │   ├── title     [e.g., "Indemnification"]
│   │   ├── type      [clause_type: indemnity / limitation / IP / payment / term / …]
│   │   ├── text      [normalized text]
│   │   ├── obligations [extracted: party + obligation + condition + deadline]
│   │   └── sub_sections [recursive]
└── schedules [list]
    └── Schedule
        ├── id        [e.g., "Schedule A"]
        ├── title
        └── content   [structured per schedule type]
```

---

## Capabilities enabled by structural comprehension

| Capability | How structure enables it |
|-----------|------------------------|
| Cross-reference validation | Resolve every `§X.Y` or `defined term` reference; flag broken links |
| Defined-term tracking | Know the definition of every term throughout the document |
| Obligation extraction | Extract who owes what obligation to whom, by when |
| Clause-level redline | Diff two ASTs at the clause level; show meaningful changes |
| Document comparison | Compare two documents of the same type structurally |
| Risk flagging | Classify clause types and flag missing or unusual clauses |
| Template gap detection | Compare a document against a standard template structure |
| Defined-term consistency | Flag defined terms used but not defined, or defined but not used |

---

## Jurisdictional document structure variations

Legal document structure varies by jurisdiction and tradition:

| Jurisdiction | Structural characteristics |
|-------------|--------------------------|
| Common law (DIFC, ADGM, UK, US) | Long-form agreements with extensive recitals, definitions, schedules; cross-reference heavy; boilerplate clauses (entire agreement, severability, waiver) standardized |
| Civil law (LB, FR, EG, UAE-onshore) | Often shorter; governing law fills in gaps the contract doesn't address; less boilerplate redundancy; civil code articles provide default rules |
| Arabic-language contracts | Right-to-left rendering; defined terms often in Arabic; numbering conventions may differ; dual-language versions create interpretation risk |
| Court filings (MENA) | Structured by procedural rules; recitals → prayer; petitioner / respondent identification formal |
| Regulations / decrees | Part → Article → Paragraph → Sub-paragraph; often with transitional and definitional articles |

The parser must recognize document type and jurisdiction and apply the appropriate structural model.

---

## Implications for skill design

Skills that process documents must:
1. **Request the parsed AST**, not raw text, where structural access is needed
2. **Reference specific locations** in their output (§14(b)(ii), not "the indemnification clause" — precise references allow the user to find the clause immediately)
3. **Use defined terms correctly**: when the document defines "Company" as X, use "Company" (the defined term) not the party name X
4. **Validate cross-references** as part of any review skill — broken cross-references are a common and serious drafting error

---

## Failure modes and limits

| Failure | Description | Mitigation |
|---------|-------------|-----------|
| Poorly formatted document | Scanned PDF, no structure, tables as images | OCR pre-processing; flag low-confidence parse |
| Non-standard numbering | Roman numerals, unusual nesting, unnumbered clauses | Flexible parser with fallback to text-based heuristics |
| Dual-language documents | English and Arabic versions; which governs? | Flag governing language; parse both; note divergences |
| Very long documents | 200-page transaction documents | Chunked parsing; on-demand section loading |
| Handwritten annotations | Counterpart signatures, margin notes | Flag as out-of-scope for structural parse |

---

## Related skills

- [[pillar-architectural-bet-no-fine-tuning]] — why structural comprehension is a skills-layer capability, not a fine-tuning target
- [[pillar-context-across-apps]] — how parsed documents feed the matter context store
- [[eng-document-parser]] — engineering implementation of the document parser
- [[review-contract-general]] — contract review skill that consumes the parsed AST
- [[pillar-legal-skills-authoring]] — how skills are designed to consume document structure
