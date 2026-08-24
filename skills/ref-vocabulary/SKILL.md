---
name: ref-vocabulary
description: Use when any participant in the system — lawyer, developer, or AI — needs a precise shared definition of a legal-AI term. This reference pack covers the intersection of AI engineering vocabulary (prompts, context windows, RAG, agents, evals) and legal-practice concepts (skills, routers, hallucination, rubrics), enabling unambiguous communication across the two disciplines. Route here when a term appears in a skill description, onboarding document, or internal discussion and its meaning is disputed or unclear.
license: MIT
metadata: " id: ref.vocabulary category: ref priority: P1 intent: [__ref__, vocabulary, glossary, definitions, ai-legal-terms] related: [router-intent-classifier, research-deep-research-orchestrator, eval-output-quality, report-hallucination-rate-tracker] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ref'.
Registered as a flat plugin skill.
-->


# Reference — Legal + AI Vocabulary

A shared lexicon bridging AI-engineering terminology and legal-practice concepts. Use this pack to ensure consistent language across skills, documentation, onboarding materials, and inter-team communication.

## Scope

This reference covers two intersecting vocabularies:

1. **AI / LLM engineering terms** — the technical building blocks of any AI-assisted legal product.
2. **Legal-AI product terms** — the architectural concepts specific to legal AI assistants like Louis.

Terms are organized thematically. Where a term has a specific meaning in this product that differs from industry-wide usage, the product-specific meaning is noted.

---

## AI Engineering Terms

### Core inference concepts

| Term | Definition | Legal-AI relevance |
|------|------------|-------------------|
| **Prompt** | The text (and sometimes images or files) sent to the model as input at inference time. Includes the system prompt and the user's message. | Every skill is, at its core, a carefully structured prompt. Prompt quality determines output quality. |
| **System prompt** | Instructions prepended to a conversation, invisible to the end user but shaping the model's behavior, persona, and constraints for that session. In this product, a loaded *skill* is the system prompt. | Skills are system prompts. A bad system prompt produces bad legal output regardless of model capability. |
| **Context window** | The maximum number of tokens (roughly: sub-word units) that the model can "see" at once — spanning system prompt, conversation history, retrieved documents, and the pending response. Measured in tokens; current frontier models offer 128K–1M tokens. | Long contracts, multi-document due-diligence sets, and legislative bundles can exceed the window. Chunking + RAG strategies are required for very large document sets. |
| **Token** | The atomic unit the model processes. One token ≈ 0.75 English words or ≈ 0.5 Arabic words. Arabic is denser in characters per token due to script encoding. | Relevant for cost estimation and context-window planning in Arabic-language work. |
| **Temperature** | A sampling parameter (0–2) controlling output randomness. Low temperature (0–0.3) yields deterministic, consistent answers — preferred for legal work. High temperature increases creativity but also variance and hallucination risk. | Legal tasks should generally run at low temperature. |
| **Hallucination** | Output in which the model generates plausible-sounding but factually incorrect or entirely fabricated content — most dangerously: case citations, statute numbers, article text, regulatory thresholds, or party names that do not exist. | The single greatest risk in legal AI. Skills mitigate this via cite-or-bust rules, retrieval grounding, and confidence scoring. See [[report-hallucination-rate-tracker]]. |
| **Grounding** | Anchoring model output in retrieved, verified source material rather than relying solely on parametric (training-time) knowledge. | Grounding is why RAG is essential for legal work: the model's training-data cutoff makes statutes and case law stale within months. |

### Retrieval and augmentation

| Term | Definition | Legal-AI relevance |
|------|------------|-------------------|
| **RAG** (Retrieval-Augmented Generation) | An architecture in which the model's response is informed by documents retrieved from a vector database or search engine immediately before generation, rather than relying solely on training knowledge. | The standard architecture for legal AI. Enables citing current statutes, regulations, and cases. |
| **Embedding** | A dense numeric vector representing semantic content of text. Used to index and retrieve documents by meaning, not just keyword. | Legal document search uses embeddings so a query for "termination for cause" also retrieves "dismissal with valid reason" documents. |
| **Chunking** | Splitting long documents into smaller segments for indexing and retrieval. Chunk size (typically 256–1024 tokens) and overlap affect retrieval precision. | Long contracts and legislation must be chunked before indexing. Clause-level chunking often outperforms paragraph-level for contract work. |
| **Reranker** | A secondary model applied after initial retrieval to re-score and reorder retrieved chunks by relevance. Improves precision at the cost of additional latency. | Valuable for complex legal queries where initial BM25/embedding retrieval is noisy. |

### Agentic patterns

