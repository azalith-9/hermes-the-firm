---
name: wiki-fundraising
description: Use when discussing startup fundraising strategy, instrument mechanics, or investor dynamics for a legal-AI or MENA-focused startup. Covers the full capital stack from pre-seed through Series E, SAFEs and convertible notes, term sheet mechanics, dilution modelling, valuation methodologies, and runway management. Also covers the specific dynamics of raising capital for legal-AI companies in MENA markets. Reach for this skill when the user asks about fundraising, SAFEs, term sheets, dilution, or investor strategy.
license: MIT
metadata: " id: wiki.fundraising category: wiki jurisdictions: [UAE, KSA, LB, US, UK, __multi__] priority: P3 intent: [__wiki__, fundraising, SAFE, term-sheet, dilution, venture-capital] related: [wiki-finance, wiki-market, wiki-pricing, wiki-growth, wiki-haqq-product] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Startup Fundraising: Pre-Seed to Series E

## Scope

This pack covers the mechanics, strategy, and MENA-specific considerations of startup fundraising from first money in through growth-stage rounds. It is aimed at founders and legal counsel working on venture financings, with particular attention to legal-AI and MENA-context nuances.

---

## Funding stage overview

| Stage | Typical size | Typical instrument | Lead investor type |
|---|---|---|---|
| Pre-seed | $150 k–$1 M | SAFE / convertible note | Angels, pre-seed funds, accelerators |
| Seed | $1 M–$5 M | Priced round or SAFE | Seed funds, strategic angels |
| Series A | $5 M–$20 M | Priced equity round | Early-stage VCs |
| Series B | $15 M–$50 M | Priced equity round | Growth VCs |
| Series C+ | $50 M+ | Priced equity round | Growth / late-stage VCs, crossover funds |

MENA-specific note: Sovereign wealth fund (SWF) participation is common at Series B and above (Mubadala, ADQ, PIF, Mumtalakat). SWF co-investments may come with special terms (information rights, board observer, preferred allocation in future rounds). Founders should review these carefully; SWF terms are often less standardised than typical VC terms.

---

## SAFEs and convertible notes

### SAFE (Simple Agreement for Future Equity)

The Y Combinator SAFE is the dominant pre-seed instrument in US-incorporated startups and is widely used by MENA startups incorporated in ADGM or DIFC (which use English-law structures).

**Key SAFE variants:**
- **Valuation cap only** — converts at the lower of: cap ÷ shares, or next-round price. Most founder-friendly.
- **Discount only** — converts at next-round price minus a discount (typically 15–25%).
- **Cap and discount** — takes the better of the two; more investor-friendly.
- **MFN (most-favoured nation)** — no cap/discount, but investor gets the best terms of any subsequent SAFE issued before conversion. Used when valuation is truly unknown.

**SAFE mathematics:**
```
Post-money SAFE conversion shares = Investment ÷ Cap (if cap applies)

Dilution effect: SAFEs dilute existing shareholders at conversion, not at issuance.
Founders often underestimate total dilution from stacked pre-seed SAFEs.
```

Model the cap table through multiple SAFE conversions before issuing. A $500 k SAFE at a $5 M cap and a $1 M SAFE at an $8 M cap followed by a $4 M Series A at a $14 M pre-money will show materially more dilution than founders expect.

### Convertible note vs SAFE

| Feature | SAFE | Convertible note |
|---|---|---|
| Debt instrument | No | Yes (accrues interest, has maturity date) |
| Maturity default risk | None | Yes — investor can demand repayment at maturity |
| Interest rate | N/A | Typically 5–8% per year |
| Jurisdiction flexibility | High (English law friendly) | Higher for jurisdictions that don't recognise SAFEs |
| Lebanon / KSA legal systems | Use carefully — civil law may not recognise US SAFE structure cleanly | Better fit, but get local counsel sign-off |

In civil-law MENA jurisdictions (Lebanon, Egypt, onshore UAE, onshore KSA), the SAFE as written under New York or English law may not be enforceable without local adaptation. Founders should use ADGM/DIFC-incorporated holding entities for SAFE issuance and keep the operating entity onshore.

---

## Term sheet mechanics

A term sheet for a priced round covers:

