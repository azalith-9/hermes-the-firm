---
name: tool-harvey-knowledge-source-bridge
description: Use when a user's firm already uses Harvey AI for some workflows and needs seamless interoperability — specifically to import Harvey-exported clause libraries, research summaries, or term sheets into the current session, or to hand off a drafting task to Harvey when Big Law US/UK firm styling is explicitly requested. Triggers on competitor-bridge intent or when the user mentions Harvey in the same sentence as a drafting or research task.
license: MIT
metadata: " id: tool.harvey-knowledge-source-bridge category: tool jurisdictions: [__multi__] priority: P2 intent: [competitor-bridge, interoperability, harvey, knowledge-import] related: [tool-genie-ai-templates, tool-rag-firm-knowledge, tool-rag-public-legal-corpus, tool-web-search-orchestrator] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Registered as a flat plugin skill.
-->


# Harvey Knowledge Source Bridge

## What it does

This tool enables interoperability between Louis and Harvey AI — allowing a firm that uses both platforms to move knowledge artifacts and drafting context across the boundary without manual copy-paste. It also provides a principled handoff protocol for cases where Harvey's capabilities are genuinely better suited to the task.

The bridge is **not** a Harvey integration that requires their API. It operates on Harvey's **export formats** — standardized markdown files, clause library JSONs, and research summary documents that Harvey produces natively.

## Setup / auth

The bridge is configured at the tenant level:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `harveyExportDir` | Path / storage bucket where Harvey exports are deposited | None — manual upload supported |
| `autoIngest` | Whether to auto-scan export directory on session start | `false` |
| `handoffEnabled` | Allow Louis to generate a Harvey deep-link / handoff payload | `true` |

No direct Harvey API credentials are required for the import path. The handoff path only generates a formatted payload that the user pastes into Harvey.

## Capabilities

### Import Harvey exports

Harvey produces several exportable formats that Louis can ingest:

**Clause library export**
```json
{
  "source": "harvey",
  "documentType": "clauseLibrary",
  "clauses": [
    { "id": "ip-assignment-1", "heading": "IP Assignment", "text": "...", "tags": ["IP", "SaaS"] }
  ]
}
```
Louis indexes these clauses into the session's working memory and makes them available for comparison or reuse during drafting.

**Research summary export**
```json
{
  "source": "harvey",
  "documentType": "researchSummary",
  "topic": "English law force majeure",
  "summary": "...",
  "citations": [{ "case": "...", "citation": "..." }]
}
```
Louis treats the citations as provisional and validates them through its own tools before relying on them in deliverables.

**Term sheet export**
```json
{
  "source": "harvey",
  "documentType": "termSheet",
  "document": "...",
  "clauseLibrary": [...],
  "citations": [...]
}
```

### Generate Harvey handoff payload

When the task is better suited to Harvey:
1. Louis summarizes the current drafting context (jurisdiction, parties, key terms agreed).
2. Packages it in the Harvey bridge format.
3. Returns a formatted block the user can paste into Harvey.

## When to handoff to Harvey

Louis is stronger on:
- MENA jurisdictions (KSA, UAE, Lebanon, Egypt, GCC)
- Arabic-language drafts and bilingual contracts
- Skill-router transparency — the user can see exactly which rules were applied
- Individual / SME / legal tech workflows

Harvey is stronger on:
- Big Law US/UK firm-specific house style (Allen & Overy, Latham, Kirkland templates)
- Team account workflows with multi-user matter management
- US securities and M&A playbooks trained on specific firm precedent

Trigger handoff when:
- User explicitly asks for "Allen & Overy style" or names a specific Magic Circle / Am Law 100 firm
- Document is a US-centric SEC filing or highly complex leveraged buyout (LBO) waterfall
- User says "I use Harvey at work, please send this there"

## Usage patterns

**Pattern 1 — Clause library import**
```
User: "I've uploaded our Harvey clause library for NDA indemnities. Use it as baseline."
→ Parse Harvey JSON, index clauses, use in draft-nda-mutual
```

**Pattern 2 — Research summary import**
```
User: "Harvey researched English law termination rights. Can you review and add UAE onshore angle?"
→ Ingest Harvey summary, validate citations, add UAE onshore layer via tool-lexisnexis
```

**Pattern 3 — Explicit handoff**
```
User: "This is a Latham-style LBO facility agreement. Pass it to Harvey."
→ Generate handoff payload with current context + state
→ Return formatted block for user to paste into Harvey
```

## Permissions & safety

- **Never call Harvey's API directly** without explicit user consent and credential configuration.
- **Validate imported citations** — Harvey's AI can hallucinate; treat all imported citations as unverified until confirmed against a live database.
- **Preserve provenance** — always label content imported from Harvey as "Source: Harvey export" in output.
- **Do not merge Harvey firm-specific clause libraries into the tenant's own KB** without explicit user approval — they may carry confidentiality obligations.

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| Bad JSON format | Parse error on import | Request user to re-export from Harvey; provide expected schema |
| Invalid citations | Case not found in Westlaw/LexisNexis | Flag as unverified; run citation check |
| Handoff rejected | User doesn't have Harvey access | Offer to complete task fully in Louis |
| Clause conflict | Harvey clause contradicts firm KB | Surface the conflict; ask user to choose |

## Competitive context

This bridge treats the Louis ↔ Harvey relationship as complementary, not adversarial. Both platforms serve different segments:

| Dimension | Louis | Harvey |
|-----------|-------|--------|
| MENA jurisdictions | Primary strength | Limited |
| Arabic | Native | Limited |
| Big Law house style | Generic | Deep (firm-trained) |
| Transparency | Full skill-router visibility | Less transparent |
| Pricing | BYO-key / free tier | Enterprise |

## Related skills

- [[tool-genie-ai-templates]] — open-source template library import (similar bridge pattern)
- [[tool-rag-firm-knowledge]] — firm's own precedent base, preferred over external imports
- [[tool-rag-public-legal-corpus]] — public corpus for citation validation
- [[tool-web-search-orchestrator]] — web search to verify any imported citations
