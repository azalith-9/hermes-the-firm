---
name: router-practice-area-detector
description: Use to classify the primary legal practice area of an incoming request from a defined 22-label taxonomy. Labels include corporate, ip, employment, real-estate, m-and-a, litigation, data-privacy, arbitration, shariah-finance, and others. Uses keyword signals for high-confidence classification, falls back to admin with a clarifying-question trigger at confidence below 0.50. Output consumed by skill selection, persona selection, and knowledge retrieval routing.
license: MIT
metadata: " id: router.practice-area-detector category: router priority: P0 intent: [__router__] related: [router-intent-detection, router-jurisdiction-detector, router-complexity-grader, router-persona-selector, router-tool-selector] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'router'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Practice Area Detector

## Purpose

Practice area detection determines which body of law is relevant to the request. This drives:

1. **Skill selection**: the practice area narrows the candidate skills from hundreds to a manageable shortlist
2. **Knowledge routing**: RAG retrieval is filtered to the relevant corpus (corporate law library vs. employment law vs. real estate)
3. **Persona selection**: certain practice areas map more naturally to certain personas (investor requests → `investor` persona; employment → `hr` persona if the user is an HR professional)
4. **Jurisdictional calibration**: some practice areas have heavily jurisdiction-specific rules (shariah-finance → KSA, UAE, DIFC; arbitration → seat-specific rules)

## Practice Area Labels

Return exactly one primary practice area label and zero or more secondary labels from this set:

| Label | Description |
|---|---|
| `corporate` | Company formation, corporate governance, shareholders, board, equity, cap tables, M&A transactions, SPVs, JVs, restructuring |
| `ip` | Trademarks, patents, copyright, trade secrets, licensing, IP assignment, DMCA, WIPO filings |
| `employment` | Employment contracts, termination, severance, end-of-service gratuity, non-competes, workplace policies, equity grants, labor disputes |
| `real-estate` | Commercial and residential leases, property purchase/sale, land registration, mortgages, real estate development, FIDIC construction adjacent |
| `m-and-a` | Mergers, acquisitions, share purchase agreements, due diligence, representations and warranties, earnouts, escrow |
| `litigation` | Demand letters, pleadings, complaints, defenses, motions, discovery, enforcement of judgments, pre-trial procedure |
| `family` | Divorce, custody, child support, prenuptial agreements, personal status, guardianship |
| `criminal` | Criminal complaints, defense, public prosecution, detention, bail, criminal liability |
| `tax` | Corporate tax, VAT/GST, transfer pricing, withholding tax, tax compliance, stamp duty |
| `immigration` | Visas, work permits, residency, citizenship, deportation, sponsorship (kafala) |
| `banking` | Banking regulation, loan documentation, security instruments, SAMA/CBUAE/BDL regulation, trade finance |
| `regulatory` | Non-banking sector regulation (telecoms, healthcare, energy, broadcasting, competition) |
| `data-privacy` | GDPR, PDPL (KSA), UAE PDPL, DIFC DPL, ADGM DPR, privacy policies, DPIAs, breach notification, data subject rights |
| `competition` | Antitrust, merger control, abuse of dominance, cartel investigations, competition law compliance |
| `construction` | FIDIC contracts, construction disputes, delay claims, EPC/turnkey, subcontracting, defects liability |
| `energy` | Oil and gas, renewables, power purchase agreements, concession agreements, energy regulation |
| `maritime` | Shipping, charterparties, bills of lading, marine insurance, port regulation, ship arrest |
| `arbitration` | Arbitration clauses, notices of arbitration, tribunal constitution, DIAC/ICC/LCIA/SCCA/DIFC-LCIA proceedings, enforcement of awards |
| `insurance` | Insurance policies, claims handling, reinsurance, insurance regulation |
| `aviation` | Aircraft leases, AOC, aviation regulation, GCAA, GACA |
| `healthcare` | Healthcare regulation, medical malpractice, hospital contracts, pharmaceutical licensing |
| `shariah-finance` | Islamic finance instruments (murabaha, ijara, sukuk, wakala, musharaka, mudaraba), AAOIFI standards, Shariah supervisory board matters |
| `estate-personal-status` | Wills, inheritance, estate administration, personal status law, waqf, succession under Shariah |
| `admin` | Default when practice area cannot be determined |