### Economic terms
- **Pre-money valuation** — agreed value before new money comes in. Post-money = pre-money + investment.
- **Option pool** — VCs typically require a 10–20% option pool *before* the investment, which dilutes existing shareholders (not the new investor). Always negotiate whether the pool shuffle is pre- or post-money.
- **Liquidation preference** — most common is 1x non-participating preferred. Watch for 2x or participating preferred in down markets; they significantly penalise founders in M&A below a high exit price.
- **Anti-dilution** — broad-based weighted average is market standard. Full ratchet is extremely punitive; rarely seen outside distressed situations.
- **Dividends** — typically non-cumulative preferred dividend; in practice rarely paid.

### Control terms
- **Board composition** — typical Series A: 2 founder seats, 1 lead VC seat, 1–2 independents. Board composition is a key negotiation point.
- **Protective provisions** — veto rights for preferred shareholders on: new share issuances, M&A, debt above a threshold, changes to certificate of incorporation. Market standard; do not give broad veto rights over day-to-day operations.
- **Pro-rata rights** — investor's right to participate in future rounds to maintain ownership percentage. Standard for lead investors; watch for pro-rata rights in SAFEs (they are unusual but sometimes asked for).
- **Information rights** — quarterly financials, annual audited accounts, monthly management accounts. Standard.

---

## Dilution management

**Key principle:** track ownership on a fully diluted basis at all times, including:
- Issued shares (common + preferred)
- Option pool (issued + unissued)
- SAFE / convertible note potential shares (at various conversion scenarios)
- Warrants

Use a cap table tool (Carta, Pulley, or a careful spreadsheet). Re-run the cap table model before every round.

**MENA-specific:** nominee structures (using a local nominee to hold shares on behalf of a foreign-owned entity) are common in onshore UAE/KSA incorporations. These create a parallel layer of beneficial ownership documentation that must be reflected accurately in the cap table and disclosed to investors.

---

## Runway and fundraising timing

Standard rule: start fundraising when you have 6–9 months of runway remaining. The process takes 3–6 months from first meeting to close (longer in MENA where wire transfers and KYC on investors can add weeks).

**MENA fundraising timing considerations:**
- Avoid starting a raise process that will close during Ramadan (board approvals and wire transfers slow significantly).
- UAE/KSA investors often summer in Europe; July–August is a slow fundraising month in the Gulf.
- Best windows: February–May and September–November.

---

## Investor types in MENA

| Type | Examples | Characteristics |
|---|---|---|
| Regional early-stage VCs | Wamda, BECO, Algebra Ventures, Flat6Labs | MENA market knowledge; smaller cheques |
| Gulf SWFs | Mubadala Ventures, PIF, ADQ, Mumtalakat | Large cheques; strategic alignment; longer process |
| International VCs with MENA presence | Sequoia India/Southeast Asia, Tiger, a16z | US-standard terms; need strong traction signal |
| Corporate VCs | Etisalat/e&, Saudi Telecom, Arab Bank | Strategic fit required; governance can be complex |
| Family offices | Numerous in UAE/KSA/Lebanon diaspora | Fast decisions; flexible terms; often no board seat |

---

## Legal documents in a round

The standard document set for a priced Series A in an ADGM/DIFC company:

1. Term sheet (non-binding except exclusivity and confidentiality)
2. Shareholders' Agreement (SHA) — governance, transfers, drag/tag, pre-emption
3. Articles of Association (AA) — constitutional document, incorporating SHA terms
4. Subscription Agreement — investment amount, representations and warranties
5. Disclosure Letter — schedules qualifying the representations
6. Cap table (certified)
7. Management / founder representations

For UAE onshore entities (LLC), the equivalent set must comply with UAE Commercial Companies Law; foreign ownership restrictions may apply (though these have largely been liberalised under the 2021 amendments to the Companies Law).

---

## Caveats & currency

Legal and regulatory requirements for foreign investment in MENA companies evolve frequently. The 2021 UAE Companies Law amendments significantly changed foreign ownership rules; KSA continues to liberalise its investment framework. Always obtain local legal counsel review of the final investment documents. SAFE templates are jurisdiction-specific; do not use a US SAFE for a DIFC entity without adapting it to ADGM/DIFC company law.

---

## Related skills

- [[wiki-finance]]
- [[wiki-market]]
- [[wiki-pricing]]
- [[wiki-growth]]
- [[wiki-haqq-product]]
