---
name: efirm-fee-quote-builder
description: Use when a law firm partner or business development team needs to construct a formal fee proposal for a prospective or existing client. Covers all major fee structures (hourly, fixed, contingency, capped, collared, milestone, subscription, hybrid), produces a complete quote with scope, assumptions, tax treatment, and validity, and flags MENA-specific restrictions on contingency and retainer arrangements. Output flows directly into the engagement letter.
license: MIT
metadata: " id: efirm.fee-quote-builder category: efirm jurisdictions: [__multi__] priority: P0 intent: [fee quote, billing structure, AFA, retainer, proposal, scope] related: - efirm-engagement-letter-draft - efirm-matter-creation-flow - efirm-finance-realization-rate-tracker - efirm-finance-wip-aging-report source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm'.
Namespaced as louis-<category>-<skill> on registration.
-->


# eFirm: Fee Quote Builder

## When to use this

Use this skill to:
- Build a formal fee proposal in response to a client Request for Proposal (RFP) or new matter instruction.
- Advise a client who asks "how much will this cost?" in a way that protects the firm and sets realistic expectations.
- Evaluate which fee structure best matches the matter type, risk profile, and client preference.
- Prepare the fee section of an engagement letter ([[efirm-engagement-letter-draft]]).
- Review whether an existing fee arrangement remains appropriate as a matter evolves.

## Fee structures — when to use each

### 1. Hourly — rates by seniority; estimate + ceiling

The baseline structure. The client pays for time spent at agreed rates.

**Best for**: matters where scope is unclear at outset (complex litigation; restructuring; regulatory investigation).

**Anti-pattern**: presenting a rate card with no estimate. This is the single most client-criticized practice in legal billing surveys. Always accompany hourly rates with a range estimate and scope assumptions.

**Format**:
- Rate card by seniority (Partner / Senior Associate / Associate / Paralegal)
- Estimated range (e.g., "USD 80,000–120,000 based on the assumptions below")
- Scope assumptions (explicitly stated — if these change, the estimate changes)
- Ceiling option: "We will not exceed USD X without your prior written approval"

### 2. Fixed fee — single sum for defined deliverable

Client pays a flat amount for a specific deliverable.

**Best for**: commoditized, well-scoped work (standard NDA drafting; company formation; straightforward employment contract; conveyancing).

**Anti-pattern**: fixed fees without a tight scope definition. Every fixed-fee engagement must have a list of what is included and what is explicitly excluded (scope changes go on a separate instruction).

**Format**:
- Total fixed fee: USD X
- Scope: [precise description of deliverable]
- Included: [list]
- Not included: [list — especially: negotiations, regulatory filings, litigation, amendments]
- Out-of-pocket expenses: pass-through at cost

### 3. Contingency — % of recovery

The firm's fee is a percentage of the recovery the client achieves.

**Best for**: plaintiff-side litigation where client cannot afford hourly fees and the claim is strong.

**Jurisdiction restrictions**:
| Jurisdiction | Status |
|---|---|
| US | Permitted for most civil claims; prohibited for criminal defense and certain family law matters; percentage negotiated |
| UK | "Conditional fee agreement" (CFA); caps apply under Access to Justice Act framework |
| DIFC / ADGM | Permitted with disclosure; DIFC Courts Practice Direction governs |
| UAE onshore | Disfavoured; consult current Bar guidance |
| KSA | Disfavoured / restricted for most matters; consult Saudi Bar Association |
| Lebanon | Generally disfavoured; Beirut Bar has guidance |
| France | Pure contingency (pactum de quota litis) is prohibited; "success fee" on top of hourly base is permitted under strict conditions |

**Always check current bar rules before proposing contingency.**

### 4. Capped fee — hourly up to a ceiling

The client pays hourly rates, but the firm absorbs overrun above an agreed cap.

**Best for**: clients who want hourly transparency with cost certainty; matters where scope is moderately predictable.

**Risk**: the firm absorbs overrun risk. Only offer caps on matter types where historical data supports the estimate. Use [[efirm-finance-realization-rate-tracker]] and WIP data to calibrate.

### 5. Collared fee — hourly with floor + ceiling

Both client and firm share risk: if the matter comes in under the floor, the client pays the floor; if over the ceiling, the firm absorbs. The "collar" is the range between floor and ceiling.

**Best for**: risk-sharing on medium-complexity matters with reasonable scope predictability.

### 6. Milestone-based — installments tied to deliverables

Payment is triggered by defined milestones (e.g., 30% on engagement; 30% on first draft; 40% on execution).

**Best for**: large transactions with defined phases; avoids the billing drag of monthly invoices on slow-moving deals.

