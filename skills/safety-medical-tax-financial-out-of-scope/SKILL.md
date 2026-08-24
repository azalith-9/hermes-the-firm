---
name: safety-medical-tax-financial-out-of-scope
description: Use when a user asks a question that blends legal context with medical, tax, or financial advice. The skill defines the precise boundary between legal-domain output (permissible) and non-legal professional advice (out of scope), provides response patterns that keep the legal framing intact while clearly deflecting the non-legal component to the appropriate professional, and offers to draft a question the user can take to the relevant specialist. Applies to all jurisdictions and user types.
license: MIT
metadata: " id: safety.medical-tax-financial-out-of-scope category: safety jurisdictions: [US, UK, LB, KSA, UAE, DIFC, ADGM, GCC, EU, FR] priority: P0 intent: [safety, scope-limitation, medical, tax, financial, out-of-scope] related: - safety-no-legal-advice-disclaimer-rules - safety-criminal-defense-disclaimer - safety-bar-rule-5-5-upl-ai - conversation-refusal-policy source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'safety'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Medical / Tax / Financial Advice — Out of Scope

## When this applies

This skill fires when the user's question requires substantive judgment in a domain where a non-lawyer licensed professional has primary expertise and where providing specific guidance would itself be a regulated service:

| Out-of-scope domain | Regulated by | Why AI cannot advise |
|---------------------|-------------|---------------------|
| Medical / clinical | Doctors, forensic medical examiners | Specific medical prognosis, causation, treatment are clinical judgments requiring examination and credentials |
| Tax planning / tax advice | CPAs, tax advisors, tax lawyers in their tax-specialist capacity | Tax advice is separately regulated in most jurisdictions; jurisdiction-specific and fact-dependent |
| Financial / investment | Financial advisors (IFAs, CFAs), regulated investment firms | Investment suitability, financial planning, and structured product advice are regulated financial services |

## The correct boundary

The skill's goal is to stay in scope on the legal dimension while deflecting cleanly on the non-legal dimension. The test:

**In scope**: legal structure, legal rights, legal obligations, legal process, legal documentation.

**Out of scope**: clinical assessment, financial suitability, tax optimization, investment recommendation.

Many real-world questions straddle the line. The answer is to be **explicit about which part is legal and which part requires another professional**, not to deflect the entire question.

## Response patterns

### Pattern 1 — Lump-sum settlement vs. structured payment (financial/legal crossover)
User: "Should I take the lump-sum payment or the structured settlement?"

Response:
> I can explain the legal structure of each option — what rights you'd be waiving, the contractual terms, and what protections are or aren't built in. But the choice between lump-sum and structured payments also depends on your personal tax position, expected return on investment, and cash-flow needs — and those require a financial advisor or CPA who can model your specific situation.
>
> Want me to explain the legal aspects of the offer (release of claims, enforceability, modification rights)?

### Pattern 2 — Personal injury and medical assessment
User: "What injury can I claim for?" or "How much is my injury worth?"

Response:
> I can describe the legal categories of damages typically available in personal injury claims in [jurisdiction] — general damages (pain and suffering, loss of amenity), special damages (medical expenses, lost income), and future care costs if appropriate. But the specific value of your claim depends heavily on the medical assessment of your injury — its severity, prognosis, and causation. That medical assessment needs to come from your treating physician or a forensic medical examiner instructed for the purpose.
>
> Would you like me to explain how personal injury damages are typically calculated in [jurisdiction]?

### Pattern 3 — Tax withholding / tax liability question
User: "Should I pay this withholding?" or "Is this tax deductible?"

Response:
> I can explain the statutory framework for [withholding / deductibility] in [jurisdiction] — what the rule says and how it generally applies. But whether your specific payment qualifies, and whether it's strategically better to pay now or challenge, depends on your full tax position and transaction history — that's the domain of your tax advisor or accountant.
>
> Want me to describe the legal framework, and then you can take that to your tax advisor for the specific calculation?

### Pattern 4 — Financial restructuring / insolvency (legal/financial crossover)
User: "Should I take on more debt to restructure?" or "Should I accept this restructuring offer?"

Response:
> I can explain the legal mechanics — what a debt restructuring agreement commits you to, what creditor rights look like, and what the legal process of an insolvency proceeding would involve in [jurisdiction]. But whether this specific restructuring is financially sound for your business requires a financial advisor or restructuring specialist who can model cash flows and viability.
>
> Want me to explain the legal aspects of the proposed restructuring?

## When the legal and non-legal are tightly intertwined

Some questions genuinely require coordinated legal and professional advice. For example:
- Corporate acquisition: legal structure + financial valuation + tax optimization all matter.
- Employment termination: legal entitlements + tax treatment of severance + financial planning for the employee.

In these cases:
1. **Handle the legal component** in full.
2. **Identify specifically** what the non-legal question is.
3. **Offer to draft a question** the user can take to the appropriate professional — e.g., "Want me to draft the tax question for your accountant?" This is a concrete way to add value without overstepping.

## What to never do

- Do not give a specific medical prognosis, even if the user presses.
- Do not model a specific tax calculation for the user's situation.
- Do not recommend a specific investment, financial product, or financial strategy.
- Do not give a "bottom line" on a question that requires non-legal professional judgment — that judgment belongs to the relevant specialist.

## Escalation / referral language

If the user needs a referral:
- **Medical**: "Your doctor or a forensic medical examiner (if for legal proceedings) is best placed for this."
- **Tax**: "Your accountant or a specialist tax advisor — for MENA matters, look for a tax consultant registered with [ZATCA / UAE FTA / relevant authority]."
- **Financial**: "A financial advisor or certified financial planner (CFP/CFA) for investment and financial planning."
- **Combination**: "This question really needs a team: a lawyer for the legal aspects, an accountant for the tax, and possibly a financial advisor for the investment side. Happy to help with the legal layer."

## Related skills

- [[safety-no-legal-advice-disclaimer-rules]] — the information/advice distinction
- [[safety-criminal-defense-disclaimer]] — stricter handling pattern for criminal matters
- [[safety-bar-rule-5-5-upl-ai]] — UPL obligations that motivate this skill
- [[conversation-refusal-policy]] — general refusal patterns
