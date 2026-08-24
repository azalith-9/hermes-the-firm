---
name: pillar-architectural-bet-no-fine-tuning
description: Internal architectural principle establishing that Louis uses frontier foundation models plus a structured skill library and retrieval augmentation — not fine-tuned models — to deliver legal AI quality. Use when reasoning about skill design, model selection, quality assurance, or why capabilities are built as skills rather than trained weights.
license: MIT
metadata: " id: pillar.architectural-bet-no-fine-tuning category: pillar jurisdictions: [__multi__] priority: P3 intent: [__internal__] related: [pillar-legal-skills-authoring, pillar-live-data-mcp, pillar-context-across-apps, pillar-document-comprehension-structural, eng-architectural-bet-no-fine-tuning] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'pillar'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Architectural Pillar: No Fine-Tuning

## Scope

This pillar defines a foundational architectural bet: Louis does **not** fine-tune frontier language models to encode legal knowledge. All legal expertise is surfaced through the **skill library + retrieval augmentation + prompt engineering** layer, applied at inference time to a state-of-the-art foundation model.

This decision affects every aspect of system design — how skills are authored, how knowledge is updated, how quality is controlled, and how the system scales to new jurisdictions and practice areas.

---

## The bet

> Use frontier models + skill library + retrieval. Do not fine-tune.

The implementation is described in [[eng-architectural-bet-no-fine-tuning]]. This pillar captures the *why* so it can inform architectural decisions throughout the codebase and skill set.

---

## Why not fine-tune

### 1. Legal knowledge goes stale fast
Law changes constantly — new statutes, new regulations, new case law, new regulatory guidance. Fine-tuned models freeze knowledge at a point in time. When the UAE Personal Data Protection Law is amended, a fine-tuned model must be retrained. A skill with retrieval can be updated in minutes.

### 2. Fine-tuning is opaque
A fine-tuned model cannot explain *why* it knows what it knows. In legal AI, auditability is essential: a lawyer needs to be able to verify the source of any claim. Skills are explicit, versionable markdown files that a practitioner can inspect. Fine-tuned weights are not.

### 3. Frontier models improve continuously
Using a fine-tuned model means forgoing capability improvements in the foundation model. Skills built on top of frontier models automatically benefit when the underlying model improves. There is no re-training cost.

### 4. Jurisdiction and practice area breadth
MENA legal AI must cover Lebanese civil law, UAE federal law, DIFC/ADGM common law, Saudi law, Egyptian law, French law, OHADA, and more — often in the same matter. Fine-tuning one model to cover this breadth is impractical. A skill-per-domain architecture scales gracefully: add a jurisdiction by authoring skills, not by retraining.

### 5. Quality control is tractable with skills, not with weights
A skill can be reviewed by a subject-matter lawyer, version-controlled, and rolled back if wrong. A fine-tuned model is a black box. Skills enable a "legal QA" workflow that fine-tuning does not.

---

## What the architecture uses instead

| Need | Solution |
|------|---------|
| Domain knowledge | SKILL.md files in the skill library |
| Current information | Live data via MCP connectors (see [[pillar-live-data-mcp]]) |
| Document context | Structural document ingestion (see [[pillar-document-comprehension-structural]]) |
| User/matter context | Cross-surface context store (see [[pillar-context-across-apps]]) |
| Routing | Semantic router + skill intent matching |
| Citation accuracy | Confidence scorer + retrieval from authoritative sources |

---

## Implications for skill authoring

Because skills are the primary vehicle for legal expertise, skill quality is the system quality. This has direct implications:

- **Skills must be precise**: a vague skill produces vague outputs even on a top-tier model
- **Skills are versioned and reviewable**: every change should be diffable; lawyers can audit changes
- **Skills encode the expert's reasoning, not just facts**: the goal is to give the model the expert's mental process, not just a list of rules
- **Skills can be swapped**: if a better formulation exists, replace the skill file — no retraining required
- **Skills degrade gracefully**: a missing skill produces a gap, not a hallucination; the router can flag "no skill for this topic" rather than confabulating

See [[pillar-legal-skills-authoring]] for the skill authoring standard.

---

## Trade-offs and known limits

This bet is not without costs:

- **Inference cost**: a rich system prompt (many skills loaded) is more expensive per call than a fine-tuned model with knowledge baked in. Mitigation: selective skill loading by router; skill compression.
- **Latency**: retrieval adds a round-trip. Mitigation: pre-load high-frequency skills; cache retrieval results.
- **Coverage gaps**: if no skill exists for a topic, quality degrades. Mitigation: the skill library must grow with demand; the router must flag coverage gaps rather than hallucinate.
- **Foundation model dependency**: vendor model changes can affect behavior. Mitigation: integration tests on representative legal prompts; model-version pinning in production.

---

## How to use this pillar

When designing a new feature, integration, or skill set:

1. **Ask if a skill can carry this knowledge.** If yes, write a skill — do not request fine-tuning.
2. **Ask if live data is needed.** If yes, add a retrieval connector — do not embed stale facts.
3. **Ask if the frontier model already handles this well.** If yes, write a lightweight routing skill — do not over-engineer.
4. **Ask if you are trying to change the model's behavior.** If yes, write a persona or heuristic skill — do not seek fine-tuning.

The only legitimate fine-tuning use case would be a heavily specialized output format (e.g., a specific court's procedural formatting) that cannot be achieved through prompting. This has not arisen to date.

---

## Caveats and currency

This pillar reflects the architectural state as of the system's initial design. As foundation model capabilities evolve (longer contexts, better instruction-following, tool use), some retrieval and skill-loading patterns may be superseded. Review this pillar annually against the current foundation model landscape.

---

## Related skills

- [[eng-architectural-bet-no-fine-tuning]] — engineering implementation of this pillar
- [[pillar-legal-skills-authoring]] — skill authoring standards that make this bet work
- [[pillar-live-data-mcp]] — live data connectors as the alternative to stale trained knowledge
- [[pillar-context-across-apps]] — cross-surface context as a skills-layer concern
- [[pillar-document-comprehension-structural]] — document understanding without fine-tuning
