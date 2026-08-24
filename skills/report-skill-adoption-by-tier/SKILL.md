---
name: report-skill-adoption-by-tier
description: Use when the product or growth team needs to understand which skills are used by which user tier (Free, Plus, Pro, Enterprise), in order to drive packaging decisions, tier upgrade incentives, and content investment prioritization. This is an internal analytics report. Trigger on the weekly or monthly product-analytics review cycle, or before a pricing or packaging change.
license: MIT
metadata: " id: report.skill-adoption-by-tier category: report jurisdictions: [__multi__] priority: P3 intent: [__internal__, product-analytics, skill-adoption, tier-packaging, growth] related: [report-weekly-ai-quality-trend, report-jurisdiction-coverage-matrix, report-competitor-output-comparison-weekly] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'report'.
Registered as a flat plugin skill.
-->


# Skill Adoption by Tier — Report

Internal product-analytics report tracking which skills each user tier (Free, Plus, Pro, Enterprise) actually uses, how often, and with what success. The primary output is a tier-packaging signal: which skills create tier-upgrade motivation, and which are underused in a tier that could leverage them more.

## Purpose

Tier packaging decisions without adoption data are guesses. This report answers:

1. **Which skills are primarily used by paid tiers?** These are the value drivers — protect them behind tier gates or use them as upgrade prompts.
2. **Which skills are used across all tiers?** These are either correct free-tier features or packaging leaks.
3. **Which high-value skills have low adoption in the tier that should use them most?** These are discoverability problems — fix with onboarding or in-product nudges.
4. **Are Enterprise users getting distinct value from specialized skills?** If not, enterprise packaging needs differentiation.

## Data inputs

| Signal | Source | Notes |
|--------|--------|-------|
| Skill invocation events | Product analytics (PostHog / Mixpanel) | Tagged with `skill_id`, `user_id`, `tier`, `timestamp` |
| User tier | Auth / billing database | Free / Plus / Pro / Enterprise |
| Session outcome | Satisfaction score, explicit feedback, task completion | Proxy for whether the skill delivered value |
| Skill depth invoked | Single-turn vs multi-turn agent workflows | Deep-research workflows signal high-engagement users |

## Metrics

For each skill × tier combination, compute:

| Metric | Definition |
|--------|-----------|
| **Unique users** | Count of distinct users in the tier who invoked the skill in the reporting period |
| **Total invocations** | Total calls, including re-runs and follow-up turns |
| **Adoption rate** | Unique users / total users in tier |
| **Satisfaction rate** | % of invocations that received positive feedback (thumbs up, 4-5 star, or no negative signal) |
| **Upgrade conversion** | For Free-tier users: % who upgraded within 7 days of invoking the skill |
| **Avg invocations per active user** | Depth of engagement among those who use the skill |

## Output format

### Tier usage summary table

For each tier (column) and each skill (row):

| Skill | Free | Plus | Pro | Enterprise | Tier concentration |
|-------|------|------|-----|------------|--------------------|
| research-statute-lookup | 12% | 28% | 42% | 18% | Pro-heavy |
| draft-nda-unilateral | 5% | 22% | 54% | 19% | Pro-heavy |
| research-deep-research-orchestrator | 1% | 8% | 35% | 56% | Enterprise-heavy |
| review-contract-redline | 8% | 30% | 48% | 14% | Pro-heavy |
| … | … | … | … | … | … |

**Tier concentration** classification:
- **Free-heavy** (> 40% of invocations from Free): potential packaging leak or correct free feature
- **Plus-heavy**: good Plus value driver
- **Pro-heavy**: core Pro value driver; protect or use as upgrade prompt
- **Enterprise-heavy**: strong Enterprise differentiator

### Top skills by upgrade conversion (Free → Paid)

| Skill | Free adoption | Upgrade rate within 7 days |
|-------|---------------|---------------------------|
| research-deep-research-orchestrator | 2% | 18% |
| review-contract-redline | 9% | 12% |
| … | … | … |

These are the skills to emphasize in Free-tier onboarding to drive upgrade intent.

### Underutilized high-value skills

Skills that are available to a tier but adopted by < 10% of that tier's users, where the skill is a core value proposition:

| Skill | Tier | Adoption | Hypothesis | Recommendation |
|-------|------|----------|-----------|----------------|
| research-jurisdiction-comparison | Pro | 6% | Not discoverable in UI | Add to Pro onboarding tour |
| … | … | … | … | … |

### Enterprise-specific skill usage

Which skills are Enterprise-only or disproportionately used by Enterprise:
- Multi-jurisdiction workflows
- Deep research orchestrator
- Compliance gap analysis (multi-framework)
- Cap table sanity (VC/M&A use case)

If Enterprise users are NOT using these, that is a customer-success problem, not a packaging problem.

## Packaging recommendations

Rules derived from the data:

1. **Upgrade-gate skills** where Free adoption is > 20% but upgrade conversion is high: move behind a paywall with a clear "upgrade to unlock" prompt.
2. **Highlight in Plus/Pro marketing** any skill with satisfaction rate > 85% in that tier.
3. **Invest in discoverability** for skills with adoption < 10% in the tier that should use them most, if satisfaction rate > 80% among users who do invoke them (hidden gem).
4. **Retire or redesign** any skill with adoption < 2% across all tiers and no growth trend over 90 days.

## Cadence

- **Weekly**: top-10 skill invocations by tier (lightweight pulse)
- **Monthly**: full matrix + packaging recommendations
- **Quarterly**: deep-dive with cohort analysis (new users vs retained users per tier)

## Related skills

- [[report-weekly-ai-quality-trend]]
- [[report-jurisdiction-coverage-matrix]]
- [[report-competitor-output-comparison-weekly]]
- [[report-hallucination-rate-tracker]]
