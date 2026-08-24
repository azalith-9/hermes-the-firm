---
name: messaging-pricing-framing-b2c
description: Use when writing pricing page copy, free-tier promotional language, upgrade prompts, or any B2C consumer-facing content that involves communicating cost and value for a legal AI assistant. Defines how to frame the free tier, the upgrade proposition, and the value anchor against professional legal costs — without making banned lawyer-replacement claims or triggering consumer protection concerns about misleading price representations.
license: MIT
metadata: " id: messaging.pricing-framing-B2C category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, pricing, B2C, freemium, value-proposition, consumer] related: [messaging-allowed-claims-consumer, messaging-banned-claims-consumer, messaging-outcome-claims-allowed, messaging-compliance-checker, messaging-bridge-line] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Registered as a flat plugin skill.
-->


# Messaging — Pricing Framing B2C

## When this applies

This skill governs how pricing is communicated to **non-lawyer consumers** (individuals, SME founders, and everyday users). It applies to:

- Pricing page copy
- Free-tier promotional messaging
- Upgrade prompts and paywalls
- Onboarding copy referencing cost
- Comparison sections on the website
- Social and search ads referencing the free tier
- Email campaigns about plan upgrades or promotions

It does **not** govern B2B/lawyer-tier pricing framing (covered separately) or financial claims that function as outcome guarantees (covered by [[messaging-outcome-claims-banned]]).

---

## Core Pricing Framing Principle

**Lead with free; unlock more with paid.** The B2C pricing narrative always starts from accessibility, not cost. The product removes barriers to legal understanding; price should never be the first thing a consumer sees.

The value anchor for paid tiers is the **cost of professional legal assistance**, not the cost of competitive products. This framing:
1. Sets consumer expectations about the real cost of legal help
2. Makes the paid tier feel dramatically underpriced by comparison
3. Avoids direct competitor comparison (which requires substantiation)
4. Stays within the bridge line — it emphasises understanding, not lawyer replacement

---

## The Freemium Frame

### What "free" means in this context

The free tier provides genuine, unrestricted access to legal information, orientation, and basic template generation. "Free" is not a bait — it is the product's commitment to accessible legal understanding. Copy must reflect this:

**Allowed:**
- "Free to start — no credit card required"
- "Your first [N] legal questions, free"
- "Understand your legal situation — for free"
- "Access basic legal information at no cost"

**Not allowed:**
- "Free legal advice" — even if the tier is free, "legal advice" implies licensed practitioner advice (UPL trigger)
- "Free lawyer" — same issue
- Free framing combined with any claim that the free tier provides the equivalent of professional legal counsel

### Upgrade framing

The upgrade from free to paid must be framed as **unlocking more depth and capability**, not as removing an artificial limitation:

| Weak upgrade frame (avoid) | Strong upgrade frame (use) |
|---------------------------|---------------------------|
| "Unlock premium" | "Get deeper analysis, longer documents, and full multi-jurisdiction coverage" |
| "Upgrade to get more" | "Handle complex contracts, multi-party agreements, and cross-border drafting" |
| "Go Pro to remove limits" | "Go Pro for the full legal workbench — used by SME founders managing real contracts" |

---

## Value Anchoring Against Professional Costs

The canonical value anchor: **professional legal assistance in the MENA region typically costs USD 200–500 per hour** (junior associate to partner range; varies significantly by jurisdiction and firm size).

This anchor is used to give consumer users a frame of reference for what the product's paid tier costs relative to the alternative:

**Allowed formulations:**
- "A typical lawyer consultation starts at $200/hour. Louis starts at $[X]/month."
- "For the cost of one lawyer hour, you get a full month of legal understanding."
- "What would take an hour of lawyer time, Louis does in minutes."

**Framing rules for this anchor:**
- Frame it as "understanding" vs "professional advice" — not as a direct service substitute
- Do not imply the product replaces the need for a lawyer in complex situations — add "for situations that need a lawyer, Louis helps you arrive prepared"
- Do not use the anchor with a specific dollar amount for a specific jurisdiction unless that amount is verified and accurate for that market
- Disclaim that the anchor is a general range, not a guarantee of savings

**What to avoid:**
- "Louis saves you $500 an hour" — specific savings guarantee; banned under [[messaging-outcome-claims-banned]]
- "Skip the $500 lawyer bill" — lawyer replacement framing; banned under [[messaging-banned-claims-consumer]]

---

## Per-Tier Copy Guidance

| Tier | Positioning | Key copy elements |
|------|-------------|------------------|
| Free | Legal understanding for everyone | "Start free", accessibility, plain language, "no jargon" |
| Basic/Starter paid | Serious self-help for active legal situations | "Unlimited questions", "longer documents", "save and share" |
| Pro / Power user | Full self-help + preparation + SME workflows | "Multi-jurisdiction", "draft contracts", "document workspace" |
| Business / SME | Founder or small business operations | "For growing businesses", "vendor contracts", "employment templates", "built-in jurisdiction guidance" |

---

## Show Value Per Use

Where analytics allow, show users the value they have already extracted from the product:
- "You've asked 14 legal questions this month — worth [N] minutes of lawyer time."
- "Your NDA draft is ready — a lawyer would charge [X range] for this starting point."

This reinforces the upgrade value proposition while staying within the "starting point, review with a lawyer" framing.

---

## Examples

**Strong B2C pricing copy:**
> "Start free. Ask your first legal question — no credit card, no jargon. When your situation gets more complex, Louis Pro handles multi-party contracts, multi-jurisdiction research, and document workspaces — for less than the cost of a single lawyer consultation."

**Weak B2C pricing copy (avoid):**
> "Upgrade to Louis Pro and never pay for a lawyer again." *(banned claim)*

**Strong upgrade prompt:**
> "You're drafting a contract across two jurisdictions. Go Pro to unlock multi-jurisdiction drafting, clause comparison, and full document analysis."

---

## Related skills

- [[messaging-allowed-claims-consumer]]
- [[messaging-banned-claims-consumer]]
- [[messaging-outcome-claims-allowed]]
- [[messaging-outcome-claims-banned]]
- [[messaging-compliance-checker]]
- [[messaging-bridge-line]]
