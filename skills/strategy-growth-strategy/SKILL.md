---
name: strategy-growth-strategy
description: Use when planning Louis's go-to-market motion, channel investment decisions, or growth experiments. Covers the dual PLG bottom-up and ABM top-down strategy, MENA distribution channels (bar associations, universities, partner ecosystem), and the individual-to-team conversion funnel. Internal use only.
license: MIT
metadata: " id: strategy.growth-strategy category: strategy jurisdictions: [__multi__] priority: P3 intent: [__internal__] related: [strategy-customers, strategy-competitors, strategy-markets, strategy-fundraising, strategy-partnerships] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'strategy'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Strategy — Growth Strategy

## Purpose

This skill defines Louis's growth playbook. Use it when allocating marketing budget, designing acquisition experiments, planning partnership outreach, or prioritising product features that support conversion.

## Dual-motion architecture

Louis runs two parallel GTM motions that feed each other:

### Motion 1 — PLG (Product-Led Growth), bottom-up

**Principle:** Free tools and free-tier access create individual lawyer adoption. Individual users prove value, then trigger team or firm upgrades.

**Funnel:**
```
Anonymous user
  → discovers free tool (EOSG calculator, deadline calculator, NDA first-draft)
  → hits usage limit
  → signs up free
  → experiences full skill set on free tier
  → promotes to colleagues / firm IT
  → firm upgrade (multi-seat)
```

**Key lever:** The free tools must deliver standalone value before asking for an account. A lawyer who runs the EOSG calculator and gets the right answer in 30 seconds is already sold on the product.

**Conversion triggers:**
- Usage-limit CTA (inline, not interruptive — see [[site-tools-router]])
- Post-task save prompt: "Save to your matter — sign up free"
- Export gate: export to DOCX / PDF requires free account

---

### Motion 2 — ABM (Account-Based Marketing), top-down

**Principle:** Direct outreach to the top-50 MENA law firms and the GC functions of the 50 largest UAE/KSA enterprises. Longer cycle; higher ACV; requires legal-industry-credentialed sales team.

**Target accounts:**
- UAE: Hadef & Partners, Al Tamimi & Co., Clifford Chance DIFC, Baker McKenzie DIFC, Al Suwaidi & Co.
- KSA: Al-Jadaan, Abdulaziz Al Ajlan, Clyde & Co Riyadh, White & Case Riyadh
- Lebanon: Frangieh & Frayha, Obeid Law, Ghosain & Zgheib (adapt list as market evolves)
- In-house: Large UAE telcos, banks, real estate groups (Aldar, ADNOC legal)

**Outreach:** Conference presence (IBA, MENA Legal Awards, Arab Legal Forum), managing-partner direct outreach, MENA bar-association co-sponsorships.

---

## Distribution channels

### Bar associations

Partner with national bar associations in UAE (Abu Dhabi Bar Association, Dubai Legal Affairs Department), KSA (Saudi Bar Association), and Lebanon (Bar Association of Beirut and Tripoli) for:
- CLE / CPD credit for Louis training sessions
- Bulk licensing at bar-association-negotiated rates
- Endorsement as a bar-approved AI tool (key trust signal in a compliance-conscious market)

### Universities

Priority targets: UAE University, American University of Sharjah, King Abdulaziz University (KSA), American University of Beirut (law faculty), Lebanese American University.

Model: free student access; faculty pilot for legal research; annual licensing for law-school clinics. Students graduate → become practitioners → bring Louis to their firm (long-tail PLG).

### Partner ecosystem

Referral partners who control access to the target ICP:
- Legal practice management software vendors (Clio regional, Smokeball, or local equivalents)
- Matter management SaaS with MENA footprint
- Big-4 legal advisory practices in UAE/KSA
- Legal recruitment firms (candidates who can recommend tools to firms)

## Growth experiments to run

| Experiment | Hypothesis | Metric |
|---|---|---|
| EOSG calculator as standalone landing page with no sign-in | Reduces friction → higher tool completion rate | Tool completion rate, downstream sign-up |
| Arabic-first onboarding for solo practitioners | Arabic UI reduces drop-off in LB/KSA solo segment | Onboarding completion by language |
| Bar-association email blast + 3-month free trial | Association endorsement drives higher trust and conversion | Sign-up rate per association |
| Webinar series: "AI for MENA Lawyers" | Thought-leadership drives inbound | Registrations → trial → conversion |

## North-star metrics

- **Weekly active lawyers** (individual users who run at least one task/week)
- **Firm adoption rate** (individual users who convert their firm to a multi-seat plan)
- **Free-to-paid conversion** (target: >5% within 30 days of sign-up for PLG users)
- **Churn** (target: <5% monthly for firm accounts)

## Related skills

- [[strategy-customers]]
- [[strategy-competitors]]
- [[strategy-markets]]
- [[strategy-fundraising]]
- [[strategy-partnerships]]
- [[site-tools-router]]
