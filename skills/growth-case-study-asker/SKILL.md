---
name: growth-case-study-asker
description: Use when the platform needs to collect user testimonials and case studies from satisfied Louis users for marketing, investor, and sales purposes. Defines the triggers, consent workflow, format, permission tiers, and incentive structure for gathering attorney and firm case studies. Applies primarily to MENA-region legal practitioners. Always obtain explicit permission before any public attribution.
license: MIT
metadata: " id: growth.case-study-asker category: growth priority: P1 intent: [__growth__, testimonial, case-study, social-proof, marketing] related: [growth-nps-prompt, growth-referral-prompt, growth-email-onboarding-sequence, growth-win-back-inactive] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'growth'.
Registered as a flat plugin skill.
-->


# Growth — Case Study Asker

## Purpose

Case studies and testimonials are the highest-trust marketing asset for a legal AI product. Lawyers are a skeptical audience — they respond to evidence from peers, not product claims. A single well-attributed case study from a respected Beirut partner or Dubai in-house counsel is worth more than dozens of generic marketing claims.

This skill defines the end-to-end process for: identifying the right moment to ask, how to ask without creating pressure, what format the case study should follow, what permission levels to get, and how the output is used.

## When to ask

Ask for a case study or testimonial only when the user has demonstrably received value. The qualifying triggers are:

| Trigger | Rationale |
|---|---|
| NPS score 9–10 | Explicit signal of satisfaction; user has self-declared enthusiasm |
| Significant time-savings task completed | e.g., drafting a full M&A due-diligence SPA, reviewing a 50-clause employment contract — the user has lived the value |
| Paid plan upgrade | Willingness to pay is a strong value signal |
| 90+ days of continuous active usage | Long-term retention suggests real integration into workflow |
| Referral made (user referred a colleague) | Already acting as advocate; formalize it |

## When NOT to ask

- Within 24 hours of a distress matter (divorce, insolvency, urgent litigation) — emotional context makes any sales ask inappropriate.
- After a bug, error, or refund request.
- If the user has already been asked within the past 90 days.
- If the user has previously declined (flag in CRM; do not re-ask unless 12+ months have passed).

## How to ask

### In-chat (soft, low-friction)
Trigger this prompt after a qualifying task completes:

> "Glad that worked well. If Louis is saving you time on matters like this, would you be open to sharing how you use it? We feature user stories from the region — fully anonymous by default, and only ever published with your explicit sign-off."

Include two CTAs: **[Sure, tell me more]** and **[Not right now]**.

### Email outreach (structured questionnaire)
Send 24–48 hours after a qualifying event. Subject line variants to A/B test:
- "How do you use Louis? (2-minute read)"
- "Your experience with Louis — worth sharing?"
- "A quick question from [Stephane / the Louis team]"

The questionnaire has five questions (see format below) with an estimate of 5–10 minutes to complete.

### Personal outreach (high-value accounts)
For enterprise/eFirm accounts or marquee individual users (partner at a top-20 MENA firm, known practitioner): direct personal reach-out from the founder or CS lead via email or LinkedIn. Higher conversion rate; reserve for high-signal accounts.

## Case study format

Every case study, regardless of permission tier, should capture:

1. **User intro**: role, firm type, jurisdiction. With permission, name and firm.
2. **Use case**: what specific legal problem or workflow they used Louis for.
3. **Process**: how they integrated Louis into their practice — was it drafting? review? research? matter management?
4. **Outcome**: quantified results where possible:
   - Time savings ("from 3 hours to 45 minutes on NDA review")
   - Quality improvement ("caught 4 issues in a standard employment contract I would have missed")
   - Cost savings ("reduced outside counsel spend by X%")
5. **Pull quote**: a single quotable sentence, attorney-approved, suitable for marketing use.

## Permission tiers

Obtain explicit, written consent before any public use. The tiers are:

| Tier | What is disclosed | Example |
|---|---|---|
| Anonymous | Role type + jurisdiction only; no name or firm | "A senior corporate partner in Dubai…" |
| Firm-named, person-anonymous | Firm name disclosed; individual not named | "[Firm] uses Louis for…" |
| Fully named | Full name, title, firm | "Lazar Saliba, Partner at [Firm], says…" |
| Logo use | Firm logo in marketing materials | Requires separate explicit written consent |

**Default for first ask**: anonymous tier. Users can upgrade their permission level later; never assume or push toward a higher tier.

## Incentives

Incentives for participation (offer but never condition use on receipt):

- Free month / credit extension as a thank-you.
- Feature in the case study (PR value for the firm).
- Invitation to Louis advisory program / beta access.
- Speaking slot at a Louis-hosted event (for high-profile participants).

## Where case studies are used

- `/case-study/[slug]` pages on the Louis marketing site.
- Investor decks and board updates.
- Sales pitch materials for eFirm prospects.
- Feature in [[growth-email-onboarding-sequence]] Day 21 email (persona-matched).
- Conference presentations and legal tech event talks.

## Quality and compliance rules

- **Never publish without sign-off**: the attorney must approve the final version before any public use.
- **No quid pro quo**: do not offer increased use limits, discounts, or preferential treatment contingent on participation. Incentives are thank-you gifts, not payments for endorsement.
- **Attribution accuracy**: always attribute to the correct person, role, and firm as consented. Errors in attribution can embarrass the attorney and destroy trust.
- **Confidentiality**: case studies must not disclose any client matter details, even implicitly. The focus is on the attorney's process and outcome, not the underlying legal matter.
- **Bar rules awareness**: in some MENA jurisdictions, attorney advertising is regulated. Review the relevant bar association rules before publishing. Lebanon Bar Association and UAE bar rules should be verified before publication.

## Tracking and metrics

- Conversion rate: asks → responses → usable case studies.
- Permission tier distribution (how many reach fully-named vs anonymous).
- Case study impact: track whether case-study pages or email inclusions drive conversion or trial upgrades.
- Referrals generated by case study readers.

## Related skills

- [[growth-nps-prompt]]
- [[growth-referral-prompt]]
- [[growth-email-onboarding-sequence]]
- [[growth-win-back-inactive]]