## Signal Heuristics

### High-Confidence Corporate Signals

"NDA", "SHA", "shareholder agreement", "board resolution", "AGM", "EGM", "option pool", "ESOP", "cap table", "convertible note", "SAFE", "venture capital", "term sheet", "liquidation preference", "anti-dilution", "drag-along", "ROFR", "co-sale", "company formation", "articles of association", "memorandum of association", "SPV"

### High-Confidence Employment Signals

"employment contract", "termination", "severance", "end-of-service gratuity", "EOSG", "non-compete", "non-solicitation", "handbook", "disciplinary", "TUPE", "redundancy", "unfair dismissal", "sponsored employee", "work permit"

### High-Confidence Real Estate Signals

"lease", "tenant", "landlord", "eviction", "rent", "service charge", "premises", "property purchase", "sale and purchase agreement" (real estate context), "land registry", "strata title", "RERA", "DLD", "Abu Dhabi municipality"

**Disambiguation note**: if FIDIC is mentioned alongside "construction" rather than a lease context → `construction` not `real-estate`

### High-Confidence Data Privacy Signals

"GDPR", "PDPL", "privacy policy", "data subject", "DPIA", "data protection officer", "DPO", "breach notification", "right of erasure", "right of access", "consent management", "cookies", "personal data", "data processing agreement", "DPA" (in data protection context)

### High-Confidence Arbitration Signals

"arbitration clause", "notice of arbitration", "DIAC", "ICC arbitration", "LCIA", "DIFC-LCIA", "SCCA", "arbitral tribunal", "arbitral award", "seat of arbitration", "enforcement of award", "New York Convention", "UNCITRAL rules"

### High-Confidence Shariah Finance Signals

"murabaha", "ijara", "sukuk", "wakala", "musharaka", "mudaraba", "takaful", "AAOIFI", "Shariah supervisory board", "riba-free", "Islamic finance", "sharia-compliant"

### High-Confidence M&A Signals

"share purchase agreement", "SPA", "asset purchase", "merger agreement", "due diligence", "representations and warranties", "indemnification" (in M&A context), "MAC clause", "material adverse change", "earn-out", "escrow", "closing conditions", "acquisition"

### High-Confidence Litigation Signals

"demand letter", "statement of claim", "complaint", "summons", "injunction", "interlocutory", "discovery", "deposition", "judgment", "appeal", "enforcement", "ex parte order"

## Disambiguation Rules

Some signals overlap between practice areas:

- "Indemnification" alone → corporate or M&A or services depending on context; check document type
- "NDA" → corporate (most common) but may be employment (post-employment NDA) — check context
- "DPA" → data-privacy (data processing agreement) vs M&A (due diligence) → check surrounding signals
- "Employment" + "equity" → corporate + employment dual-label
- "Lease" alone → real-estate; but "software license" → ip; "equipment lease" → banking or commercial
- "Arbitration clause" within a contract review → arbitration secondary; primary is the contract's practice area

## Confidence and Fallback

- **≥ 0.80 confidence**: proceed with the classified practice area; no clarification needed
- **0.50–0.79 confidence**: classify but note the uncertainty in downstream skill selection (may pull from two practice areas)
- **< 0.50 confidence**: return `admin` as the practice area and trigger [[conversation-clarifying-questions]] to ask: "What kind of legal matter is this related to? For example, is it about an employment issue, a contract, a business transaction, or something else?"

Do not ask open-ended questions — offer 3–4 practice area options inferred from the available signals.

## Output

```json
{
  "practice_area": "<label>",
  "confidence": 0.0-1.0,
  "secondary": ["<label>", ...],
  "disambiguation_note": "<if applicable — e.g., 'DPA could be data-privacy or M&A; assuming data-privacy from context'>"
}
```

## Related Skills

- [[router-intent-detection]]
- [[router-jurisdiction-detector]]
- [[router-complexity-grader]]
- [[router-persona-selector]]
- [[router-tool-selector]]
- [[conversation-clarifying-questions]]
