---
name: onboarding-upgrade-prompt-when-credits-low
description: Use when a user is approaching or has hit their credit/token limit, attempts a tier-restricted feature, or shows a high-burn usage pattern. Governs the exact timing, copy, and frequency rules for surfacing upgrade prompts inside a legal AI chat product — including hard rules about deferral during emotionally sensitive conversations and mid-task interruptions.
license: MIT
metadata: " id: onboarding.upgrade-prompt-when-credits-low category: onboarding priority: P0 intent: [upgrade, credits, upsell, onboarding, tier-restriction] related: [unlock-contextual-upsell, onboarding-first-session-checklist, ops-credit-burn-rate-watcher, ops-churn-risk-detector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'onboarding'.
Registered as a flat plugin skill.
-->


# Onboarding — Upgrade Prompt When Credits Low

## When this applies

This skill governs every in-product moment where the system needs to surface an upgrade or plan-expansion prompt. It activates on three distinct triggers:

1. **Credit depletion threshold** — the user has consumed ≥ 80% of their monthly token/credit allowance (i.e., fewer than 20% of credits remain).
2. **Tier-restricted feature block** — the user attempts to invoke a feature that requires a higher plan (e.g., Deep Research, multi-jurisdiction analysis, bulk drafting, document workspace beyond the free limit).
3. **Heavy-use day** — intraday usage is ≥ 3× the user's own rolling daily average, signalling an imminent exhaustion event even if the monthly counter has not yet triggered.

## Behavior

### Credit-low prompt

When the 80% threshold is reached, surface a non-blocking, dismissable prompt at the next natural break (after the assistant has finished delivering a response — never mid-generation):

> You've used 80% of your monthly credits. Upgrade to Pro for 50,000 more credits, or wait until your next reset on [date].
>
> [**Upgrade now**]  [Remind me in 7 days]  [Don't show again this cycle]

- "Upgrade now" → deep-link to the billing/plan page with the correct plan pre-selected.
- "Remind me in 7 days" → suppresses the prompt for 7 days unless the user hits 95%.
- "Don't show again this cycle" → suppresses until the monthly reset (and never again for this cycle).

At **95% depletion**, re-surface regardless of the 7-day suppression — the user may be about to lose access mid-matter, which is a real harm.

### Tier-restricted feature prompt

When the user attempts a feature outside their tier, replace the blocked action with:

> **[Feature name]** is available on Pro and above. You can:
>
> [**See plans →**]  [**Try once for X credits**]  [Go back]

- "Try once for X credits" is only shown if the user has sufficient credits remaining — never show it if credits would go negative.
- Do not expose the underlying technical reason for the block (e.g., don't say "feature flag disabled for free tier").

### Heavy-use day prompt

When intraday burn hits 3× the daily average, surface a soft heads-up — not an upgrade push:

> You're using Louis heavily today. At this pace, your credits may run out before your [date] reset. Upgrade to avoid interruptions.
>
> [**Upgrade**]  [Dismiss]

## Timing rules

| Rule | Details |
|------|---------|
| Not during distress | If the conversation signals emotional weight (grief, crisis, urgent matter, high-stakes client situation), defer all upgrade prompts by 24 hours. |
| Not mid-task | Only surface after the assistant has delivered a complete response — never interrupt a streaming reply. |
| Frequency cap | At most one upgrade prompt per 24-hour window per user. Multiple triggers on the same day queue to the next break, they do not stack. |
| Dismissal respected | "Don't show again" is honoured until the next billing cycle reset. Suppression state is stored server-side, not only in the browser. |
| Post-success timing | Ideal placement is immediately after a high-value output (a completed draft, a research summary). The user has just experienced value — the upsell has more credibility here. |

## Copy principles

- **Show real value first.** The prompt appears after the user has already received something useful. Reference that: "You've drafted 12 contracts this month — keep the momentum going."
- **Be specific about what they get.** "50,000 more credits" is better than "more credits". "Unlimited document workspace" is better than "more features".
- **One primary action.** Every prompt has a single prominent CTA. Secondary options (Remind me later, Dismiss) are clearly secondary in the visual hierarchy.
- **No manufactured urgency.** Do not use countdown timers or "limited time" language unless it is factually true.

## Edge cases

- **Trial-tier users**: surface the prompt at 60% (not 80%) because trials often have lower absolute credit ceilings.
- **Enterprise accounts**: suppress all credit prompts — billing is handled outside the product. Show usage dashboards instead via the admin panel.
- **BYO-key users** (bring-your-own API key): suppress the credit-based prompts entirely. Show a warning only if their configured API key returns quota errors from the upstream provider.
- **Concurrent sessions**: token consumption is aggregated at the user/tenant level, not per session. Ensure the credit counter reflects the true aggregate.

## Do not

- Do not push upgrade prompts inside emotionally sensitive legal contexts (divorce proceedings, criminal matters, bereavement estate work).
- Do not use guilt framing ("You're about to lose everything you've built…").
- Do not surface upgrade prompts more than once per 24 hours.
- Do not block a user mid-generation — always let the current response complete.
- Do not fabricate credit figures or reset dates — pull live values from the billing service.

## Related skills

- [[unlock-contextual-upsell]] — for upselling within the flow of substantive legal work
- [[onboarding-first-session-checklist]] — the broader onboarding sequence this fits into
- [[ops-credit-burn-rate-watcher]] — the backend monitor that feeds the trigger signals
- [[ops-churn-risk-detector]] — detects when heavy usage coupled with upgrade refusal signals churn risk
