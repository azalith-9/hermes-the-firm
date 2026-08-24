---
name: wiki-ai
description: Use when a user asks foundational questions about artificial intelligence as a field — its history, core paradigms, major techniques (supervised learning, reinforcement learning, neural networks, transformers), alignment challenges, the emergence of agents, or multimodal systems. This knowledge pack provides a structured reference for legal professionals and legal AI users who need to understand the technology underlying the tools they use.
license: MIT
metadata: " id: wiki.ai category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, artificial-intelligence, foundations, technology] related: - wiki-ai-and-llms - wiki-ai-labs - wiki-blockchain source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Artificial Intelligence — Foundations

## Scope

This knowledge pack covers the foundational concepts of artificial intelligence as a field, with enough depth for legal professionals to understand the technology they are using or evaluating — without requiring a computer science background. It is not a technical implementation guide; it is a conceptual reference.

## Historical arc

AI as a formal discipline began at the Dartmouth Conference in 1956. The field has gone through several cycles of enthusiasm and funding withdrawal ("AI winters") before arriving at the current era of deep learning.

Key transitions:
- **1950s–1980s**: Rule-based systems and symbolic AI. Expert systems encode human knowledge as if-then rules. Effective in narrow domains; brittle in the real world.
- **1980s–2000s**: Statistical machine learning. Systems learn patterns from data rather than following hand-coded rules. Support vector machines, decision trees, Bayesian classifiers.
- **2010s**: Deep learning revolution. Large neural networks trained on large datasets outperform previous methods on vision, speech, and text tasks. Enabled by GPU computing and large training datasets.
- **2017**: Transformer architecture (Attention is All You Need) becomes the dominant approach for language tasks.
- **2020s**: Large language models (LLMs) demonstrate emergent capabilities. AI enters mainstream use in legal, medical, financial, and creative domains.

## Core concepts

### Neural networks
Inspired loosely by biological neurons, a neural network is a mathematical function that maps input (text, image, audio) to output (classification, generation, prediction) through layers of weighted transformations. The weights are learned from training data.

### Supervised learning
Learning from labeled examples: the system is shown many input-output pairs (e.g., contract text → risk level) and learns to generalize to new examples. Requires labeled training data, which is expensive to produce in legal domains.

### Unsupervised learning
Learning structure from unlabeled data. Clustering, dimensionality reduction, anomaly detection. Used in legal e-discovery for document clustering.

### Reinforcement learning from human feedback (RLHF)
A technique for aligning model behavior with human preferences. After initial training, human evaluators rate model outputs; these ratings train a reward model; the language model is then fine-tuned to maximize reward. Most modern LLMs use RLHF or a variant.

### Transformer architecture
The architectural foundation of all current large language models. Key innovation: the attention mechanism, which allows the model to consider all parts of an input simultaneously rather than processing it sequentially. Enables learning long-range dependencies in text.

### Alignment
The challenge of ensuring AI systems do what their operators and users intend — and do not cause unintended harm. Active research area. Includes: value alignment (matching human values), safety (preventing dangerous outputs), interpretability (understanding why a model produces its outputs).

### Agents
AI systems that can take sequences of actions in the world — calling tools, browsing the web, writing and executing code, managing files — in pursuit of a goal, rather than simply responding to a single input. Legal AI applications increasingly use agent architectures for multi-step research and document workflows.

### Multimodal AI
Systems that operate across multiple input types: text, images, audio, video. A multimodal legal AI can read a scanned contract (image), transcribe a client call (audio), and draft a document (text) in an integrated pipeline.

## Relevance to legal professionals

Legal professionals using AI tools should understand:

1. **AI does not reason like a lawyer.** It identifies patterns in training data. Hallucination (confident generation of false information) is a real risk — always verify citations and statute references.
2. **Training data determines capability.** A model trained primarily on US or UK legal text will perform poorly on MENA law. Jurisdiction-native training or fine-tuning matters.
3. **Alignment is ongoing work.** RLHF and similar techniques reduce harmful outputs but do not eliminate them. AI legal tools require human review for consequential decisions.
4. **Agents introduce new risks.** An AI that can take actions (file documents, send emails, query databases) has a larger blast radius when it errs. Least-privilege and human-in-the-loop checkpoints are essential.

## How to use this pack

Use as background context when explaining AI concepts to clients, evaluating AI legal products, or understanding the technical limitations of AI-assisted legal work.

## Caveats and currency

The AI field moves rapidly. Model capabilities, safety techniques, and regulatory frameworks are changing faster than any static knowledge pack can track. Verify specific technical claims against current sources before citing them in professional contexts.

## Related skills

- [[wiki-ai-and-llms]]
- [[wiki-ai-labs]]
- [[wiki-blockchain]]
