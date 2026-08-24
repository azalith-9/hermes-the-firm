---
name: import-nil-contract-analysis-samir-patel
description: Use when migrating the Samir Patel NIL (Name, Image, and Likeness) contract analysis methodology into the mini-hermes-the-firm format. The adapter maps NIL deal analysis logic — athlete/influencer rights, exclusivity windows, royalty structures, brand-alignment constraints, and termination triggers — into the standard skill model. Relevant for sports law, talent representation, and influencer-marketing contexts across MENA and international markets.
license: MIT
metadata: " id: import.nil-contract-analysis-samir-patel category: import jurisdictions: [UAE, US, UK, __multi__] priority: P3 intent: [__import__, nil, sports-law, name-image-likeness, contract-analysis, migration] related: [import-contract-review-anthropic, import-tech-contract-negotiation-patrick-munro, import-nda-review-jamie-tso, review-contract-generic] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Registered as a flat plugin skill.
-->


# Import: NIL Contract Analysis (Samir Patel)

## What it does

This import adapter migrates a **NIL (Name, Image, and Likeness) contract analysis skill modelled on the Samir Patel methodology** into the `mini-hermes-the-firm` standard format. NIL contracts govern how athletes, entertainers, and influencers monetise their personal brand: the right to use their name, image, likeness, and persona in commercial contexts.

NIL law originated in US collegiate sports but the underlying legal framework — rights of publicity, personality rights, image rights — applies globally. In MENA, athlete and influencer agreements are increasingly common, particularly in UAE and Saudi Arabia where major sports investments (LIV Golf, Newcastle United, Formula E, esports) have created a significant NIL market.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `contract_type` | Legacy `type` | `endorsement_deal` |
| `talent_category` | Legacy `talent` | `athlete` |
| `exclusivity_check` | Legacy `check_exclusivity` boolean | `true` |
| `royalty_structure_check` | Legacy `check_royalties` boolean | `true` |
| `term_check` | Legacy `check_term` boolean | `true` |
| `morals_clause_check` | Legacy `check_morals` boolean | `true` |
| `image_rights_scope` | Legacy `image_scope` | `full` |
| `governing_law` | Legacy `governing_law` | `__multi__` |
| `output_format` | Legacy `format` | `deal_analysis_memo` |

## Dry-run preview

```
IMPORT PREVIEW — nil-contract-analysis-samir-patel
Source shape    : NIL contract analysis (Patel methodology)
Contract type   : endorsement_deal
Talent          : athlete
Exclusivity     : checked
Royalty structure: checked
Term            : checked
Morals clause   : checked
Image rights    : full scope
Output          : deal_analysis_memo
```

## NIL contract review checklist (post-import)

### 1. Grant of rights
- Scope of NIL rights granted: name, image, likeness, voice, signature, biography?
- Media channels covered: digital, social, broadcast, print, out-of-home?
- Geographic scope: global, regional, country-specific?
- Duration: fixed term, event-tied, or perpetual?

### 2. Exclusivity
- Category exclusivity: is the talent restricted from competing brand deals in the same product category?
- Sub-category carve-outs: are there permitted competing endorsements below a revenue threshold?
- Brand alignment clauses: does the agreement require pre-approval of other endorsements?

### 3. Compensation structure
- Flat fee vs royalty vs hybrid
- Royalty calculation base: net revenue, gross revenue, net sales?
- Royalty rate: is it competitive for the talent category and market?
- Guaranteed minimums and escalators
- Payment milestones and currency
- Late-payment interest rate (check for Shariah-compliance in KSA/UAE contexts)

### 4. Morals / conduct clause
- Trigger events: criminal conviction, public scandal, regulatory sanction?
- Who decides? Unilateral brand discretion is common but highly unfavourable for talent
- Right to cure before termination?
- Consequences: suspension vs termination; repayment of advances?

### 5. Approval rights
- Content approval: does talent have right to approve creative materials featuring their NIL?
- Social media obligations: required posts, approved language, disclosure compliance (#ad, #sponsored per FTC guidelines and UAE IAA standards)?

### 6. Termination
- For cause triggers
- Convenience termination (with what notice and compensation?)
- Post-termination sell-off period for existing inventory

### 7. Image rights ownership
- Who retains IP in photographs, footage, and creative assets produced under the agreement?
- Work-for-hire vs licence-back structure?

## MENA jurisdictional notes

- **UAE**: personality rights are protected under UAE Federal Law on Media (and sector-specific regulations for sports); foreign athletes in UAE should verify visa/residency coupling does not constrain endorsement activities.
- **KSA**: Saudi General Entertainment Authority (GEA) governs entertainment and sports events; all endorsement content must comply with Saudi content standards.
- **Lebanon**: right of publicity not specifically codified; protection through copyright law and general tort principles.
- **Cross-border**: if the brand is global but the talent is in MENA, specify which national law governs image-rights usage in each territory.

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `nil_law_not_applicable` | Talent outside US collegiate system | Reframe as "image rights agreement"; same analysis applies |
| `morals_clause_overbroad` | Unilateral brand discretion with no standard | Flag as HIGH risk; recommend objective standard + cure right |
| `royalty_base_unclear` | Contract silent on calculation base | Flag as MEDIUM risk; recommend explicit definition |
| `exclusivity_scope_infinite` | All categories, global, perpetual exclusivity | Flag as HIGH risk for talent; recommend time-limited category lock |

## Related skills

- [[import-contract-review-anthropic]]
- [[import-tech-contract-negotiation-patrick-munro]]
- [[import-nda-review-jamie-tso]]
- [[review-contract-generic]]
- [[import-vendor-due-diligence-patrick-munro]]
