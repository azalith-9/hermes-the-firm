---
name: router-complexity-grader
description: Use at the start of every request pipeline to grade the complexity of the incoming request and assign it to a complexity bucket. Buckets drive downstream model selection, token budget, tool activation, and latency targets. Five buckets ranging from short-answer (under 200 tokens) to agentic (multi-step with tool calls and gates). Outputs a JSON object consumed by the tool selector and model router.
license: MIT
metadata: " id: router.complexity-grader category: router priority: P0 intent: [__router__] related: [router-intent-detection, router-tool-selector, router-confidence-scorer, router-platform-aware, router-jurisdiction-detector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'router'.
Registered as a flat plugin skill.
-->


# Complexity Grader

## Purpose

The Complexity Grader assigns every incoming request to exactly one complexity bucket before any other processing occurs. The bucket drives:

1. **Model selection**: short-answer requests do not need the highest-capability model; deep-research and full-document requests do
2. **Token budget**: estimated output token count allows the inference layer to pre-allocate compute and enforce latency budgets
3. **Tool activation**: only certain buckets unlock RAG, web search, or agentic tool calls
4. **Latency targeting**: web surface has hard latency SLAs (≤4s for short-answer; ≤12s for medium); the grader ensures requests are not over-processed

## Inputs / Signals

| Signal | How to read it |
|---|---|
| Message length | Long message with pasted document → likely medium or full-document |
| Verb intent | "What is…" / "Define" → short-answer; "Draft…" → medium/full-document; "Compare all jurisdictions…" → deep-research |
| Quantifier adverbs | "thoroughly", "all options", "comprehensive", "compare" → escalate to deep-research |
| Number of jurisdictions | >2 jurisdictions mentioned → deep-research |
| Document attachment | Any attached or pasted document → at least medium; multi-document → full-document |
| Workflow reference | Reference to a workflow.* or agentic skill → agentic |
| Domain specificity | Named statute / article number → may require web check (recency) |

## Complexity Buckets

### `short-answer`
- **Estimated output**: ≤ 200 tokens
- **Typical requests**: single factual question ("What is the limitation period for contract claims in the UAE?"), greeting, yes/no legal question, simple definition, quick calculation with a single variable
- **Tools activated**: none; model answers from training
- **Latency target**: ≤ 4 seconds first token on web; ≤ 2 seconds on API

### `medium`
- **Estimated output**: 200–1,500 tokens
- **Typical requests**: drafting a single clause, reviewing a 1–2 page excerpt, answering a single-jurisdiction legal question with some elaboration, producing a structured short memo
- **Tools activated**: RAG if user references their own documents; no web search unless freshness is critical
- **Latency target**: ≤ 12 seconds on web

### `deep-research`
- **Estimated output**: 1,500+ tokens
- **Typical requests**: multi-jurisdiction comparison, recent amendment lookup, regulatory landscape overview, case law research, comparative analysis with recommendations
- **Tools activated**: RAG (firm KB + public legal corpus), web search for recent amendments/rulings, legal data hunter if needed
- **Latency target**: up to 30 seconds acceptable with a progress indicator; warn user if exceeding 20 seconds

### `full-document`
- **Estimated output**: 3,000+ tokens, structured output
- **Typical requests**: full contract draft, complete memorandum of law, due diligence report, full lease or NDA generation
- **Tools activated**: RAG for precedents; template engine if available; web for any jurisdiction-specific verification
- **Latency target**: streaming output expected; total generation may take 60–120 seconds; user should see progress

### `agentic`
- **Estimated output**: multi-step, variable
- **Typical requests**: any request referencing a `workflow.*` skill, multi-step M&A diligence, automated clause-by-clause review with output to a structured report, deposition prep workflow, automated regulatory filing sequence
- **Tools activated**: full tool suite as specified by the workflow; may include connector calls (Linear, CRM, document storage), calculator tools, multi-turn confirmation gates
- **Latency target**: asynchronous; user should be informed that results will be delivered in stages

## Logic — Grading Rules

Apply rules in order; first match wins:

1. If the message is a greeting, chitchat, admin question, or feature question about Louis → `short-answer`
2. If the message contains a workflow.* reference or multi-step procedure description → `agentic`
3. If the message attaches multiple documents (>2) or asks for a complete contract draft → `full-document`
4. If the message contains "compare", "all jurisdictions", "comprehensive", "thoroughly", "case law search", "recent amendments", or ≥3 jurisdictions → `deep-research`
5. If the message attaches a single document for review or asks for a single clause draft → `medium`
6. If none of the above match → `short-answer` (default; err toward the lighter bucket)

## Output

Return a single JSON object on one line:

```json
{
  "complexity": "short-answer|medium|deep-research|full-document|agentic",
  "estimated_tokens_out": <integer>,
  "needs_tools": ["rag", "web", "calc", "legal-data-hunter"],
  "confidence": 0.0-1.0,
  "grading_reason": "<one sentence>"
}
```

If the request is ambiguous between two buckets, default to the lighter bucket and include a note in `grading_reason`. Over-grading (escalating a short-answer to deep-research) wastes compute and harms latency more than under-grading.

## Why This Matters

Latency is the single most reported user-experience complaint in legal AI products. The grader prevents two failure modes:

1. **Over-processing**: a greeting triggers RAG retrieval and web search → 8-second response to "Hi"
2. **Under-processing**: a multi-jurisdiction regulatory comparison is handled with no tools → hallucinated answer citing non-existent statutes

The grader is a cheap operation (runs in < 100ms) and pays for itself in reduced compute waste and improved latency across all other requests.

## Related Skills

- [[router-intent-detection]]
- [[router-tool-selector]]
- [[router-confidence-scorer]]
- [[router-platform-aware]]
- [[router-jurisdiction-detector]]
- [[router-skip-rag-when-not-needed]]
