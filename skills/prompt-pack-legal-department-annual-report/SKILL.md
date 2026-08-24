---
name: prompt-pack-legal-department-annual-report
description: Use when a General Counsel or legal operations team needs to draft an annual report for the legal department covering matter statistics, spend analysis, significant matters, risk management, operational improvements, diversity metrics, and strategic priorities. Applicable to in-house legal teams reporting to boards, CEOs, or audit committees across corporate sectors.
license: MIT
metadata: " id: prompt-pack.legal-department-annual-report category: prompt-pack practice_area: legal-ops-billing priority: P2 intent: [summarize, legal-department-annual-report] related: - prompt-pack-legal-department-kpi-dashboard - prompt-pack-legal-budget-forecast - prompt-pack-outside-counsel-guidelines - prompt-pack-matter-closing-procedure - prompt-pack-legal-invoice-review-checklist source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'prompt-pack'.
Registered as a flat plugin skill.
-->


# Legal Department Annual Report

## When to use this

Use this skill when the legal department needs to report to the board, CEO, CFO, or audit committee on the year's legal activities, spending, and strategic contribution. The annual report demonstrates legal department value, supports budget requests, and provides governance visibility.

Triggers:
- "Draft the legal department's annual report for fiscal year [year]."
- "I need to present to the board on what legal accomplished this year."
- "Compile our matter statistics and spend for the year-end review."

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Company name and reporting year | Names the report and scopes the period | Ask user |
| Matter statistics (volume by type) | Core quantitative evidence of workload | Ask user or note "data to be inserted" |
| Legal spend summary (internal + external) | Shows cost efficiency and budget adherence | Ask user |
| Significant matters highlights | Demonstrates legal impact and risk management | Ask user |
| Headcount and team structure | Shows resource allocation | Ask user |
| Strategic priorities for coming year | Forward-looking section for board engagement | Ask user |

## Optional inputs

- Diversity, equity, and inclusion metrics (workforce representation, outside counsel diversity data)
- Client satisfaction scores (internal survey results)
- Operational improvements delivered during the year
- Legal technology initiatives
- Key regulatory developments affecting the business

## Report structure

### Executive Summary (1–2 pages)
- Total matters handled: volume, year-over-year change
- Total legal spend: internal costs + external counsel fees, vs budget
- Top 3 legal achievements of the year
- Top 3 legal risks entering the new year
- Headcount summary

### Section 1: Matter Statistics
Present a table and brief narrative:

| Matter Type | Matters Opened | Matters Closed | Matters Carried Forward | Avg Cycle Time |
|---|---|---|---|---|
| Transactions / M&A | | | | |
| Contracts / Commercial | | | | |
| Employment | | | | |
| Litigation / Arbitration | | | | |
| Regulatory / Compliance | | | | |
| Real Estate | | | | |
| IP | | | | |
| **Total** | | | | |

Include trend commentary: are volumes increasing? Is cycle time improving?

### Section 2: Spend Analysis
- Total legal spend vs budget (waterfall chart recommended)
- Breakdown: internal staffing costs vs external counsel vs technology vs other
- External counsel: top 5 firms by spend, average blended hourly rate vs prior year
- Litigation and dispute resolution costs as a proportion of total spend
- Cost-per-matter metrics where calculable

### Section 3: Significant Matters
For each significant matter (typically the top 5–10 matters by strategic importance or cost):
- Matter name / description (redact if necessary for confidentiality)
- Jurisdiction(s)
- Status at year-end
- Business outcome / impact
- Legal fees incurred

### Section 4: Risk Management
- New laws and regulations that required internal response in the year
- Risk assessment updates (litigation reserve changes, regulatory risk flags)
- Proactive risk mitigation initiatives (compliance programs launched, policy updates)

### Section 5: Operational Improvements
- Contract turnaround time improvements
- Legal technology deployed (CLM, e-billing, AI tools)
- Process improvements (playbooks, standard forms introduced)
- Training delivered to business units

### Section 6: People and Diversity
- Headcount at year-start and year-end; promotions, departures
- Diversity metrics for legal team (if reported)
- Outside counsel diversity spend data (if tracked under guidelines)
- Training and professional development

### Section 7: Strategic Priorities for the Coming Year
- Major anticipated legal activities (M&A pipeline, regulatory filings, litigation)
- Resource requests (headcount, technology investment)
- Process transformation initiatives
- Key external risks (regulatory landscape, dispute exposure)

## Drafting standards

- Lead each section with a one-paragraph narrative summary before tables; boards read narratives, not just numbers.
- Use RAG (Red/Amber/Green) status indicators for litigation and compliance risks in the risk section.
- Be factual and precise: do not speculate on outcomes of pending matters.
- Keep the executive summary to two pages; the full report may be 10–20 pages plus annexes.
- Include a glossary of acronyms and legal ops terminology for non-lawyer board members.

## MENA-specific considerations

- **GCC in-house teams** reporting to holding-company boards: include country-by-country breakdown for UAE, KSA, Qatar, Bahrain operations where the legal team covers multi-jurisdictional matters.
- **Lebanon-based entities**: note currency/FX impact on spend figures; USD vs LBP cost allocation requires explanation.
- **Regulatory environment notes**: highlight significant legal developments in applicable jurisdictions (e.g., UAE data protection law, KSA VAT/Zakat changes, Egypt investment law amendments) that required legal department response.

## Common mistakes

- **All data, no narrative**: Tables without explanation leave boards unable to judge whether the department performed well.
- **Omitting outside counsel diversity data**: If the company has outside counsel guidelines with diversity requirements, the annual report is where compliance is measured.
- **Not connecting spend to value**: Report legal department outcomes (deals closed, disputes won, regulatory risks mitigated) to justify the cost.
- **Forgetting to redact sensitive matter details**: Annual reports may be distributed broadly; sensitive litigation strategy and privileged communications must be excluded.

## Related skills

- [[prompt-pack-legal-department-kpi-dashboard]]
- [[prompt-pack-legal-budget-forecast]]
- [[prompt-pack-outside-counsel-guidelines]]
- [[prompt-pack-matter-closing-procedure]]
- [[prompt-pack-legal-invoice-review-checklist]]
