---
name: wiki-startup
description: Use when a user asks about startup operations, founding mechanics, early-stage fundraising, hiring at a startup, go-to-market strategy, or scaling challenges in the MENA context. Provides a reference on the full lifecycle from founding through growth, with MENA-specific legal and operational considerations for DIFC, ADGM, UAE-onshore, KSA, and Lebanese-based startups.
license: MIT
metadata: " id: wiki.startup category: wiki jurisdictions: [UAE, DIFC, ADGM, KSA, LB, __multi__] priority: P3 intent: [__wiki__, startup, founding, fundraising, gtm, scaling, MENA startup] related: [wiki-vc-startups, wiki-sales, wiki-strategy, workflow-startup-incorporation-pack, workflow-investment-round-closing-pack] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Registered as a flat plugin skill.
-->


# Startup Operations Reference

## Scope

This pack covers the legal and operational dimensions of startup lifecycle management from founding through fundraising, hiring, go-to-market, and scaling. It is oriented toward MENA founders and investors but draws on global best practices where applicable.

---

## Phase 1 — Founding

### Jurisdiction Choice

The first legal decision is where to incorporate. Key options:

| Jurisdiction | Best for | Key advantages | Key traps |
|-------------|---------|---------------|-----------|
| DIFC (Dubai) | Tech/VC-backed startups, fintech | English law, common-law courts, mature VC ecosystem, USD cap tables | Annual licensing fees; physical presence requirements |
| ADGM (Abu Dhabi) | Crypto/digital assets, asset management | Progressive digital assets framework (FSRA), flexible company forms | Newer ecosystem, fewer VCs physically present |
| Delaware (US) | US-bound startups, YC companies | Standard for US VC; NVCA docs; familiarity | Tax complexity for non-US founders; requires US presence |
| Singapore | Asia-Pacific reach | Strong IP regime, political stability, ASEAN gateway | Less direct relevance if clients/team are in MENA |
| UAE-onshore (mainland) | Local market operations | Lower cost than free zones; local government contracts | Requires UAE national partner or licensed distributor (some sectors) |
| KSA | KSA market access | Massive market; government procurement | Complex regulatory environment; Saudization requirements |
| Lebanon | Cost-efficient | Low cost; skilled tech talent | Currency instability; banking restrictions; political risk |

### Founder Agreements

Critical at founding; difficult to fix retroactively:
- **Co-founder equity split** — address early; document in writing; avoid equal splits among co-founders if roles differ significantly
- **Vesting schedules** — standard: 4-year vest, 1-year cliff; double-trigger acceleration for exits
- **IP assignment** — all IP created by founders before and during employment must be formally assigned to the company; courts will not presume assignment
- **83(b) election (US)** — for US-based founders with unvested shares, must be filed within 30 days of share issuance; missing this creates massive tax exposure
- **Founder employment agreements** — define role, salary (often deferred), non-compete, non-solicit

### Cap Table Fundamentals

- Issue shares at nominal value at founding; establish option pool (typically 10–15% pre-Series A)
- Use a cap table management tool (Carta, Pulley, or regional equivalent) from day one
- Avoid convertible notes / SAFEs for very early rounds without considering dilution impact
- Anti-dilution provisions and preference waterfall are VC-introduced later; founders must understand these before agreeing to them

---

## Phase 2 — Early-Stage Fundraising

### Fundraising Instruments

| Instrument | Stage | Key terms | Notes |
|------------|-------|-----------|-------|
| Friends & Family round | Pre-seed | Simple loan or SAFE | Keep simple; avoid complex terms early |
| SAFE (Simple Agreement for Future Equity) | Pre-seed / seed | Valuation cap, discount, MFN | Y Combinator standard; widely used globally |
| Convertible note | Seed | Interest rate, maturity, cap, discount | Has debt-like features (maturity date) |
| Priced equity (seed round) | Seed | Share class, pre-money valuation, rights | More expensive to document; needed for institutional investors |
| Series A | Series A | Lead investor, priced preferred, prorata rights | Standard institutional VC round |

### MENA Fundraising Sources

**Accelerators:**
- Hub71 (Abu Dhabi) — significant grants + investments
- DIFC Fintech Hive, FinTech Arabia
- Flat6Labs (multiple MENA cities)
- Wamda, Endeavor MENA

**Seed / Early-Stage Funds:**
- BECO Capital (UAE)
- MEVP (Lebanon/UAE)
- Shorooq Partners (UAE/KSA)
- Nuwa Capital (UAE)
- Vision Ventures (KSA)
- Wamda Capital