### 7. Subscription — monthly retainer for ongoing advisory work

The client pays a fixed monthly fee for access to defined legal services.

**Best for**: general counsel advisory relationships; compliance monitoring; recurring small-matter work.

**Scope discipline is critical**: define clearly what is and is not covered. Subscription clients tend to over-demand; the scope boundary prevents underpricing.

### 8. Hybrid — fixed for routine + hourly for non-routine

Combines predictability for standard work with flexibility for complex or unanticipated elements.

**Example**: "Fixed fee of USD X for the transaction documents; hourly rates apply for regulatory filings, which are scope-dependent."

## Quote contents — mandatory sections

A complete fee quote contains all of the following:

### 1. Matter scope

```
SCOPE OF THIS QUOTE

This quote covers:
  - [Specific deliverable 1]
  - [Specific deliverable 2]
  ...

This quote does NOT cover:
  - [Exclusion 1 — e.g., regulatory filings]
  - [Exclusion 2 — e.g., litigation arising from the transaction]
  - [Exclusion 3 — e.g., advice in jurisdictions other than [X]]

Scope changes will be agreed in writing and quoted separately.
```

### 2. Fee structure choice + rationale

Brief explanation of why the chosen structure was recommended (one paragraph).

### 3. Estimate with assumptions and scope limits

```
FEE ESTIMATE

Based on our experience with similar matters and the assumptions below, we estimate
fees of USD [X] – USD [Y].

Assumptions:
  1. [Number of counterparties / complexity level]
  2. [Cooperation level from client in providing documents]
  3. [No litigation arising]
  4. [Single-jurisdiction matter]

If any assumption changes, we will promptly advise you of the revised estimate.
```

### 4. Out-of-pocket expenses

```
EXPENSES

The estimate above does not include disbursements, which are passed through at cost:
  - Court filing fees, registration fees
  - Notarization and legalization
  - Translation services
  - Travel (if required; approved in advance)
  - Third-party data room / technology costs
```

### 5. Trust / retainer requirements

```
RETAINER

We require an initial retainer of USD [X] before commencing work.
This will be held in our [IOLTA / designated client / trust] account and applied 
against final invoices.
```

### 6. Billing cadence

Monthly / on milestone / on completion. State whether invoices are due net-30 or other.

### 7. Tax / VAT treatment

| Jurisdiction | VAT / Tax treatment |
|---|---|
| UAE | 5% VAT on legal services under Federal Decree-Law No. 8 of 2017 |
| KSA | 15% VAT on legal services |
| Bahrain | 10% VAT |
| Lebanon | No VAT on legal services (professional services exemption) |
| France | 20% TVA on legal services |
| UK | 20% VAT on legal services |
| DIFC / ADGM | Follow UAE VAT rules if registered |
| US | No federal VAT; state sales tax on legal services varies by state (most exempt) |

Always state whether quoted amounts are VAT-inclusive or exclusive.

### 8. Scope-change mechanism

```
SCOPE CHANGES

Any work outside the scope defined above requires a separate written instruction.
We will provide a supplemental fee estimate before commencing any additional work.
```

### 9. Validity

```
VALIDITY

This quote is valid for 30 days from the date above.
After that date, rates and estimates are subject to revision.
```

## Anti-patterns to avoid

| Anti-pattern | Problem |
|---|---|
| "Hourly, see attached rate card" with no estimate | Clients cannot budget; damages trust; leads to billing disputes |
| Fixed fee without tight scope | Scope creep makes the matter unprofitable; creates renegotiation friction |
| Promising specific outcomes | Violates professional conduct rules in all covered jurisdictions |
| Contingency without checking bar rules | May be an ethics violation in KSA, Lebanon, France |
| No VAT line | Invoice disputes; regulatory exposure |
| No expense pass-through clause | Client disputes about who pays for court fees, translations |

## MENA-specific notes

- **KSA**: contingency is disfavoured and in many matter types effectively prohibited. Milestone-based or hourly-with-ceiling is the typical alternative.
- **UAE**: client funds held as retainer are subject to escrow/trust rules; state clearly which account holds the retainer and how it is released.
- **Lebanon**: bar fee schedule provides minimum fee guidelines for certain matter types; check that the quote does not fall below bar minimums.
- **GCC generally**: government clients often expect formal fee negotiations and may require ministry approval of legal fees above certain thresholds; build in a longer quote-validity period and approval process.

## Related skills

- [[efirm-engagement-letter-draft]]
- [[efirm-matter-creation-flow]]
- [[efirm-finance-realization-rate-tracker]]
- [[efirm-finance-wip-aging-report]]
- [[efirm-client-intake-form]]
