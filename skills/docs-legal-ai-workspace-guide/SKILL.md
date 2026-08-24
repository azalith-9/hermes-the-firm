---
name: docs-legal-ai-workspace-guide
description: Use when a user needs guidance on how to use the full legal AI workspace — the chat interface, document drafting, matter management, citations, risk analysis, and automated workflow features. This is the primary end-user guide documentation skill, covering all major workspace capabilities with topical sections designed for both new and experienced users.
license: MIT
metadata: " id: docs.legal-ai-workspace-guide category: docs jurisdictions: [__multi__] priority: P2 intent: [__docs__, workspace guide, user guide, how to use, features, onboarding] related: [docs-legal-os-overview, docs-mobile-app-onboarding, docs-faq-pack, docs-enterprise-deployment] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Legal AI Workspace Guide

## What the workspace is

The legal AI workspace is the central environment where legal professionals interact with the platform's AI capabilities across the full legal workflow: chat (research and advice), document drafting, contract review, matter management, citation surfacing, and risk flagging. It is designed for day-to-day use by lawyers, in-house counsel, paralegals, and legal operations professionals.

## Core features

### Chat — AI legal assistant

The chat interface is the starting point for most legal tasks.

- **Ask a question**: type a legal question directly. The assistant answers using calibrated uncertainty language (see platform behavioral standards), cites sources by jurisdiction, and offers next-step actions.
- **Intake for drafting**: type "draft an NDA for..." and the assistant will run the appropriate intake conversation before generating the document.
- **Research mode**: for complex legal questions, prefix your query with "Research:" to invoke the deep research skill (uses more credits; returns more comprehensive multi-source analysis).
- **Jurisdiction selection**: you can specify jurisdiction in the query ("...under UAE law", "...under DIFC") or set a workspace default in **Settings → Workspace → Default Jurisdiction**.
- **Arabic / bilingual mode**: for Arabic-language queries or bilingual output, type in Arabic or add "bilingual output" to your request.

### Document drafting

Invoke drafting skills directly from chat or from the **New Document** button.

1. **Select document type**: NDA, employment contract, SHA, MSA, lease, loan agreement, will, POA, litigation brief, and 200+ other types.
2. **Complete intake**: the assistant may ask clarifying questions (jurisdiction, parties, key terms) before generating.
3. **Review the draft**: the draft appears in the document editor. Review, redline, and edit inline.
4. **Export**: export as .docx (Microsoft Word), .pdf, or bilingual Arabic-English .docx. Export costs credits for premium formats.

### Contract review

Upload an existing contract (PDF or .docx) and invoke the review skill.

1. **Upload**: drag-and-drop or **Upload** button in the document panel.
2. **Select review type**: full review (all clauses), red-flag review (risks only), jurisdiction-specific review (e.g., "flag clauses non-compliant with UAE law").
3. **Review output**: structured report with: (a) clause-by-clause flags with severity (high/medium/low); (b) market-standard deviations; (c) recommended changes. Available as in-app comments or exported redline.

### Multi-document compare

Compare two versions of a contract to generate a redline and change summary.

1. Upload Version 1 and Version 2.
2. Invoke **Compare Documents**.
3. Output: tracked-changes redline (.docx) + change summary table (clause changed, nature of change, impact assessment).
Costs credits per document pair.

### Matters

Organize all work by client matter.

- **Create a matter**: **Matters → New Matter → Enter client name, matter name, type**.
- **Link documents**: all documents drafted or uploaded within a matter are linked to it.
- **Matter timeline**: chronological view of all activity on the matter.
- **Deadline tracking**: add deadlines (court filing dates, contract expiry, statute of limitations) and receive in-app reminders.
- **Team assignment**: assign matters to specific users within the workspace. Set access levels (view / comment / edit / own).
- **Matter export**: export the full matter file (all documents, timeline, notes) as a ZIP archive.

### Citations

The platform surfaces citations inline in AI-generated analysis.

- **Format**: statute name + article number (where available at high confidence), or institutional guidance reference.
- **Jurisdiction filter**: citations are filtered by the jurisdiction of the query/document.
- **Pinpoint citations**: for professional (B2B) users, citations include article-level pinpoints. See platform behavioral standards for citation confidence tiers.
- **Export with citations**: legal analysis exported as a memo includes an automatically generated footnote / endnote section.

### Risk analysis

The risk analyzer flags legal, commercial, and compliance risks in drafted or uploaded documents.

- **Risk categories**: high (likely to cause a dispute or regulatory issue), medium (suboptimal but not fatal), low (standard market deviation).
- **Jurisdiction overlay**: risk flags are calibrated to the document's governing law jurisdiction.
- **Suggested fixes**: each risk flag includes a suggested clause revision or next-step action.
- **Risk summary**: exportable one-page risk summary for client or board presentation.

### Flows — automated legal workflows

Flows are multi-step automated sequences for repetitive legal tasks.

Examples:
- **NDA processing flow**: receive an NDA by email → OCR ingest → risk review → generate markup → draft cover email with key issues → send to counterparty.
- **Employment onboarding flow**: trigger on HR system (new hire) → generate employment contract draft → route for partner review → send to employee via DocuSign.
- **Contract expiry reminder flow**: scan matter deadlines → send reminder 60/30/7 days before expiry → generate renewal draft if configured.

Flows require configuration by a workspace administrator. Pre-built flow templates are available in **Settings → Flows → Templates**.

## Getting started

1. **First login**: complete the onboarding checklist (set default jurisdiction, upload your firm logo, invite your first colleagues).
2. **First document**: try "Draft a mutual NDA between Acme Ltd and XYZ Corp, DIFC law, 2 years." This demonstrates the full intake → draft → review cycle.
3. **Upload an existing contract**: upload any contract and select "Red flag review" to see the risk analyzer in action.
4. **Create your first matter**: organize the NDA and any related documents into a matter to see the matter management features.

## Keyboard shortcuts

| Shortcut | Action |
|---|---|
| `Cmd/Ctrl + K` | Open command palette |
| `Cmd/Ctrl + N` | New document |
| `Cmd/Ctrl + M` | New matter |
| `Cmd/Ctrl + U` | Upload document |
| `Cmd/Ctrl + E` | Export current document |
| `Cmd/Ctrl + /` | Open help / ask the assistant |

## Related skills

- [[docs-legal-os-overview]]
- [[docs-mobile-app-onboarding]]
- [[docs-faq-pack]]
- [[docs-enterprise-deployment]]
