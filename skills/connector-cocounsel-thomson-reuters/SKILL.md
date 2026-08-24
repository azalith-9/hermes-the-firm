---
name: connector-cocounsel-thomson-reuters
description: Use when a lawyer needs to hand off a complex legal research query to Thomson Reuters CoCounsel — the AI-assisted research layer built on TR's Westlaw database — because the query requires case law retrieval, statutory interpretation, or secondary-source research at a depth beyond the in-house skill set. Requires the user's organization to hold an active Thomson Reuters enterprise license. Triggers on requests involving US case law, multi-jurisdictional statutory research, or deep regulatory analysis where TR's curated legal database adds verifiable authority.
license: MIT
metadata: " id: connector.cocounsel-thomson-reuters category: connector jurisdictions: [__multi__] priority: P2 intent: [__connector__] related: [connector-eur-lex, connector-legifrance, connector-sec-edgar, connector-companies-house-uk, connector-legal-data-hunter] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Registered as a flat plugin skill.
-->


# Connector — Thomson Reuters CoCounsel

## What it does

Thomson Reuters CoCounsel is an AI-powered legal research assistant built on Thomson Reuters' authoritative legal content databases — primarily Westlaw (US, UK, Canada, Australia, and select EU jurisdictions) and Practical Law. The CoCounsel connector allows the legal-AI platform to route research queries that require verified, citation-backed legal authority to CoCounsel and return the results as structured research memos.

This connector is appropriate when:
- The research requires **actual case citations** that can be Shepardized or KeyCite-verified.
- The question involves **US federal or state statutory interpretation** from primary sources.
- The matter requires **secondary source research** (law review articles, Practical Law notes, treatise excerpts).
- The in-house skill set cannot answer the question with sufficient legal precision without risking hallucinated citations.

## Setup / auth

### Enterprise license requirement

This connector is not available to users on free or individual plans. It requires an active Thomson Reuters enterprise account with CoCounsel feature access enabled.

Authentication is **federated**: the user logs in to the legal-AI platform with their firm credentials, and the platform uses the firm's TR enterprise license to access CoCounsel on the user's behalf. No separate CoCounsel login is required within the assistant workflow.

Configuration steps:
1. Firm's TR account manager enables CoCounsel API access.
2. Platform receives TR OAuth client credentials for the firm's account.
3. Tokens are stored per-tenant in the platform's secrets manager.
4. Each authorized user within the firm can invoke CoCounsel via the assistant.

### Access model

| Access level | Who gets it | What they can do |
|---|---|---|
| Full CoCounsel | Partner-level or designated research lawyers | All research tasks, Westlaw full-text retrieval |
| Limited CoCounsel | Associates, trainees | Research tasks; Westlaw snippets (not full text) |
| No access | Non-lawyer staff | Cannot invoke this connector |

## Capabilities

### Research query hand-off

The primary function: accept a natural-language research question, forward it to CoCounsel, and return a structured research response.

The query should be framed as a focused legal question, not a vague topic. Examples of well-formed queries:
- "What is the current standard in the Second Circuit for piercing the corporate veil in a single-member LLC?"
- "Summarize UK Court of Appeal decisions from 2018–2024 on frustration of contract in force majeure clauses."
- "What are the disclosure obligations under SEC Rule 10b-5 in the context of a going-private transaction?"

CoCounsel returns:
- A research memo (typically 2–8 pages) with citations.
- Key cited cases with KeyCite flags (positive / negative treatment).
- Relevant statutes with current version notation.

### Practical Law retrieval

For transactional and compliance questions, CoCounsel can surface Practical Law notes — practice area–specific how-to guides and standard documents maintained by TR editorial teams. These are particularly useful for:
- Understanding deal market practice in a jurisdiction where the firm has limited experience.
- Identifying standard protective clauses in a specific transaction type.
- Compliance checklists for regulatory filings.

### Statutory and regulatory text

CoCounsel can retrieve current statutory text with amendment history and point to pending legislative changes (US Congress and select state legislatures).

## Usage patterns

### Pattern 1 — Research memo on a novel point

```
User: "Run a CoCounsel research on whether DIFC Courts can enforce an ICC arbitral award 
       where the award debtor's assets are in mainland UAE"
→ Connector formats the query for CoCounsel
→ Returns: research memo + key cases + applicable provisions (DIFC Arbitration Law, 
  UAE Federal Arbitration Law, New York Convention status)
→ Associate reviews and cites in their submissions
```

### Pattern 2 — Quick case law check before drafting

Before drafting a contractual limitation-of-liability clause for a US-governed SaaS agreement, use CoCounsel to retrieve the current state of enforceability in the relevant state (e.g., California's treatment of consequential damages waivers in B2B contracts).

### Pattern 3 — Regulatory compliance baseline

For a MENA fintech company seeking US market entry: use CoCounsel to pull a Practical Law overview of US money services business licensing requirements before the in-house team proceeds with a gap analysis.

## Jurisdictional scope — what CoCounsel covers well (and where it doesn't)

| Jurisdiction | CoCounsel coverage | MENA relevance note |
|---|---|---|
| United States | Excellent (all federal + 50 states) | Essential for US-listed MENA companies or US-governed contracts |
| United Kingdom | Good (English + Welsh law) | Relevant for DIFC-seat arbitration; UK precedent persuasive in DIFC Courts |
| Canada, Australia | Good | Occasional relevance for common-law analysis by analogy |
| EU member states | Partial (via EUR-Lex integration) | Use [[connector-eur-lex]] for primary EU law; CoCounsel adds secondary analysis |
| France | Limited | Use [[connector-legifrance]] for French primary sources |
| UAE / KSA / Lebanon | Not covered | Use [[connector-legal-data-hunter]] for MENA primary sources |
| DIFC / ADGM | Not natively covered | DIFC/ADGM law draws on English common law — CoCounsel's UK materials are relevant by analogy |

## Permissions & safety

- **No query logging by TR beyond standard usage analytics.** Confirm with the firm's TR account manager that CoCounsel query content is not used for TR model training.
- **Privilege caution.** Query content may reveal privileged strategy. Use CoCounsel for legal-question framing only — do not include client identifiers, confidential facts, or deal terms in the query text sent to CoCounsel.
- **Citation verification is mandatory.** CoCounsel-generated citations must be KeyCite-verified before submission to any court or regulatory body. The assistant must remind the user of this at every research hand-off.
- **No fabricated citations.** If CoCounsel returns a result that appears to cite a case the user cannot verify in Westlaw, treat it as suspect and escalate for manual verification.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| `License not found` | User's account not enabled for CoCounsel | Direct user to TR account manager; do not attempt workaround |
| Query too vague | CoCounsel returns low-confidence results | Prompt user to reframe as a specific legal question with jurisdiction and time period |
| Research memo has conflicting authorities | Circuit split or unsettled law | Surface the split clearly; do not resolve on the assistant's behalf |
| Result is outdated | Statute amended after TR's last update | Flag with "verify current statutory text" note; cross-reference with [[connector-eur-lex]] or [[connector-legifrance]] as appropriate |

## Related skills

- [[connector-eur-lex]]
- [[connector-legifrance]]
- [[connector-sec-edgar]]
- [[connector-companies-house-uk]]
- [[connector-legal-data-hunter]]