**Government and Sovereign Programs:**
- Mubadala Capital (UAE)
- Saudi Aramco Energy Ventures (SAEV)
- Saudi Venture Capital Company (SVC)
- Lebanon-based EU programs (post-crisis, smaller scale)

### Term Sheet Negotiation — Founder Watch Points

- **Liquidation preference** — 1× non-participating preferred is founder-friendly; 2× or participating preferred is aggressive
- **Anti-dilution** — broad-based weighted-average is standard; full ratchet is extremely investor-friendly
- **Board composition** — at Series A, standard is 2 founder seats, 1 lead investor seat, 1–2 independent; founders should negotiate to keep majority control until Series B
- **Drag-along provisions** — ensure reasonable threshold (majority of all shares, not just preferred) to avoid minority investor blocking an exit
- **Exclusivity** — typical 30–45 days; avoid longer without strong reason

---

## Phase 3 — Hiring

### First Hires

- Co-founder hires vs. employee hires: employees have statutory protections; co-founders do not (treat early team with vesting + agreements, not just promises)
- For MENA hires: employment law compliance is mandatory from day one (MOHRE registration in UAE, NSSF in Lebanon, GOSI in KSA)
- Work permits for non-citizens are employer-sponsored in UAE and KSA — this creates termination complexity (visa cancellation must accompany termination)

### Employment vs. Contractor

Misclassification risk:
- UAE: unlimited employment contracts are the default; gig/contractor arrangements are scrutinized
- KSA: contractors under Sharia law may have employment-like rights if the relationship looks like employment
- Use genuine contractor relationships only for project-based work with multiple clients; full-time exclusive arrangements are de facto employment

### Equity for Employees

- Employee Stock Option Plans (ESOPs) are standard; use established template in the applicable jurisdiction
- DIFC and ADGM have clear ESOP regimes
- UAE mainland ESOP enforceability is less settled — structure carefully
- KSA: cash-settled phantom equity or bonus plans are more common than equity grants

---

## Phase 4 — GTM (Go-to-Market)

### Product-Led Growth vs. Sales-Led

| Approach | Signals | MENA fit |
|----------|---------|---------|
| PLG | Viral, self-serve, low ACV, API product | Works for consumer and developer tools; limited for B2B legal/enterprise |
| Sales-led | High ACV, enterprise buyers, procurement | Standard for legal-tech, fintech, government-adjacent |
| Community-led | Network effects, developer ecosystem | Emerging in MENA; works for open-source and developer tools |

### MENA GTM Considerations

- **Language**: Arabic UI and support is essential for KSA domestic market; bilingual (Arabic/English) for UAE enterprise
- **Government as a customer**: the largest enterprise buyers in UAE and KSA are government entities (ministries, sovereign funds, national banks); government sales cycles are 12–24 months with procurement requirements
- **Relationships over marketing**: MENA enterprise sales are heavily relationship-driven; conferences, chambers of commerce, and warm introductions outperform cold outreach
- **Channel partners**: consider distribution through local system integrators or consulting firms who already have government and enterprise relationships

---

## Phase 5 — Scaling

### Series A and Beyond

Key changes at Series A:
- Institutional investors demand quarterly board meetings, financial reporting, audited accounts
- HR formalization: employee handbook, performance management, compensation bands
- Finance formalization: ERP system, finance controller hire, proper treasury management
- Legal compliance: data privacy programs, IP audit, regulatory license review as the product expands to new markets

### Common Scaling Pitfalls

- **Founder dependence**: single founder holding all customer relationships is a risk; institutionalize customer success early
- **Hiring too fast**: over-hiring at seed stage before product-market fit leads to cash crises; maintain at least 18 months runway at all times
- **Entering new markets too early**: MENA market penetration is still shallow in most sectors; dominate one geography before expanding
- **Ignoring compliance**: regulatory risk accumulates as the company grows; a compliance gap at seed becomes a material liability at Series A/B

---

## How to Use This Pack

Reference when:
- Advising a MENA founder on incorporation and early structuring
- Reviewing a term sheet or SAFE for a MENA startup
- Conducting legal due diligence on an early-stage company
- Designing a startup's employment and equity framework

---

## Caveats & Currency

Startup ecosystem data (fund names, accelerator programs, regulatory frameworks) evolves rapidly in MENA. Verify current fund activity, government program terms, and regulatory changes before advising. The DIFC and ADGM update their company law and employment regulations periodically.

## Related Skills

- [[wiki-vc-startups]]
- [[wiki-sales]]
- [[wiki-strategy]]
- [[workflow-startup-incorporation-pack]]
- [[workflow-investment-round-closing-pack]]
- [[workflow-hire-employee-pack]]
- [[draft-founders-agreement]]
- [[draft-vesting-schedule]]
