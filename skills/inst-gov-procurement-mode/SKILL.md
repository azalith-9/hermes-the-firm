---
name: inst-gov-procurement-mode
description: Use when a law firm, legal tech vendor, or legal AI platform is responding to a government Request for Proposal (RFP) or Request for Quotation (RFQ), completing a security questionnaire, preparing compliance attestations, or drafting bid pricing for a public-sector legal services or legal technology contract. Covers MENA public procurement frameworks (KSA, UAE, LB, EG) as well as standard international procurement requirements. Activates document-generation mode for procurement-specific outputs including reference letters, attestations, and multi-year pricing models.
license: MIT
metadata: " id: inst.gov-procurement-mode category: inst jurisdictions: [KSA, UAE, LB, EG, GCC, __multi__] priority: P1 intent: [__inst__, government-procurement, RFP, RFQ, bid, compliance, public-sector] related: [inst-ksa-moj-integration, inst-uae-moj-integration, draft-service-agreement-gov, kb-ksa-government-tenders] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'inst'.
Registered as a flat plugin skill.
-->


# Inst — Government Procurement Mode

## Purpose

Government procurement of legal services and legal technology follows specialized rules across MENA jurisdictions. This skill activates a structured operating mode for preparing, reviewing, and submitting government bid packages — covering RFP/RFQ responses, security and compliance questionnaires, attestation letters, customer references, and bid pricing strategies.

---

## When to use this

- A law firm is bidding on a government legal services panel tender (KSA Ministry panels, UAE federal panels, Lebanese government retainers)
- A legal AI vendor (including Louis/HAQQ) is responding to a government IT or professional services procurement
- A user needs to complete a security questionnaire from a government agency
- A user is preparing a compliance attestation (ISO 27001, SOC 2, GDPR/PDPL equivalents, Najiz-compatible data standards)
- A user is drafting a reference customer letter for inclusion in a government bid
- A user needs to model annual vs multi-year pricing for a public-sector engagement

---

## Inputs

| Input | Required | Notes |
|---|---|---|
| Jurisdiction | Yes | Determines procurement law framework |
| Procurement type | Yes | Legal services / IT / professional services |
| Contracting authority | Yes | Ministry, court, regulator, municipality |
| Scope of services | Yes | What is being procured |
| Evaluation criteria | If available | Price/quality split; local content requirements |
| Incumbent vendor | Optional | Affects pricing strategy |
| Security classification | Optional | Public / restricted / confidential |

---

## Document types

### 1. RFP / RFQ response template
Structure for a full bid response:
1. Executive summary (1-2 pages) — tailored to agency's stated priorities
2. Technical proposal — approach, methodology, team qualifications
3. Relevant experience — prior government work, case studies (anonymized if required)
4. Staffing plan — named leads, CVs, licensing confirmations
5. Compliance section — local content %, Saudization/Emiratization rates, SME status
6. Commercial proposal — pricing schedule (see below)
7. Annexes — certifications, bar registrations, insurance certificates

### 2. Security questionnaire
Common government security questions and standard compliant responses:
- Data residency (does data leave the country?)
- Encryption standards (at rest: AES-256; in transit: TLS 1.2+)
- Access control (RBAC, MFA, audit logs)
- Incident response (SLA, notification timelines — PDPL Art. 24 / UAE Data Protection Law)
- Sub-processor list (cloud providers, APIs used)
- Penetration testing cadence

### 3. Compliance attestations
- ISO 27001 certification status
- SOC 2 Type II report availability
- Compliance with jurisdiction-specific laws:
  - **KSA**: National Cybersecurity Authority (NCA) Essential Controls (ECC-1:2018); PDPL (Personal Data Protection Law 2021)
  - **UAE**: UAE Information Assurance Standards; UAE PDPL (Federal Decree-Law No. 45 of 2021)
  - **LB**: No dedicated PDPL yet (draft circulating); apply GDPR standard by analogy for international tenders
  - **EG**: Law No. 151 of 2020 (Personal Data Protection)

### 4. Reference customer letters
- Format: on official letterhead, addressed to the contracting authority
- Content: scope of work performed, duration, volume, satisfaction statement, contact details
- Caution: obtain client's explicit consent; check NDA scope before referencing government matters

### 5. Bid pricing strategies

#### Annual vs multi-year
| Model | Pros | Cons | Best for |
|---|---|---|---|
| Fixed annual | Simple; easy to budget | No volume discount lever | Short tender cycles |
| Multi-year with escalation | Predictable; CPI escalator protects margin | Locked in if scope grows | 3-5 year panels |
| Tiered / volume | Wins on cost score; scales | Complex to model | High-volume matters |
| Time-and-materials cap | Flexible for unknown scope | Risk of over-run | Regulatory/advisory |
| Retainer + success fee | Aligns incentives | Uncommon in gov; scrutiny | Litigation panels |

**MENA-specific note**: KSA and UAE government tenders frequently require a **local content percentage** declaration (Nitaqat in KSA; In-Country Value / ICV in UAE). Price models must demonstrate local staff ratios.

---

## Jurisdictional procurement frameworks

| Jurisdiction | Framework | Key rules |
|---|---|---|
| KSA | Government Tenders and Procurement Law (Royal Decree M/128 of 2019) | e-platform Etimad; local content; Saudization percentage declared |
| UAE (federal) | Federal Law No. 6 of 2018 on Public Procurement | e-GP platform; ICV certificate required; SME preference |
| UAE (DIFC/ADGM) | DIFC/ADGM procurement policies (common-law framework) | Less prescriptive; FIDIC-based contracts common |
| LB | Law No. 244 of 2000 on Public Tenders | Central Tender Board (CTB); paper + digital; post-2019 crisis has affected public procurement activity |
| EG | Law No. 182 of 2018 on Public Procurement | Monaa3sat platform; local + foreign supplier rules; 10% price preference for domestic |

---

## Common mistakes

- **Generic bids**: government evaluators score differentiation — always reference the agency's specific mandate and language from the tender documents
- **Missing local content declaration**: non-compliance disqualifies bids in KSA and UAE
- **Security questionnaire gaps**: leaving fields blank fails compliance scoring — provide "Not Applicable / Reason" rather than leaving empty
- **Pricing arithmetic errors**: multi-year models must reconcile line items — generate pricing tables in structured format and verify totals
- **Over-promising SLAs**: government contracts have penalty clauses; propose realistic SLAs with cure periods

---

## Related skills

- [[inst-ksa-moj-integration]]
- [[inst-uae-moj-integration]]
- [[draft-service-agreement-gov]]
- [[kb-ksa-government-tenders]]
- [[kb-uae-procurement-law]]