| Term | Definition | Legal-AI relevance |
|------|------------|-------------------|
| **Tool call** | A structured invocation of an external function — API, database query, calculator, or browser — by the model as part of its reasoning chain. The model emits a structured tool-call payload; the host executes it and returns results. | Legal AI tools include statute lookups, sanctions screeners, registry searchers, and document parsers. |
| **Agent** | A model-powered system that autonomously plans and executes multi-step tasks using tool calls and memory, rather than producing a single response. Can be single-agent or orchestrated multi-agent. | Deep research, due-diligence pipelines, and multi-jurisdiction comparisons are agent workflows. See [[research-deep-research-orchestrator]]. |
| **Orchestrator** | In a multi-agent system, the primary agent that decomposes the goal, delegates sub-tasks to specialist agents, and synthesizes their outputs. | The deep-research orchestrator is an example: it delegates to a statute-lookup agent, a case-law agent, a regulator-guidance agent, and synthesizes a memo. |
| **Memory** | Mechanisms for persisting information across turns or sessions — in-context (long context window), external (vector DB, key-value store), or summarized. | Legal matter context (parties, facts, prior research) should be persisted across a session to avoid re-elicitation. |
| **Function / Tool schema** | The JSON description of a tool's name, inputs, types, and behavior that the model reads to decide when and how to call it. | All connectors in this product expose a tool schema. |

### Evaluation and quality

| Term | Definition | Legal-AI relevance |
|------|------------|-------------------|
| **Eval** (evaluation) | A systematic assessment of model or skill output against a benchmark — typically a test set of prompts with known-good reference answers. Evals catch regressions when models or skills are updated. | Legal evals must test jurisdiction accuracy, citation correctness, and risk-flag completeness — not just fluency. |
| **Rubric** | A structured scoring guide defining what makes an output good, mediocre, or poor across specific dimensions. | Legal rubrics weight accuracy of legal principle > completeness > clarity > formatting. |
| **LLM-judge** | Using a more capable language model to automatically evaluate another model's outputs against a rubric, at scale. Supplements but does not replace human expert review. | Used in the hallucination-rate tracker to assess whether a cited article actually says what the model claimed. |
| **Benchmark** | A standardized test set or evaluation suite used for comparison across models or versions. | Internal legal benchmarks cover: statute-lookup accuracy, redline quality, jurisdiction-comparison depth. |
| **Latency** | The time from request submission to response completion. Measured P50/P95. | Critical for UX: redline on a 20-page contract must complete in a reasonable time even in deep-research mode. |
| **Cost** | Token cost of a model call (input + output tokens × per-token rate). Agents with many sub-calls can be expensive. | Deep-research workflows must budget credits and disclose cost to user before running. |

---

## Legal-AI Product Terms

### Architecture

| Term | Definition | Notes |
|------|------------|-------|
| **Skill** | A modular, self-contained system-prompt fragment that activates a specific behavior or capability in the AI assistant — e.g., drafting an NDA, reviewing a contract, looking up a statute. Skills are the primary unit of product quality. | This file describes the vocabulary used to build skills. |
| **Skill router** | An intent-classification layer that reads the user's message and activates the correct skill (or skill combination). The router must be fast and deterministic. | Routing errors are silent failures: a mis-routed query produces confidently wrong output in the wrong domain. See [[router-intent-classifier]]. |
| **Practice-area router** | A coarser router that first classifies the domain (corporate, employment, data-privacy, litigation, etc.) before fine-grained skill selection. | |
| **Knowledge base (KB)** | A reference-document pack embedded in or retrieved alongside a skill, providing jurisdiction-specific legal content that the model would otherwise hallucinate or get wrong. | KBs are indexed in the RAG layer; skills reference them via [[wikilinks]]. |
| **Pillar** | A major, cross-cutting KB or reference skill covering a foundational area (e.g., MENA corporate law, FATF AML framework). | |
| **Connector** | An integration skill that wraps an external data source or tool — a registry API, a legal database, a sanctions list — and exposes it to agent workflows via a standardized tool schema. | |
| **Eval suite** | The collection of test cases covering a skill's key behaviors, used to validate quality on every model or skill update. | |

### Quality and safety

| Term | Definition | Notes |
|------|------------|-------|
| **Cite-or-bust rule** | The rule that a skill must never fabricate a citation; if no verified source is found, it must say so explicitly rather than inventing one. | Applies to all research, case-law, and statute skills. |
| **Confidence score** | A machine-generated assessment of the model's certainty about a specific output, used to gate escalation to human review or to signal hedging. | Surfaced in outputs as "Confidence: high / medium / low" with basis stated. |
| **Escalation** | The behavior of routing a query or output to a human expert when confidence is low, stakes are high, or a domain falls outside the skill's scope. | Non-negotiable for jurisdiction-specific tax and regulatory opinions. |
| **Hallucination guard** | A runtime or post-processing check that detects likely fabrications — e.g., checking that a cited article number exists in the indexed statute text. | Part of the QA layer applied before output is shown to the user. |

---

## How to Use This Pack

- Reference this vocabulary when writing or reviewing skill frontmatter and documentation.
- When onboarding a legal professional to the platform, share this as a primer on AI terminology.
- When onboarding a developer, share the "Legal-AI Product Terms" section as a primer on domain concepts.
- When a skill body uses a term defined here, link to this pack via `[[ref-vocabulary]]`.

## Caveats & Currency

AI engineering terminology evolves rapidly. Terms like "agentic loop," "tool use," and "function calling" have been defined differently by different vendors at different times. Definitions here reflect practice as of early 2026. Verify vendor-specific documentation when implementing.

## Related skills

- [[router-intent-classifier]]
- [[report-hallucination-rate-tracker]]
- [[research-deep-research-orchestrator]]
- [[eval-output-quality]]
- [[ref-jurisdiction-index]]
