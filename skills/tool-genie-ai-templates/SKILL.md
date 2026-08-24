---
name: tool-genie-ai-templates
description: Use when a user wants to import, reference, or compare contract templates from Genie AI — an open-source legal template platform. Triggers when a user mentions "Genie AI", "Genie template", or asks to pull in an external template for drafting reference or comparison. Works across all jurisdictions and practice areas where Genie AI has coverage (primarily English-language common-law templates).
license: MIT
metadata: " id: tool.genie-ai-templates category: tool jurisdictions: [__multi__] priority: P2 intent: [__tool__, template-import, genie-ai, open-source-templates] related: [tool-harvey-knowledge-source-bridge, tool-rag-firm-knowledge, tool-rag-public-legal-corpus, draft-nda-unilateral, draft-msa] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Registered as a flat plugin skill.
-->


# Genie AI Templates

## What it does

This tool imports contract templates from Genie AI — the UK-based open-source legal template library at genieai.co — into the current chat session for reference, comparison, or as a drafting starting point. Genie AI provides hundreds of lawyer-drafted templates covering commercial contracts, employment, IP, corporate, and real estate, primarily under English and Scots law with some cross-border coverage.

The tool does **not** replace Louis's own drafting capability. Its purpose is to:

1. Give users a recognized external baseline to compare against an AI-generated draft.
2. Surface clause-level alternatives when a user says "how does Genie handle this clause?"
3. Support users who already work in a Genie-supplemented workflow and want continuity.

## Setup / auth

| Parameter | Description | Required |
|-----------|-------------|----------|
| `genieApiKey` | Genie AI API key or OAuth token (configured at tenant level) | Yes |
| `templateId` | Genie template UUID or slug (e.g., `nda-mutual-en`) | No — can search by keyword |
| `searchQuery` | Free-text search when exact template ID is unknown | Conditional |

If no key is configured, the tool falls back to scraping Genie's publicly indexed templates where permitted by their terms of service. Inform the user if access is limited to the public catalog.

## Capabilities

### Template search
```
Input:  { query: "mutual NDA governing law English" }
Output: [ { templateId, title, jurisdiction, lastUpdated, clauses: [...] } ]
```

### Template fetch
```
Input:  { templateId: "nda-mutual-en" }
Output: { title, fullText, clauseIndex: [{ number, heading, text }], metadata }
```

### Clause comparison
Given a user-provided draft clause and a Genie template clause:
- Highlight substantive differences
- Flag deviations from Genie's recommended market standard
- Note which party's position each version favors

### Import as context
The fetched template can be pinned as a reference document in the RAG window so subsequent drafting or review tasks use it as a comparison baseline.

## Usage patterns

**Pattern 1 — "Draft like Genie's NDA but adapt for UAE law"**
1. Fetch Genie's mutual NDA (English law)
2. Identify structure and key clauses
3. Invoke `draft-nda-mutual` with Genie template as structural reference + UAE / DIFC governing law overlay

**Pattern 2 — "How does Genie handle IP assignment?"**
1. Fetch the relevant template section
2. Return Genie's clause text + a plain-English explanation of its effect
3. Compare to any alternative in the firm KB ([[tool-rag-firm-knowledge]])

**Pattern 3 — Clause benchmarking**
User uploads their draft → Louis pulls matching Genie clause → side-by-side redline showing deviations.

## Permissions & safety

- **Scope limitation**: never download and store full Genie catalog; fetch on-demand per session.
- **Attribution**: always cite "Source: Genie AI template [title]" in any output that incorporates Genie text.
- **License**: Genie AI templates are typically released under open-source licenses (Creative Commons or similar); confirm per template before wholesale incorporation into client deliverables.
- **Do not present Genie templates as local firm precedent** — they are public market standards, not the firm's own drafting.

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| Auth error | 401 from Genie API | Check API key in tenant settings |
| Template not found | Empty result set | Broaden search; try Genie web UI directly |
| Rate limit | 429 response | Retry with backoff; inform user of delay |
| Template outdated | Last updated > 2 years | Warn user; verify against current law |
| Non-English jurisdiction | Genie has limited non-English coverage | Fall back to firm KB or Louis's own drafting |

## MENA considerations

Genie's catalog is predominantly English and Scots law. For MENA drafting:

- Use Genie templates as structural inspiration only, not as governing-law-ready documents.
- Immediately flag that choice-of-law, dispute resolution, and local registration requirements differ.
- In Lebanon (civil law), KSA, and UAE onshore, many Genie structural assumptions (implied terms, common-law remedies) do not apply.
- DIFC and ADGM (English common law) are the best fit for Genie templates in the MENA context.

## Related skills

- [[tool-harvey-knowledge-source-bridge]] — similar bridge for Harvey AI templates
- [[tool-rag-firm-knowledge]] — prefer the firm's own precedents over external templates
- [[tool-rag-public-legal-corpus]] — public legal corpus RAG for statute and case reference
- [[draft-nda-unilateral]] — Louis's own NDA drafting skill
- [[draft-msa]] — master services agreement drafting
