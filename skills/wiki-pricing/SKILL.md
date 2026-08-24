---
name: wiki-pricing
description: Use when designing or evaluating pricing strategy for a legal-AI product — covering tiered and usage-based pricing, feature-gating, the free-tier and BYO-key model, enterprise vs SMB pricing dynamics, and the specific considerations of pricing in MENA markets where willingness-to-pay and purchasing structures differ from US/EU SaaS norms. Reach for this skill when the user asks about pricing tiers, monetisation strategy, feature flags, or how to price a legal-AI product.
license: MIT
metadata: " id: wiki.pricing category: wiki jurisdictions: [UAE, KSA, LB, __multi__] priority: P3 intent: [__wiki__, pricing, monetisation, tiered-pricing, usage-based, MENA-pricing] related: [wiki-growth, wiki-market, wiki-fundraising, wiki-haqq-product, wiki-product-mgmt] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Registered as a flat plugin skill.
-->


# Pricing Strategy for Legal-AI Products

## Scope

This pack covers pricing design for a legal-AI product: tier architecture, pricing models, feature-gating mechanics, the BYO-key strategy, enterprise pricing, and the MENA-specific considerations that affect willingness to pay and purchasing behaviour. It connects to the HAQQ product positioning of 100% free + BYO key as the default growth motion.

---

## Pricing model options

### Tiered subscription

The most common SaaS pricing model. Offer 2–4 tiers with clearly differentiated value:

| Tier | Target | Price point | Key features |
|---|---|---|---|
| Free | Solo practitioners, trial | $0 | Core skills; BYO key; limited document storage |
| Starter | Solo / small firm | $29–49/month | All core skills; higher limits; basic analytics |
| Professional | Individual lawyer at a firm | $79–129/month | Advanced skills; integrations; priority support |
| Firm / Team | Law firm account | $200–500/month (flat or per seat) | Team features; admin dashboard; custom skills |
| Enterprise | Large firms, in-house | Custom (ACV $10 k–$100 k+) | SSO, audit log export, custom data residency, SLA |

### Usage-based pricing

Charge per skill invocation, per document processed, or per LLM token consumed. More transparent for users who want to control costs; more complex to predict for the business.

**Hybrid**: a subscription that includes a usage allowance (e.g. 500 skill invocations/month), with overage charged at a per-unit rate. This is the current best-practice for AI products where underlying model costs are usage-proportional.

### Feature-gated pricing

Features are the primary differentiation between tiers — not limits alone. Examples:
- Free tier: drafting + review of standard documents
- Paid tier: cross-jurisdictional analysis, custom playbooks, deal comparison, API access
- Enterprise: custom skill authoring, SSO, data residency, dedicated instance

Feature gating is more defensible than limit-based gating (a user who hits a limit feels frustrated; a user who sees an upgrade prompt on a clearly valuable feature is motivated to upgrade).

---

## BYO key (Bring Your Own Key) model

A BYO-key model allows users to provide their own LLM API key (Anthropic, OpenAI, etc.) to power the product, with the product charging for the platform and features but not for model usage.

**Strategic rationale for HAQQ:**
- Removes cost barrier for solo practitioners and small firms who otherwise can't afford per-use AI
- Differentiates from competitors whose usage-based pricing makes regular use expensive at scale
- Signals transparency and alignment — the product doesn't profit from model usage markup
- Creates a developer-platform framing — builders use BYO key as a matter of course

**Implementation considerations:**
- Store API keys encrypted at rest; never log or expose them in plaintext
- Allow multiple keys (Anthropic, OpenAI) and route based on user preference or skill requirement
- Show users their approximate token usage and cost against the API key so they maintain visibility
- BYO-key users must accept responsibility for their API usage costs; make this clear in onboarding

---

## MENA pricing considerations

### Willingness to pay

MENA legal professionals' willingness to pay for SaaS tools is generally lower than US/UK equivalents, for several reasons:
- Lower baseline software spend per professional (many MENA firms still rely on manual processes or pirated software rather than commercial SaaS)
- Price sensitivity is higher in Lebanon and Egypt than in UAE and KSA (GDP per capita differences)
- Government and quasi-government entities in GCC have budget but slow procurement; they are not monthly credit-card customers

**Practical implication**: a $99/month individual plan that is market-standard in the US may need to be $49 or $39 in the MENA pricing version. Alternatively, offer an annual plan with a significant discount (30–40%) to capture the price-sensitive segment.

### Currency and payment

- UAE: card payments work well; USD pricing is standard for international SaaS; AED pricing is appreciated
- KSA: MADA (local debit) is more common than international credit cards; offering MADA integration significantly increases conversion with Saudi consumers
- Lebanon: USD card payments are the functional option; avoid LBP pricing
- Egypt: EGP pricing for local market; international cards work for the professional segment

### Procurement and purchasing behaviour

In GCC, many mid-size to large law firm purchases go through an IT or procurement process, not direct individual subscription. This has implications:
- Annual invoiced billing (PO + 30-day payment terms) is required for firm-level sales
- A "request a quote" path is needed in addition to self-serve checkout
- VAT invoicing (UAE 5%, KSA 15%) must be correct on all invoices; non-compliant invoices will be rejected by corporate buyers

---

## Public-tool vs enterprise pricing

For HAQQ, the free/BYO-key model functions as a "public tool" — accessible to anyone with an API key, with full core functionality. This is a strategic choice with pricing implications:

**Why public-tool works:**
- Creates bottom-up adoption (individual lawyers adopt, then bring to the firm)
- Builds the developer-platform ecosystem (builders use the free tier to build on the platform)
- Generates organic distribution through the MENA legal community

**The enterprise upsell path:**
- Free individual → Starter (when they want more storage and features) → Professional (when they want integrations and advanced skills) → Firm plan (when they recommend it to colleagues) → Enterprise (when the firm's IT team gets involved and wants SSO, audit, and data residency)

The key at each step: the upgrade must be clearly justified by concrete additional value, not just by artificially hitting limits on the free tier.

---

## Competitive pricing context

| Product | Model | Price range |
|---|---|---|
| Harvey | Enterprise only | Custom ($50 k–$500 k+ ACV) |
| CoCounsel | Add-on to Thomson Reuters subscription | $50–150/month per seat |
| Spellbook | Freemium | Free → $25–75/month |
| Robin AI | SMB SaaS | $50–150/month |
| Genie AI | Freemium | Free → $50–100/month |

HAQQ's positioning: more accessible than Harvey (which doesn't serve the MENA mid-market), more capable than Spellbook (which lacks MENA law knowledge), and differentiated from all by Arabic-language support and MENA-first domain knowledge.

---

## Caveats & currency

Pricing should be validated against real willingness-to-pay data from actual users, not only benchmarks. Run price sensitivity surveys (Van Westendorp, Gabor-Granger) with a sample of your target users before committing to a price architecture. MENA payment processor availability changes; verify current Stripe, Tamara, and MADA integration options before committing to a payment stack.

---

## Related skills

- [[wiki-growth]]
- [[wiki-market]]
- [[wiki-fundraising]]
- [[wiki-haqq-product]]
- [[wiki-product-mgmt]]
