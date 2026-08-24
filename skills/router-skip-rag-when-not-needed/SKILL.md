---
name: router-skip-rag-when-not-needed
description: Use to determine whether RAG (Retrieval-Augmented Generation) retrieval should be skipped for a given request. RAG retrieval is the primary source of latency in legal AI chat responses; skipping it for requests that do not need it — generic legal questions, boilerplate drafting, chitchat, admin queries — reduces first-token latency by 600–900ms at p95. Defines precise skip and no-skip conditions with rationale for each.
license: MIT
metadata: " id: router.skip-rag-when-not-needed category: router priority: P0 intent: [__router__] related: [router-tool-selector, router-complexity-grader, router-intent-detection, router-skip-rag-when-not-needed] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'router'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Skip RAG When Not Needed

## Purpose

RAG retrieval — searching the firm's knowledge base, public legal corpus, or personal document store — is valuable when the answer genuinely requires it. It is expensive when it does not. The round-trip for a RAG search and result incorporation adds 600–900ms to p95 latency, which is a material degradation of perceived response speed. On mobile and voice surfaces, this degradation is severely felt.

This skill is the anti-latency gate: it runs immediately after intent detection and complexity grading, and before any RAG call is issued. Its job is to identify the clear cases where RAG is not needed and suppress the retrieval call.

## Skip Conditions — Do NOT run RAG

### Condition 1 — No Reference to Private or Specific Documents

If the user's message contains none of the following, there is no reason to retrieve from a private corpus:
- "my", "our", "the contract", "the matter", "the document", "the file"
- A specific client name, matter reference, or case number
- "the one I uploaded", "the lease", "their NDA", "this clause"
- A project or workspace name

Without these signals, the user is asking a question that the model should answer from its training, not from private documents.

### Condition 2 — Generic Legal Knowledge Question

Questions about well-established legal principles, definitions, or general rules do not require RAG:

- "What is consideration in contract law?"
- "What does force majeure mean?"
- "Explain the difference between a representation and a warranty"
- "What is the general limitation period for contract claims in the UAE?" (well-established statutory rule)
- "What are the elements of a valid contract?"
- "What is the difference between a director and a shareholder?"

These questions have stable answers in the model's training. RAG retrieval will not improve the answer and may introduce noise from documents that are not directly relevant.

### Condition 3 — Boilerplate Generation Without Firm-Specific Context

Requests to generate standard boilerplate that does not depend on a specific client or matter:
- "Can you generate a standard NDA template for a technology company?"
- "Write me a confidentiality clause for an employment contract"
- "Draft a force majeure clause"
- "Give me a standard limitation of liability clause"

The model knows these constructs from training. There is no additional value from retrieving the firm's existing precedent unless the user has indicated they want firm-style language ("draft this in our standard style" or "use our template").

### Condition 4 — Admin, Chitchat, and Feature Questions

Questions about the platform, billing, account settings, or general conversation:
- "How do I upgrade my plan?"
- "What features are available in the Pro tier?"
- "Hello, how are you?"
- "Can you work in French?"

These never need knowledge base retrieval.

### Condition 5 — Pure Calculation Tasks

If the request is a calculation (EOSG, interest, limitation period deadline) with all variables provided:
- "If an employee was hired on 1 January 2020 and terminated on 1 June 2025, what is their UAE EOSG?"

The calculator tool is needed; the RAG tool is not. These are separate systems.

## No-Skip Conditions — RAG IS Required

### Condition A — Pronoun or Reference to Prior Conversation or Document

If the user references something from the current conversation or a previously uploaded document:
- "Rewrite it in plain English" → "it" is a prior document; must have that document in context
- "What does clause 5 say about termination?" → requires the specific contract
- "Based on the lease we discussed…" → context from prior turns

RAG over personal document store (or conversation history context) is mandatory here.

### Condition B — Workspace or Matter is Active

If the user's session is scoped to a specific matter or workspace and they ask about "the lease", "their NDA", "this clause" — even without explicit reference to a document — the workspace context implies that firm-specific documents should be retrieved.

### Condition C — Precedent Search Request

If the user explicitly asks for precedent examples:
- "Find similar clauses in our knowledge base"
- "What's our standard approach to IP indemnification?"
- "Do we have a template for this?"

These require RAG over the firm's precedent library.

### Condition D — Recency-Sensitive Questions

If the question requires information that may have changed since training:
- "What are the current RERA rent cap percentages for 2025?"
- "Has the KSA PDPL been amended recently?"

This needs web search, not RAG over the private corpus. But it does need *some* retrieval. Do not conflate "skip RAG" with "skip all tools" — the web-search tool may still be needed.

## Latency Budget

- RAG retrieval (private corpus, vector search) target: ≤ 900ms at p95
- Web search: ≤ 1,500ms at p95
- If RAG is skipped: first token should be available in < 1,500ms at p95 on web; < 800ms on cached short-answer paths

Monitoring: log RAG skip/no-skip decision with the reason code for latency analysis. This data informs ongoing calibration of the skip conditions.

## Output

Emit a routing decision:

```json
{
  "skip_rag": true/false,
  "reason_code": "no-private-reference|generic-knowledge|boilerplate|admin-chitchat|calculation",
  "tools_still_needed": ["web-search", "calculator"],
  "latency_target_ms": <integer>
}
```

If `skip_rag: false`, the reason must be one of: `prior-document-reference`, `workspace-scoped`, `precedent-search`, `recency-sensitive`.

## Why This Matters

A RAG retrieval that finds nothing (because the user was asking a generic question) wastes time, adds latency, and may introduce low-relevance retrieved chunks that degrade response quality. The skip gate costs almost nothing to run (it is a pattern-match on the message, not a model call) and prevents the most common source of unnecessary latency in legal AI deployments.

## Related Skills

- [[router-tool-selector]]
- [[router-complexity-grader]]
- [[router-intent-detection]]
