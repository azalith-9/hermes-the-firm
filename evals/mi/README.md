# Evals — Skill Regression Tests (Michigan)

Ported into hermes-the-firm from codearranger/claude-legal (MIT), plugin
`us-mi-legal-corpus`, `evals/`. These are prompt-based regression tests for
the Michigan skills that now live under `skills/mi-*`. Provenance noted for
the firm's third-party-notices accounting.

This folder contains prompt-based regression tests for each
skill in the `us-mi-legal-corpus` plugin.

> **TODO**: Author evals across the five categories
> (drafting, formatting, procedural, subject-matter,
> integration). Aim for at least 20 evals across the five
> categories.

## Folder layout

- `procedural/` — matter-neutral civil-procedure evals
- `drafting/` — drafting-skill evals
- `formatting/` — format and local-rule evals
- `subject-matter/` — subject bundle evals
- `integration/` — end-to-end multi-skill evals
