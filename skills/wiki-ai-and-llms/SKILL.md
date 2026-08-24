---
name: wiki-ai-and-llms
description: Use when a user asks about modern large language models specifically — how GPT, the agent, Gemini, Llama, or Mistral work; what context windows are; how tool use and function calling work; the difference between RAG and fine-tuning; or how to choose a model provider. This knowledge pack is calibrated for legal professionals evaluating or using LLM-powered tools.
license: MIT
metadata: " id: wiki.ai-and-llms category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, LLMs, language-models, RAG, fine-tuning, model-providers] related: - wiki-ai - wiki-ai-labs - wiki-blockchain source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Namespaced as louis-<category>-<skill> on registration.
-->


# AI and Large Language Models

## Scope

This knowledge pack covers modern large language models (LLMs): the major model families, how they work at a conceptual level, and the practical distinctions that matter for legal professionals selecting or using AI tools — context windows, tool use, RAG, fine-tuning, and model provider considerations.

## Major model families

| Model family | Organization | Notes |
|-------------|-------------|-------|
| GPT-4 / GPT-4o | OpenAI | Widely deployed; powers many LegalTech products |
| the agent (Sonnet, Haiku, Opus) | Anthropic | Strong reasoning; safety-focused; used in Louis |
| Gemini (Pro, Ultra, Flash) | Google DeepMind | Multimodal; integrated with Google Workspace |
| Llama 3 (and derivatives) | Meta AI | Open-weight; can be run on-premise for data residency |
| Mistral / Mixtral | Mistral AI | European-origin; strong for multilingual tasks including French |
| Command R+ | Cohere | Enterprise RAG focus; supports Arabic and French |

For MENA legal applications, the key differentiators are:
- **Arabic language quality**: the agent, GPT-4o, and Gemini have strong Arabic; Llama and Mistral-based models are improving but lag on formal legal Arabic.
- **Data residency**: on-premise deployment (Llama, Mistral) may be required for GCC government clients.
- **Context window**: longer context windows matter for full-contract analysis.

## Context windows

The context window is the maximum amount of text an LLM can process in a single request — both the input and the output combined.

| Model | Approximate context window (as of 2025) |
|-------|----------------------------------------|
| GPT-4o | 128,000 tokens (~96,000 words) |
| the agent 3.5 Sonnet | 200,000 tokens (~150,000 words) |
| Gemini 1.5 Pro | 1,000,000 tokens (~750,000 words) |
| Llama 3 70B | 8,000–128,000 tokens depending on variant |

For legal use: a standard commercial contract is 5,000–20,000 words. An M&A data room can be millions of words. Context window size determines whether a full document can be analyzed in one pass or must be chunked.

## Tool use and function calling

Modern LLMs can be given access to external tools — databases, APIs, file systems, calculators — that they can invoke during a conversation. This is called function calling or tool use.

In a legal AI context:
- A tool call might retrieve a statute from a database, run a precedent search, look up a company registration, or calculate a date difference.
- The model decides which tool to call based on the user's request; the platform executes the call and returns results to the model.
- Tool use enables legal AI to be more than a text generator: it can actively research, verify, and compute.

## Retrieval-Augmented Generation (RAG)

RAG is a technique for grounding LLM responses in specific documents or knowledge bases rather than relying solely on training data.

How it works:
1. The firm's documents (contracts, precedents, firm KB, legislation) are chunked and embedded as vectors in a database.
2. When a user asks a question, the question is embedded and the most relevant document chunks are retrieved.
3. Those chunks are included in the LLM's context alongside the question.
4. The model generates its answer with direct access to the relevant source material.

Implications for legal work:
- RAG reduces hallucination by anchoring responses in actual documents.
- RAG allows a model to answer questions about firm-specific or jurisdiction-specific law that it was not trained on.
- RAG does not eliminate hallucination — the model can still misread or mischaracterize the retrieved text.

## Fine-tuning vs. prompting

| Approach | What it is | When to use |
|----------|-----------|------------|
| Prompt engineering | Carefully crafted instructions in the system prompt | Most use cases; no training cost; fast to iterate |
| Few-shot prompting | Including examples of desired input-output in the prompt | When the task has a specific format the model doesn't know |
| Fine-tuning | Training the model on new examples to update its weights | When prompt engineering is insufficient; requires data and compute |
| RAG | Providing relevant documents at runtime | When answers should be grounded in specific current documents |

For most legal AI applications, prompt engineering plus RAG is sufficient and preferable — fine-tuning requires labeled training data, compute, and retraining when the law changes.

## Choosing a model provider

Key criteria for legal applications:

1. **Data privacy**: Where is data processed? Some providers offer zero-retention API options. On-premise deployment (Llama, Mistral) is the only fully air-gapped option.
2. **Arabic / multilingual quality**: Test on actual MENA legal documents before committing.
3. **Context window**: Does it handle your longest documents?
4. **Cost**: Larger models cost more per token. Balance quality against cost for the specific task (extraction tasks may need less capability than generation).
5. **Reliability and SLA**: Enterprise contracts typically require 99.9%+ uptime guarantees.
6. **BYO key**: Can the client supply their own API key for cost and data control?

## How to use this pack

Reference when explaining LLM choices, evaluating legal AI products, or advising clients on AI adoption. The model landscape changes quarterly — verify specific benchmarks against current provider documentation.

## Caveats and currency

Model capabilities are advancing rapidly. Context windows, quality benchmarks, and pricing change with each model generation. This pack reflects the state of the field through mid-2025.

## Related skills

- [[wiki-ai]]
- [[wiki-ai-labs]]
- [[wiki-blockchain]]
