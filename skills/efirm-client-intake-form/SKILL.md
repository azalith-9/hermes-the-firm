---
name: efirm-client-intake-form
description: Use when a law firm needs to open a new client file — the skill generates a tailored intake form, captures identity and entity information, collects opposing-party details for conflict checking, triggers AML/sanctions screening, and fires the downstream engagement workflow. Covers KSA Bar, UAE MOJ, Lebanon Bar, and DIFC/ADGM SRO compliance requirements. This is the gateway step to all subsequent matter-creation and engagement work.
license: MIT
metadata: " id: efirm.client-intake-form category: efirm jurisdictions: [KSA, UAE, LB, DIFC, ADGM, __multi__] priority: P1 intent: [intake, onboarding, AML, KYC, conflict-check, engagement] related: - efirm-conflict-check - efirm-engagement-letter-draft - efirm-matter-creation-flow - efirm-fee-quote-builder source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm'.
Registered as a flat plugin skill.
-->


# Client Intake Form

## When to use this

Use this skill when:
- A new prospective client contacts the firm and a formal matter file needs to be opened.
- An existing client brings a new matter with new counterparties not previously in the system.
- A client's ownership structure has changed (new UBOs) and KYC refresh is required.
- The firm is onboarding a client referred from another jurisdiction and needs jurisdiction-specific intake fields.

The intake form is the **mandatory first step** before any substantive legal work begins. It triggers the conflict check, AML screening, and engagement letter workflow — none of which can be completed without the intake data.

## Required fields

### Section 1: Individual client identity

| Field | Why required | Notes |
|---|---|---|
| Full legal name | Conflict check; engagement letter | As on passport/ID |
| Date of birth | Identity verification; AML | |
| Nationality | Regulatory; restrictions may apply | |
| National ID / Passport number | KYC; identity verification | |
| Residential address | Engagement letter; service of process | |
| Contact details (phone, email) | Communication | |
| PEP status (Politically Exposed Person) | AML obligation | Self-declaration + screening |
| Source of funds (matter payment) | AML obligation | Required in all MENA and UK/EU jurisdictions |

### Section 2: Entity client identity

| Field | Why required | Notes |
|---|---|---|
| Legal name of entity | Conflict check; engagement | |
| Jurisdiction of incorporation | Regulatory; governing law | |
| Commercial registration number (CR) | Identity; KSA/UAE required | |
| Registered address | Engagement letter | |
| Ultimate beneficial owners (UBOs) | AML — 25% threshold standard | Each UBO must complete individual section |
| Authorised signatory | Engagement letter execution | Must provide authorization document |
| Corporate structure chart | AML; complex structures | Required if >2 holding tiers |
| Entity type | Company / Foundation / Trust / Partnership | Affects AML obligations |

### Section 3: Matter description

| Field | Notes |
|---|---|
| Short matter title | Descriptive; used for matter record |
| Matter type | Corporate / Dispute / IP / Employment / Regulatory / Personal |
| Brief factual description | Key facts; counterparties; jurisdiction |
| Urgency level | Standard / Urgent / Emergency |
| Estimated duration | Client expectation; resource planning |

### Section 4: Opposing parties (conflict check inputs)

| Field | Notes |
|---|---|
| Opposing party names (all) | Every adverse party, their counsel if known |
| Corporate groups / parents | Conflict checks must reach parent company |
| UBOs of opposing entities (if known) | Issue conflicts possible even if entities differ |
| Witnesses / key third parties | Where positional conflicts may arise |

### Section 5: Payment and AML

| Field | Notes |
|---|---|
| Paying party (if different from client) | Common in cross-border matters; AML checks apply |
| Source of funds | Earned income / sale proceeds / loan / inheritance / other |
| Expected payment currency | USD / AED / SAR / LBP / EUR / other |
| Retainer amount required | Linked to fee quote |
| Payment method | Bank transfer / cheque / other (no cash above thresholds) |

### Section 6: Engagement scope and acknowledgments

| Field | Notes |
|---|---|
| Scope of engagement | What the firm is being retained to do |
| Out-of-scope items (explicit) | Prevents scope creep disputes |
| Fee structure acknowledgment | Client confirms understanding of fee basis |
| Conflict waiver (if applicable) | If a conflict exists and is being waived |
| Marketing preferences | Opt-in/out of firm updates |
| Governing jurisdiction for engagement | For multi-jurisdictional clients |

## Auto-triggered downstream actions

On submission of a complete intake form, the following actions are triggered automatically:

1. **[[efirm-conflict-check]]** — runs against all parties listed in Sections 1–4.
2. **Sanctions screening** — screens all parties against OFAC, EU, UN, DFSA, and relevant national lists.
3. **Beneficial ownership lookup** — verifies UBO data against commercial registry records where available.
4. **PEP screening** — cross-references politically exposed person lists.
5. **AML risk scoring** — generates a risk classification (low / medium / high / declined) based on entity type, jurisdiction, matter type, and source of funds.
6. **[[efirm-engagement-letter-draft]]** — pre-populated with data from this form; routed to responsible partner for review.

If any of (1)–(5) returns a flag, the intake is held for partner review before the engagement letter is generated.

## Jurisdiction-specific compliance notes

| Jurisdiction | Key requirements |
|---|---|
| KSA | Saudi Bar Association requires licensed attorney to certify client identity; foreign clients require Saudi sponsor/agent identification; Zakat/VAT number for corporate clients |
| UAE (onshore) | Anti-Money Laundering Law (Federal Law No. 20 of 2018) applies to lawyers; DNFBP (designated non-financial business and profession) obligations include CDD and suspicious transaction reporting |
| DIFC | DFSA Rulebook and DIFC Anti-Money Laundering Law apply; AML Officer appointment required for firms meeting threshold; enhanced due diligence for PEPs and high-risk jurisdictions |
| ADGM | FSRA rules and ADGM AML regulations; similar to DIFC in rigor |
| Lebanon | Law No. 44/2015 on AML; Beirut Bar Association KYC guidelines; heightened vigilance given FATF grey-list periods |
| France | Loi Sapin II transparency obligations for certain entities; Conseil National des Barreaux rules on client identification; TRACFIN reporting |
| UK | Solicitors Regulation Authority AML guidance; full source-of-funds verification required; "verify, not rely" standard |

## Common mistakes

- **Incomplete UBO identification**: firms often stop at the first layer of corporate ownership. A three-tier holding structure with a BVI parent may ultimately be owned by a sanctioned individual. Go to the natural-person beneficial owner.
- **No source of funds for retainer**: collecting a retainer without a source-of-funds declaration is an AML compliance gap in virtually every jurisdiction covered.
- **Cash retainers**: do not accept cash retainers above applicable thresholds (USD 3,000 in many MENA markets; lower thresholds in EU/UK).
- **Inadequate PEP screening**: "PEP" includes family members and close associates, not just the individual — the scope is wider than most intake forms capture.
- **Skipping entity intake for single-member LLCs**: a sole-owner LLC is functionally the same as an individual for AML purposes; apply both sections.

## Related skills

- [[efirm-conflict-check]]
- [[efirm-engagement-letter-draft]]
- [[efirm-matter-creation-flow]]
- [[efirm-fee-quote-builder]]
- [[research-sanctions-screening]]
