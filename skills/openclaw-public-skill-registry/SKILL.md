---
name: openclaw-public-skill-registry
description: Use when discovering, searching, or referencing the OpenClaw public registry of community-authored and lawyer-verified legal AI skills. The registry provides versioned, quality-tiered skills covering MENA and global jurisdictions, seeded by HAQQ and extended by community contributors. Applicable whenever a user or system needs to discover what skills exist, verify a skill's provenance, or assess its quality tier before deployment.
license: MIT
metadata: " id: openclaw.public-skill-registry category: openclaw priority: P2 intent: [openclaw, registry, skill-discovery, community, legal-ai] related: [openclaw-contrib-template, openclaw-eval-harness-shared, openclaw-skill-portability-claude-codex-gemini] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'openclaw'.
Registered as a flat plugin skill.
-->


# OpenClaw — Public Skill Registry

## Scope

The OpenClaw Public Skill Registry is the open, versioned, lawyer-reviewed catalogue of legal AI skills for the `mini-hermes-the-firm` ecosystem. It is the authoritative source for:

- **Discovering** what skills exist across practice areas and jurisdictions
- **Assessing** skill quality before integrating into a product or workflow
- **Attributing** authorship to the lawyers and developers who contributed each skill
- **Tracking** versions and changes over time

The registry is free to use. Attribution to authors is required under CC-BY-SA 4.0.

## Registry structure

Skills are organized into a two-level hierarchy:

```
skills/
  <category>/
    <skill-id>/
      SKILL.md          ← the enriched skill file
      CHANGELOG.md      ← optional; for skills with multiple versions
      examples/         ← optional; input/output samples
```

Categories currently in the registry:

| Category | Description |
|----------|-------------|
| `draft` | Document drafting skills (contracts, letters, motions) |
| `review` | Contract and document review / risk analysis |
| `kb` | Legal knowledge bases (statutes, frameworks, thresholds) |
| `research` | Regulatory lookup, comparative analysis |
| `conversation` | Behavioral and safety guardrails |
| `router` | Request routing and orchestration |
| `connector` | Tool and integration connectors |
| `ops` | Product operations and analytics |
| `onboarding` | User onboarding and activation |
| `output` | Formatting and output style standards |
| `openclaw` | Registry meta-skills (this file is one of them) |

## Quality tiers

Every skill in the registry carries a quality-tier marker in its frontmatter (`priority` field):

| Tier | Meaning |
|------|---------|
| **P0** | Core, production-ready. Lawyer-reviewed, eval-tested, actively maintained. |
| **P1** | Production-ready. Lawyer-reviewed; may not have full eval coverage. |
| **P2** | Community-contributed. Reviewed but narrower scope or less-tested. |
| **P3** | Experimental. Not yet reviewed; do not use in production without validation. |

## Authorship and attribution

Each skill's `source` field records the original author (name, GitHub handle, or organization) and any external source link. The registry also maintains a `AUTHORS.md` at the repository root listing every contributor with the skills they authored.

Attribution is required when:
- Republishing a skill in a product or document
- Deriving a new skill from an existing one
- Citing a skill's content in a benchmark or publication

HAQQ contributes the seed library — approximately 200 skills covering MENA jurisdictions, core contract types, and the ops/tooling layer. These are labelled `source: Louis — HAQQ Legal AI` and are maintained by the HAQQ team.

## Searching the registry

### By practice area
```
skills/draft/         ← all drafting skills
skills/kb/            ← all knowledge bases
```

### By jurisdiction
Skills include a `jurisdictions` frontmatter field. To find all UAE skills:
```bash
grep -r "UAE" skills/*/*/SKILL.md
```

### By intent keyword
```bash
grep -r "non-compete" skills/*/*/SKILL.md
```

### Via the registry index
A machine-readable `registry.json` at the repository root indexes all skills with their metadata for programmatic discovery.

## Versioning policy

- Skills are versioned with a quoted string in frontmatter (`version: "1.0"`).
- Patches (typo, minor wording) increment to `"1.0.1"`.
- New sections or additional jurisdictions increment to `"1.1"`.
- Breaking rewrites of core guidance increment to `"2.0"`.
- Deprecated skills are not deleted; they receive a `deprecated: true` flag and a `superseded_by` pointer.

## Industry adoption goal

The registry aims to become the canonical community resource for legal AI skills — equivalent to what npm is for JavaScript packages or HuggingFace is for ML models, but scoped to legal AI skill definitions. Third-party products that embed OpenClaw skills are encouraged to display the quality tier and attribution information to their end users.

## Caveats

- Skills in the registry are practitioner-grade tools, not legal advice. Users are responsible for verifying current law in their jurisdiction before relying on any skill's output.
- Jurisdiction coverage is uneven. MENA (especially UAE, KSA, Lebanon) is the most thoroughly covered; other jurisdictions rely more heavily on community contributions.
- Law changes. Check the `version` date and verify against primary sources for time-sensitive matters.

## Related skills

- [[openclaw-contrib-template]] — how to contribute a new skill to the registry
- [[openclaw-eval-harness-shared]] — how skill quality is benchmarked
- [[openclaw-skill-portability-claude-codex-gemini]] — adapting registry skills across AI providers
