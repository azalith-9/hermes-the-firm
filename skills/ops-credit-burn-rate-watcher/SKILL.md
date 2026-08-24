---
name: ops-credit-burn-rate-watcher
description: Use when monitoring token and cost consumption per tenant, user, or matter across all connected LLM providers. Tracks burn rate trends, alerts when a tenant is projected to hit their plan limit within 7 days, flags abnormal per-turn costs driven by inefficient model selection or prompt bloat, and generates optimization suggestions — covering the agent, Gemini, GPT-4, and other providers.
license: MIT
metadata: " id: ops.credit-burn-rate-watcher category: ops jurisdictions: [__multi__] priority: P1 intent: [credits, ops, cost-monitoring, token-burn, optimization] related: [onboarding-upgrade-prompt-when-credits-low, ops-churn-risk-detector, ops-ad-budget-vs-bug-rate-circuit-breaker] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Registered as a flat plugin skill.
-->


# Ops — Credit Burn Rate Watcher

## Purpose

Token consumption is the primary cost driver in a legal AI product. Unchecked burn rates lead to two problems simultaneously: tenants unexpectedly exhausting their plan limits (bad user experience, churn signal) and the platform incurring costs above what the subscription covers (margin erosion). This skill monitors burn rate at multiple levels of granularity and produces actionable alerts and optimization suggestions.

## What it monitors

Monitoring operates at three levels:

### 1. Per-tenant level
- Total tokens consumed in the current billing period (by provider: the agent, Gemini, GPT-4, etc.)
- Total USD cost in the current billing period
- Rolling burn rate (tokens/day and $/day over last 7 days)
- Projected date of plan limit exhaustion at current burn rate
- Budget remaining as a percentage

### 2. Per-matter level
- Tokens per matter (aggregated across all sessions touching that matter)
- Cost per matter
- Matters with abnormal burn (defined as >3× the account's average cost-per-matter)

### 3. Per-turn level
- Tokens per turn (input + output)
- Cost per turn
- Model used for the turn
- Skill(s) invoked for the turn
- Whether the turn used a cached response (and what the cost saving was)

## Alert thresholds

| Alert | Trigger | Action |
|-------|---------|--------|
| Plan limit approaching | Projected to hit limit within 7 days at current rate | Email to account owner + flag in ops dashboard |
| Matter abnormal burn | Single matter consuming >3× account average cost-per-matter | Ops flag + CSM notification |
| Cost-per-turn drift | 7-day rolling avg cost-per-turn increases >30% vs prior 7 days | Engineering alert — likely prompt bloat or model selection regression |
| Deep-research multi-hop | Single turn consuming >$X (configurable) due to multi-step agentic research | Flag for review — may warrant model downgrade for routine queries |
| Provider cost spike | A specific provider's cost share increases >20% without a corresponding increase in usage | Check for provider pricing change or inadvertent model upgrade |

## Optimization suggestions

When a burn-rate alert fires, the watcher generates up to 3 ranked optimization suggestions:

### Model selection
> "Routine queries (drafting standard clauses, basic Q&A) are being routed to the agent Opus. Switching these to the agent Haiku or Gemini Flash could reduce costs by an estimated X% with minimal quality impact."

### Prompt caching
> "System prompt skill composition for tenant [X] is not using prompt caching. Enabling cache on the static portions of the system prompt could reduce input token costs by ~40% for this tenant."

### Prompt bloat
> "The average system prompt for this tenant grew from 2,400 to 6,200 tokens in the last 30 days. Identify and remove unused skills from the composition stack."

### Skill routing
> "X% of turns are being routed to expensive deep-research skills for queries that could be handled by the KB lookup skill. Review skill router thresholds."

## Output

The watcher produces three outputs:

1. **Ops dashboard view**: per-tenant burn rate table with trend indicators and alert flags.
2. **Ops alert**: triggered on any threshold breach; routed to the ops Slack channel `#credits-ops`.
3. **Customer-facing usage email**: sent to the account owner when projected exhaustion is ≤7 days. Uses plain language ("at your current pace, your plan credits will run out on [date]") and includes an upgrade CTA. Coordinated with [[onboarding-upgrade-prompt-when-credits-low]] to avoid double-alerting.

## Data retention

- Per-turn cost data is retained for 90 days for trend analysis.
- Per-matter aggregates are retained for the life of the matter plus 1 year.
- Aggregated billing totals are retained for 7 years for financial record-keeping.

## Related skills

- [[onboarding-upgrade-prompt-when-credits-low]] — the in-product prompt that fires for users approaching their limit
- [[ops-churn-risk-detector]] — burn exhaustion without upgrade is a churn signal; these two skills should share data
- [[ops-ad-budget-vs-bug-rate-circuit-breaker]] — related ops monitoring for spend decisions
