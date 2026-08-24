---
name: eng-feature-flag-rollout-skills
description: Use when managing the rollout of new or updated legal AI skills using feature flags — controlling which organizations, users, or tenant tiers have access to a skill, enabling gradual rollout, A/B testing skill versions, and instant kill-switches for problematic skills. Engineering skill critical for safe deployment of legal AI capabilities without firm-wide disruption.
license: MIT
metadata: " id: eng.feature-flag-rollout-skills category: eng jurisdictions: [__multi__] priority: P2 intent: [feature-flags, rollout, A/B-test, gradual-release, kill-switch] related: - eng-fallback-model-cascade - eng-langfuse-eval-runner - eng-audit-log-schema - eng-latency-slo-by-skill source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Feature Flag Rollout — Skills

## What it does

Feature flags for skills control which skills are available to which users, at which versions, under what conditions. In a legal AI product, skills are the primary feature surface — a new skill for drafting a Saudi employment contract, an updated conflict-check algorithm, or an experimental WIP report format. Feature flags allow:

1. **Safe rollout**: ship a new skill to 5% of users before all users.
2. **Org-scoped enablement**: a skill that requires firm-specific configuration (e.g., billing-system integration) can be enabled only for that firm.
3. **Version A/B testing**: run two skill versions in parallel; evaluate quality via [[eng-langfuse-eval-runner]] before full promotion.
4. **Instant kill-switch**: if a skill produces harmful or inaccurate legal output in production, disable it for all users in under 60 seconds.
5. **Tier-gated access**: reserve advanced skills for pro/enterprise tier users.

## Flag schema

Each skill flag is an entry in the flag configuration store:

```json
{
  "flag_id": "skill:efirm-conflict-check",
  "skill_id": "efirm-conflict-check",
  "skill_version": "1.1",
  "enabled_global": true,
  "rollout_percentage": 100,
  "overrides": [
    {
      "condition": "org_id == 'org_haqq'",
      "skill_version": "1.2-beta",
      "rollout_percentage": 100,
      "note": "HAQQ is piloting v1.2-beta"
    },
    {
      "condition": "user_tier == 'free'",
      "enabled": false,
      "note": "Conflict check not available on free tier"
    }
  ],
  "kill_switch": false,
  "created_at": "ISO-8601",
  "updated_at": "ISO-8601",
  "owner": "eng-team | product-team",
  "review_date": "ISO-8601"
}
```

## Evaluation logic

For every incoming request, the skill router evaluates flags in order:

```
1. If kill_switch == true: skill unavailable → return graceful error
2. If org_id matches an override: apply override (version + rollout%)
3. If user_tier matches an override: apply override
4. Else: apply global rollout_percentage (hash(user_id + flag_id) % 100 < rollout_percentage)
5. If skill available: load skill_version
```

Hash-based rollout ensures stability — the same user always gets the same variant within a rollout, avoiding inconsistent experiences across sessions.

## Rollout stages for a new skill

| Stage | Rollout % | Duration | Promotion criteria |
|---|---|---|---|
| Internal only | 0% global; 100% for eng/product org_ids | 1 week | No errors; latency within SLO |
| Alpha | 5% of consenting opt-in users | 1 week | Quality score ≥ target per Langfuse eval |
| Beta | 20% | 1–2 weeks | Feedback positive; no critical flags |
| GA | 100% | Permanent | — |

For P0 skills (conflict check, engagement letter), the rollout stages are mandatory and cannot be skipped. For P2 skills, a single internal-only → GA progression is acceptable if quality is confirmed.

## Version-parallel A/B testing

To compare two skill versions:

```json
{
  "flag_id": "skill:efirm-engagement-letter-draft",
  "experiment": {
    "enabled": true,
    "variant_a": {"skill_version": "1.0", "traffic_pct": 50},
    "variant_b": {"skill_version": "1.1-test", "traffic_pct": 50},
    "eval_metric": "langfuse_score:quality",
    "min_samples": 100,
    "auto_promote_threshold": 0.05
  }
}
```

Route users stably (same variant across sessions) using `hash(user_id + experiment_id) % 100`.

Evaluate using [[eng-langfuse-eval-runner]]: if variant B shows a statistically significant improvement (p < 0.05) after 100+ samples, auto-promote to 100% or alert the product team for manual promotion.

## Kill-switch procedure

When a skill must be immediately disabled:

1. Set `kill_switch: true` in the flag store (change propagates in < 10s with a cache-busting mechanism).
2. All in-flight requests complete (no mid-stream interruption).
3. New requests for that skill receive:
   ```
   "This feature is temporarily unavailable. Please try again later or contact support."
   ```
4. Incident is logged with: who triggered the kill-switch, timestamp, reason.
5. Engineering investigates root cause.
6. To re-enable: set `kill_switch: false` after fix is deployed and verified.

**Never** roll back a kill-switch without a fix — the reason it was triggered still applies.

## Tier-gated skills

Map skill IDs to minimum tiers in configuration:

```json
{
  "efirm-conflict-check":          "pro",
  "efirm-engagement-letter-draft": "pro",
  "efirm-fee-quote-builder":       "pro",
  "efirm-client-update-email-draft": "basic",
  "efirm-deadline-tracker":        "basic"
}
```

When a free-tier user attempts to invoke a pro-skill, the router returns a paywall response with an upgrade CTA — not an error.

## Audit trail

All flag changes (create, update, kill_switch toggle) are recorded in the audit log ([[eng-audit-log-schema]]) with:
- Admin user ID who made the change
- Before and after state
- Timestamp
- Reason (free text)

Flag changes to P0 skills require a second admin approval before taking effect.

## Related skills

- [[eng-fallback-model-cascade]]
- [[eng-langfuse-eval-runner]]
- [[eng-audit-log-schema]]
- [[eng-latency-slo-by-skill]]
