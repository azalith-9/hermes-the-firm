---
name: tool-currency-converter
description: Use when converting between currencies for damages calculations, contract valuations, or cross-border legal matters. Covers spot and historical rates for USD, EUR, GBP, AED, SAR, LBP, KWD, QAR, BHD, OMR, EGP, and major global currencies. Includes a critical Lebanese Pound caveat on the multi-rate environment (official BDL vs Sayrafa vs parallel) and guidance on pinning a specific FX rate for litigation use.
license: MIT
metadata: " id: tool.currency-converter category: tool jurisdictions: [__multi__] priority: P2 intent: [calculator, currency] related: [tool-calculator-statutory-interest, tool-calculator-end-of-service-gratuity, tool-calculator-stamp-duty-tax, research-damages-quantification] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Tool — Currency Converter

## What it does

Converts amounts between currencies at spot or historical rates, with particular awareness of MENA currencies and the special complications of the Lebanese Pound (LBP) multi-rate environment. Essential for damages quantification, cross-border contract valuations, and tax calculations in mixed-currency matters.

## Setup / auth

- **Spot rates:** Use a reliable FX data provider (e.g., Open Exchange Rates, Fixer.io, or ECB for EUR base). Always record the source and timestamp in the output.
- **Historical rates:** Most FX providers offer historical rate APIs going back 10–20+ years. Essential for damages "as of" a specific past date.
- **LBP special source:** For Lebanese Pound rates, use BDL (Banque du Liban) official rate. Do not rely on generic FX APIs which may return outdated or inaccurate LBP rates.

## Supported currencies (primary MENA set)

| Currency | Code | Peg status |
|---|---|---|
| UAE Dirham | AED | Pegged to USD at 3.6725 |
| Saudi Riyal | SAR | Pegged to USD at 3.75 |
| Kuwaiti Dinar | KWD | Pegged to currency basket; typically ~3.25–3.30 USD/KWD |
| Qatari Riyal | QAR | Pegged to USD at 3.64 |
| Bahraini Dinar | BHD | Pegged to USD at 0.376 |
| Omani Rial | OMR | Pegged to USD at 0.385 |
| Egyptian Pound | EGP | Managed float; significant devaluation since 2022 — always use current/date-specific rate |
| Lebanese Pound | LBP | Complex — see dedicated section below |
| US Dollar | USD | Base reserve currency |
| Euro | EUR | Floating |
| British Pound | GBP | Floating |
| Japanese Yen | JPY | Floating |
| Chinese Yuan | CNY | Managed |

## Inputs

| Field | Type | Required | Notes |
|---|---|---|---|
| `from` | string | Yes | ISO 4217 currency code |
| `to` | string | Yes | ISO 4217 currency code |
| `amount` | number | Yes | Amount to convert |
| `asOfDate` | ISO date | No | Historical rate date; defaults to today (spot) |
| `rateSource` | string | No | Preferred source (BDL, ECB, OECD, etc.) — overrides default |

## Output schema

```json
{
  "from": "USD",
  "to": "AED",
  "amount": 100000,
  "asOfDate": "2026-05-14",
  "rateUsed": 3.6725,
  "rateSource": "AED/USD peg (fixed)",
  "converted": 367250,
  "advisoryFlags": []
}
```

```json
{
  "from": "LBP",
  "to": "USD",
  "amount": 1000000000,
  "asOfDate": "2026-05-14",
  "rateUsed": 89500,
  "rateSource": "BDL official rate (post-Feb 2023 unification)",
  "converted": 11173.18,
  "advisoryFlags": [
    "LBP: Multiple rates exist. BDL official rate used (LBP 89,500/USD as of Q1 2026 — verify current BDL circular). For pre-2023 contracts, see LBP historical caveat below."
  ]
}
```

## Lebanese Pound — critical caveats

The Lebanese Pound is one of the most legally complex currency situations globally. Three rates have coexisted:

| Rate | Status | Notes |
|---|---|---|
| **BDL official** | Primary rate; unified in Feb 2023 at ~LBP 15,000/USD, subsequently further devalued | Louis defaults to this for all calculations unless instructed otherwise |
| **Sayrafa platform rate** | BDL's managed market rate; typically different from official | Relevant for some commercial transactions 2021–2023 |
| **Parallel (black) market rate** | Informal; significantly higher than official | Used in practice but not legally recognised; courts have inconsistently handled this |

**Pre-2019 contracts denominated in "LBP":** These were entered into when LBP was pegged at ~LBP 1,507/USD. Post-2019 devaluation, parties dispute which rate applies to discharge obligations. Lebanese courts have not uniformly resolved this. For any pre-2019 LBP contract, flag that the conversion rate requires expert testimony or court determination — do not present a conversion as settled.

**Post-Feb 2023:** BDL unified the official and Sayrafa rates. Current official rate is the appropriate default for most calculations from this date forward.

## FX pinning for litigation

In litigation, a single FX rate must be fixed ("pinned") for the damages calculation period. Best practices:
- **Date of loss:** Most common approach — use the FX rate on the date the loss occurred.
- **Date of judgment:** Sometimes ordered by courts (particularly in DIFC/ADGM/UK proceedings).
- **Average over the period:** Used for claims accruing over time (e.g., lost profits across 12 months).
- Always cite the FX rate and source in the pleadings or expert report.

## Permissions & safety

- Always surface the source and timestamp of the rate used; never present a conversion as "exact" without noting that live rates fluctuate.
- For pegged currencies (AED, SAR, QAR, BHD, OMR), note the peg — the conversion is deterministic.
- For EGP, note that the rate may have moved significantly since the user's reference date.
- Do not use third-party FX data without confirming the provider's data-freshness SLA.

## Related skills

- [[tool-calculator-statutory-interest]]
- [[tool-calculator-end-of-service-gratuity]]
- [[tool-calculator-stamp-duty-tax]]
- [[research-damages-quantification]]
