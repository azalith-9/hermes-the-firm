---
name: unlock-contextual-upsell
description: Use when a user on a free or lower tier encounters a capability that requires an upgrade — deep research, higher query limits, eFirm features, Word plugin, or business-plan features. Surfaces a specific, value-led upgrade prompt tied to the exact feature the user just attempted. Governs timing, frequency, and copy so that upgrade prompts feel helpful rather than intrusive. Calibrated against the user's demonstrated value (high-value session = stronger prompt) and emotional state (distress = no prompt).
license: MIT
metadata: " id: unlock.contextual-upsell category: unlock priority: P0 intent: [upsell, upgrade-prompt, conversion, tier-gating] related: [unlock-case-study-relevant-to-user, unlock-empty-state-suggestions, unlock-cross-product-bridge] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'unlock'.
Registered as a flat plugin skill.
-->


# Unlock — Contextual Upsell

## When this applies

This skill governs all upgrade prompts shown to users who encounter a capability gate — a feature, limit, or workflow that requires a higher plan. It fires when:

- **Free tier hits feature gates**:
  - Deep research mode (multi-step legal research) → "Available on Pro"
  - More than X queries/day → "Upgrade for higher limits"
  - eFirm features (firm KB, matter management, RAG over firm documents) → "Available on Business plan"
  - Word plugin → "Pro+ feature"
  - Advanced drafting (multi-clause SPA, complex commercial) → "Pro recommended"
- **Starter plan approaching credit limit** — warn at 80% and 95% usage
- **Pro plan hitting business-feature usage** — e.g., attempting multi-user matter isolation

## Behavior

### Standard pattern
When the gate is hit, show exactly this pattern — no improvisation:

```
[Feature you wanted] is available on [Plan].
Get [X specific benefit] for $[Y]/mo.
[Upgrade →]   [See all plans]   [Maybe later]
```

The feature name must match **exactly what the user just tried**. Generic "upgrade for more features" is ineffective and feels disconnected.

### Prompt construction rules

**1. Name the specific blocked feature**
- Wrong: "Upgrade for more capabilities."
- Right: "Deep research mode — multi-step legal research across Westlaw and Lexis — is available on Pro."

**2. Lead with the benefit, not the price**
- Wrong: "Pro plan is $79/mo."
- Right: "Get unlimited queries and deep research for $79/mo."

**3. Show real ROI where possible**
- "Pro users draft NDAs 3× faster with the firm KB integration."
- "Average Pro user saves 5 hours/week vs drafting manually."
- Match the ROI claim to the specific feature that was blocked.

**4. One clear call to action**
- Primary CTA: "Upgrade →" (direct link to checkout for the recommended plan)
- Secondary: "See all plans" (comparison page)
- Dismiss: "Maybe later" (session-level suppress; respect immediately)

## Calibration rules — critical

### When NOT to push an upgrade prompt:

| Condition | Action |
|---|---|
| User is in distress (see [[conversation-empathy-b2c]]) | Suppress prompt entirely; address the issue first |
| Less than 10 minutes since signup | Suppress; give value first |
| User already hit "Maybe later" this session | Suppress for the remainder of the session |
| User has seen 3+ prompts in the last 7 days | Suppress; frequency capping applies |
| User is in the middle of a critical task (signing deadline) | Complete the task first; prompt after |

### When to push HARDER:

| Condition | Behavior |
|---|---|
| User just completed a high-value task (drafted 12-page MSA) | Higher-intensity prompt: name the specific time saved |
| User hit the same gate 3+ times in one session | Increase urgency: "You've hit this limit 3 times today." |
| User's heavy usage day | Prompt at end of session with daily summary of value created |
| User is actively browsing pricing page | Trigger in-session prompt via chat |

### Conversion triggers (where to place extra effort)
1. **Post-high-value-task prompt** — immediately after the user finishes a complex task where they can feel the value delivered
2. **Repeated gate hit** — 3+ gate hits in one session means the user is actively trying to use features beyond their tier
3. **Heavy usage day** — many queries, multiple documents processed = intrinsic motivation exists

## A/B testing parameters

The following elements should be A/B tested per cohort:

| Element | Variants |
|---|---|
| Copy intensity | Value-led ("save 5h/week") vs feature-led ("unlimited queries") |
| Discount offer | No discount / 20% off first month / "Try Pro free 14 days" |
| CTA label | "Upgrade now" vs "Start free trial" vs "Get Pro" |
| ROI framing | Hours saved / drafts completed / queries available |
| Timing | Immediately on gate hit / after task completes / at session end |

Track per variant: click-through rate, conversion rate, churn within 30 days post-upgrade.

## Plan tier mapping

| Tier | Key limit | Upgrade target |
|---|---|---|
| Free | 5 queries/day; no firm KB; no deep research | Starter or Pro |
| Starter | 30 queries/day; limited document length; no eFirm | Pro |
| Pro | Unlimited queries; firm KB; deep research; Word plugin | Business |
| Business | All Pro + eFirm; multi-user; matter management | Enterprise |
| Enterprise | Custom; white-label; API access | N/A |

When showing the upgrade target, skip tiers where possible — free user should be prompted to Pro, not to Starter, unless the Starter plan genuinely meets their use case at a significantly lower price point.

## Localization for MENA

- Prices should display in USD by default; offer toggle to AED, SAR, or LBP if user jurisdiction is detected
- MENA users are more receptive to "save time" framing than "save money" framing in professional contexts
- WhatsApp handoff: offer "Continue on WhatsApp" alongside upgrade CTA — MENA users may want to upgrade via WhatsApp with a human sales agent for Business/Enterprise plans

## Do not

- Never push upgrade during a user distress moment
- Never push more than once per day (frequency cap)
- Never say "this feature is not available" without immediately showing the path to unlock
- Never show a generic "upgrade for more" message — always tie to the specific blocked feature
- Never mock up or imply a feature is broken — clearly state it is a tier gate

## Examples

**Good** — deeply contextual:
> "Multi-document comparison is a Pro feature. With Pro, you can compare up to 10 contract versions side by side, saving ~2 hours of manual line-up. $79/mo. [Upgrade →] [Maybe later]"

**Bad** — generic and disconnected:
> "You've reached your limit. Please upgrade to continue using Louis."

## Related skills

- [[unlock-case-study-relevant-to-user]] — surface before upgrade prompt to prime with social proof
- [[unlock-empty-state-suggestions]] — starter suggestions for free-tier users who haven't hit a gate yet
- [[unlock-cross-product-bridge]] — bridge between product tiers (Justinian → Louis → Enterprise)
