---
name: feed-regulator-bulletins-mena
description: Use when the platform needs to surface official regulatory authority bulletins, circulars, and administrative guidance from MENA financial, commercial, and sectoral regulators to users. Covers UAE (CBUAE, SCA, VARA, MOHRE, DLD), KSA (SAMA, CMA, GAZT/ZATCA), Lebanon (BDL, CMA-LB), Egypt (CBE, FRA, EGX), and GCC equivalents. The primary compliance-monitoring feed for regulated-sector practitioners and in-house counsel.
license: MIT
metadata: " id: feed.regulator-bulletins-MENA category: feed jurisdictions: [UAE, KSA, LB, EG, QA, BH, KW, OM, DIFC, ADGM, GCC] priority: P3 intent: [__feed__, regulatory-monitoring, compliance, MENA, circulars] related: [feed-gazettes-watcher, feed-legal-news-mena, feed-case-law-new-publications, kb-financial-regulation-mena, heuristic-always-state-jurisdiction-first] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'feed'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Regulator Bulletins MENA Feed Surface

## Purpose

Regulatory circulars and bulletins issued by MENA supervisory authorities carry the force of compliance obligations for regulated entities. Unlike primary legislation (tracked by the gazettes watcher), regulatory bulletins are issued by specific sector regulators — central banks, capital market authorities, financial intelligence units, labor authorities, real estate regulators — and often require immediate compliance action.

This feed surface monitors the bulletin channels of the major MENA regulators and surfaces compliance-relevant items to practitioners based on their practice area, sector exposure, and jurisdiction profile.

## Monitored regulators and bulletin sources

### UAE
| Regulator | Scope | Bulletin channel |
|---|---|---|
| CBUAE (Central Bank UAE) | Banking, insurance, AML/CFT | Circulars portal |
| SCA (Securities and Commodities Authority) | Capital markets, funds, listed companies | Notices + circulars |
| VARA (Virtual Assets Regulatory Authority) | Crypto assets, VASPs | Rulebooks + guidance |
| MOHRE (Ministry of HR & Emiratisation) | Employment, Emiratisation quotas | Ministerial decisions |
| DLD (Dubai Land Department) | Real estate transactions | RERA circulars |
| HAAD / DHA | Healthcare regulation (Abu Dhabi / Dubai) | Bulletins |
| TDRA (Telecommunications & Digital Government Authority) | Data protection, telecoms | Guidance notes |

### DIFC / ADGM
| Regulator | Scope |
|---|---|
| DFSA (Dubai Financial Services Authority) | Financial services in DIFC |
| FSRA (Financial Services Regulatory Authority) | Financial services in ADGM |

### KSA
| Regulator | Scope |
|---|---|
| SAMA (Saudi Central Bank) | Banking, insurance, fintech |
| CMA (Capital Market Authority) | Capital markets, listed companies, funds |
| ZATCA (Zakat, Tax and Customs Authority) | Tax, VAT, customs |
| MHRSD (Ministry of HR & Social Development) | Labor, Saudization |
| GAZT / NCA | Cybersecurity (National Cybersecurity Authority) |

### Lebanon
| Regulator | Scope |
|---|---|
| BDL (Banque du Liban) | Banking, monetary, AML |
| CMA-LB (Capital Markets Authority Lebanon) | Capital markets (nascent) |
| ISS (Insurance Control Commission) | Insurance supervision |

### Egypt
| Regulator | Scope |
|---|---|
| CBE (Central Bank of Egypt) | Banking, monetary policy |
| FRA (Financial Regulatory Authority) | Non-banking financial sector |
| EGX (Egyptian Exchange) | Listed company obligations |
| NTRA (National Telecom Regulatory Authority) | Telecoms, data |

### Pan-GCC / international
- FATF (Financial Action Task Force) guidance (AML/CFT relevance)
- IOSCO guidance (capital markets)
- BIS / Basel Committee guidance (banking)

## Personalization logic

1. **Sector filter**: match regulators to the user's industry sector tags (banking, insurance, real estate, capital markets, crypto, employment, etc.).
2. **Jurisdiction filter**: only surface bulletins from regulators in the user's active jurisdictions.
3. **Urgency scoring**: bulletins with explicit compliance deadlines are scored "urgent" regardless of other filters; always surface within 24 hours of publication.
4. **Practice-area boost**: a banking/finance lawyer gets CBUAE and SAMA bulletins at high priority; an employment lawyer gets MOHRE and MHRSD at high priority.
5. **AML/CFT universal flag**: AML/CFT circulars are surfaced to all users with any UAE, KSA, or LB jurisdiction active, regardless of practice area, because of the cross-sector impact of these obligations.

## Output spec

```json
{
  "id": "bulletin-uuid",
  "regulator": "CBUAE",
  "jurisdiction": "UAE",
  "sector": "banking",
  "bulletin_type": "circular",
  "reference": "CBUAE/BSD/2025/05-001",
  "title": "Circular on Enhanced Customer Due Diligence for High-Risk Correspondent Banking",
  "summary": "Requires UAE-licensed banks to apply enhanced CDD measures for correspondent relationships with banks in jurisdictions on the FATF grey list. Effective 1 July 2025. Compliance gap analysis required within 60 days of issue.",
  "published_date": "2025-05-09",
  "compliance_deadline": "2025-07-01",
  "urgency": "high",
  "source_url": "https://...",
  "practice_areas": ["banking", "AML-CFT"],
  "relevance_score": 0.96
}
```

## Urgency tiers

| Urgency | Criteria | Alert mode |
|---|---|---|
| Critical | Compliance deadline < 30 days; immediate action required | In-app alert + push + email |
| High | Compliance deadline 30–90 days; new obligation | Feed item with banner |
| Medium | Guidance without hard deadline; best-practice update | Standard feed item |
| Low | Statistical report, speech, non-binding commentary | Low-priority feed item |

## Quality bar

- Compliance deadlines must be extracted and displayed exactly as stated in the bulletin. Do not infer deadlines.
- Bullet-point AI summaries of compliance requirements must use the same language as the regulator uses. Do not rephrase obligations in softer language.
- If the bulletin text is in Arabic only, AI-translate for the summary but mark clearly: "Summary translated from Arabic original — verify."
- Where a bulletin amends a prior bulletin, reference the prior bulletin by number.

## Failure modes

- **Regulator website restructuring** (very common in GCC): flag source as "parsing error" in ops; cache last known items; do not surface stale data beyond 7 days without disclosure.
- **Missing compliance deadline**: if no explicit deadline is stated, mark deadline field as "Consult bulletin — deadline not explicitly stated."
- **Duplicate bulletins**: some regulators re-issue circulars with minor numbering changes. Deduplicate by content similarity; show only the most recent version.

## Related skills

- [[feed-gazettes-watcher]]
- [[feed-legal-news-mena]]
- [[feed-case-law-new-publications]]
- [[kb-financial-regulation-mena]]
- [[heuristic-always-state-jurisdiction-first]]
