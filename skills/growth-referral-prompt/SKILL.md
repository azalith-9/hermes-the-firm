---
name: growth-referral-prompt
description: Use when the platform needs to prompt satisfied Louis users to refer colleagues, with copy and mechanics for in-chat, email, and in-app modal channels. Defines triggers, timing rules, reward structures (AI tier vs eFirm tier), copy patterns, and the referral tracking page. Primary growth lever for lawyer-to-lawyer word-of-mouth in MENA markets where peer trust drives adoption more than advertising.
license: MIT
metadata: " id: growth.referral-prompt category: growth priority: P0 intent: [__growth__, referral, word-of-mouth, activation, MENA] related: [growth-nps-prompt, growth-case-study-asker, growth-email-onboarding-sequence, growth-push-notif-templates, unlock-contextual-upsell] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'growth'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Growth — Referral Prompts

## Purpose

In the MENA legal market, practitioner trust travels through professional networks — law school cohorts, bar association circles, firm alumni, WhatsApp groups. Advertising a legal AI product to lawyers generates skepticism; a recommendation from a trusted colleague generates trials. The referral program is therefore the highest-ROI acquisition channel for Louis in this market.

This skill defines when to prompt, how to prompt, the reward structure, and the mechanics of the referral flow.

## When to ask

Referral prompts have high conversion only when the user has genuine, recent positive experience:

| Trigger | Rationale |
|---|---|
| After a successful drafting or review session | User just experienced value; the endorsement is authentic |
| After NPS score 9–10 | User has self-declared they would recommend Louis |
| 30+ days of active continuous usage | Long-term user can speak credibly to colleagues |
| After paid plan upgrade | Willingness to pay reflects real conviction |
| After a referral from this user's network | If someone found Louis through them informally, formalize it |

## When NOT to ask

Asking at the wrong moment destroys trust and can permanently suppress referral behavior:

- Within 24 hours of a distress matter (divorce, insolvency, urgent litigation).
- Immediately after an error, bug, or refund request.
- Within 30 days of a prior referral prompt (regardless of whether the prior ask resulted in a referral).
- If the user has explicitly said they don't want to be asked (flag in CRM; suppress permanently unless user re-opts in).

## Prompt patterns

### Soft in-chat prompt
Appears after a qualifying task completes, inline in the chat:

> *"If Louis is saving you time, share with a colleague? You'll both get +50% credits this month."*

Two CTAs: **[Share link]** and **[Maybe later]**

The copy must be honest about the mutual benefit (both parties gain), brief (one sentence), and easy to dismiss. Do not block the chat flow.

### Email prompt
**Subject line variants** (A/B test):
- "Know a lawyer who'd love Louis?"
- "Share Louis with a colleague — you'll both benefit"
- "A quick request — 30 seconds"

**Body structure**:
1. One-paragraph rationale: "You've been using Louis for [X] months. If you know a colleague who could benefit, we'd be grateful for the introduction."
2. Personalized referral link (unique to user).
3. Reward explanation (clear, honest).
4. Optional: pre-written share copy they can paste directly into email or WhatsApp. ("Hi [Name], I've been using Louis, a legal AI for MENA practitioners. It's saved me significant time on [drafting/reviewing]. Here's a link to try it — we both get +50% credits.")

### In-app modal
Triggered after a qualifying task in the web/mobile interface:

- Visual: gift icon + reward badge
- Headline: "Share Louis, get rewarded"
- Sub-copy: one sentence mutual benefit explanation
- Referral link: prominent, one-tap copy
- Social share options: WhatsApp (primary for MENA), LinkedIn, Email
- Dismiss: clear X button; no dark patterns

## Reward structures

Rewards must be meaningful, honest, and easy to understand. No fine print.

| Tier | Referrer gets | Referred user gets | Cap |
|---|---|---|---|
| AI tier (consumer / individual) | +50% credits on their first paid month | +50% credits on their first paid month | 6 referrals per year per user |
| eFirm tier (B2B firm) | 1 free month of their plan | 1 free month after signup | 6 referrals per year per account |

**Cumulative cap**: 6 referrals per year prevents abuse while allowing genuine network effect.

**Tracking**: each referral is tracked via a unique link. The referral is credited when the referred user: (a) signs up, (b) completes at least one task, and (c) either upgrades or completes 30 days of active use. See `/referral` page for referrer's dashboard.

## MENA-specific considerations

- **WhatsApp is the primary share channel** for MENA legal practitioners; email is secondary. The referral flow must include a one-tap WhatsApp share that includes the message and link pre-formatted.
- **Arabic copy**: provide Arabic-language referral copy templates for users with Arabic language preference. Pre-written WhatsApp message should be available in Arabic.
- **Bar association ethics**: referral incentives (credit discounts) do not constitute fee-splitting and are not regulated as such. However, verify before adding cash or gift incentives, as some MENA bar rules restrict attorney advertising.
- **Cultural register**: the prompt should feel like an offer between peers, not a corporate referral program. The tone "we'd be grateful for the introduction" reads better in this market than "earn rewards."

## Referral page (`/referral`)

The referral page shows:
- The user's unique referral link.
- Their referral history: who signed up, who converted, total credits earned.
- One-click copy/share buttons.
- Pre-written share copy in both EN and AR.
- Terms of the reward program.

## Tracking and metrics

- **Referral invite rate**: % of qualifying users who click "share link" (target: > 15%).
- **Referral conversion rate**: % of referred sign-ups who complete first task within 7 days (target: > 40%; referred users convert faster than organic).
- **Credit redemption rate**: % of referred users who reach the paid tier and redeem the credit.
- **Attribution window**: 30 days from referral link click to account creation.

## Related skills

- [[growth-nps-prompt]]
- [[growth-case-study-asker]]
- [[growth-email-onboarding-sequence]]
- [[growth-push-notif-templates]]
- [[unlock-contextual-upsell]]
