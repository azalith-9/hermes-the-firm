---
name: router-jurisdiction-detector
description: Use to detect the governing-law jurisdiction(s) implied by the user's message before any drafting, review, or advice task. Never assumes a jurisdiction — uses currency cues, city names, statute references, court names, and party domicile to infer the jurisdiction with a confidence score. Covers 30+ jurisdictions including the full MENA set and GCC free zones. If confidence is below 0.70, triggers the clarifying-questions skill rather than guessing.
license: MIT
metadata: " id: router.jurisdiction-detector category: router priority: P0 intent: [__router__] related: [router-intent-detection, router-practice-area-detector, router-complexity-grader, router-language-detector, router-confidence-scorer] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'router'.
Registered as a flat plugin skill.
-->


# Jurisdiction Detector

## Purpose

Almost every legal question is jurisdiction-specific. The statute that governs a lease, the rules for terminating an employment contract, the validity of a non-compete, the mandatory arbitration requirements — all depend on which jurisdiction's law applies. Answering without knowing the jurisdiction produces advice that may be actively wrong.

This skill detects the likely governing jurisdiction from contextual signals in the user's message. It never assumes. If signals are absent or ambiguous, it asks.

## Supported Jurisdictions

The detector recognizes all jurisdictions in this set:

**MENA primary**:
LB (Lebanon) · KSA (Saudi Arabia) · UAE-federal · UAE-DIFC · UAE-ADGM · QFC (Qatar Financial Centre) · EG (Egypt) · OM (Oman) · KW (Kuwait) · BH (Bahrain) · JO (Jordan)

**MENA secondary**:
MA (Morocco) · DZ (Algeria) · TN (Tunisia) · IQ (Iraq)

**Europe and common law**:
FR (France) · UK-EW (England and Wales) · UK-Scotland · IE (Ireland) · DE (Germany) · ES (Spain) · IT (Italy) · NL (Netherlands) · BE (Belgium)

**Americas**:
US-federal · US-CA (California) · US-NY (New York) · US-DE (Delaware) · US-TX (Texas)

**Supranational**:
EU · OHADA · GCC

## Detection Heuristics

Apply heuristics in this order — earlier signals are stronger:

### 1. Explicit Statement

If the user says "under UAE law", "governed by Lebanese law", "Saudi Arabia PDPL", "DIFC Courts" — this is authoritative; set confidence 0.98.

### 2. Statute / Regulation Cues

Named statutes are very strong signals:

| Cue | Jurisdiction |
|---|---|
| "Article 1124 Civil Code" (Lebanon-specific article reference) | LB |
| "Royal Decree", "Saudi Companies Law", "SAMA", "SCCA" | KSA |
| "Federal Decree-Law", "UAE Labour Law", "VARA" | UAE-federal |
| "DIFC Law No. …", "DIFC Employment Law" | UAE-DIFC |
| "ADGM Regulations", "ADGM Employment Regulations" | UAE-ADGM |
| "PDPL" alone | KSA (Saudi PDPL); disambiguate if UAE context is also present |
| "GDPR" alone | EU (may also apply to non-EU entities processing EU data) |
| "FSRA" | UAE-ADGM |
| "QFC", "QFCA" | QFC |
| "DIFC-LCIA", "DIAC" | UAE-DIFC (arbitration context) |
| "Code des obligations", "OCC" | LB |
| "Loi …/…" | FR or LB depending on context |
| "Companies Act 2006" | UK-EW |
| "Delaware General Corporation Law" | US-DE |

### 3. Court / Tribunal Cues

| Cue | Jurisdiction |
|---|---|
| "Cour de cassation" | LB or FR — disambiguate using other signals |
| "DIFC Courts" | UAE-DIFC |
| "ADGM Court" | UAE-ADGM |
| "Saudi General Court", "Commercial Court Riyadh" | KSA |
| "Dubai Courts" / "Abu Dhabi Courts" | UAE-federal (specific emirate) |
| "Cairo Court of Cassation" | EG |
| "Beirut Court of Appeal" | LB |
| "High Court" alone | UK-EW (primary signal) or other common-law jurisdiction |

### 4. Currency Cues

| Currency | Jurisdiction |
|---|---|
| AED, Dirham | UAE |
| SAR, Riyal (Saudi) | KSA |
| LBP, Lebanese Pound, "fresh dollars" | LB |
| KWD | KW |
| QAR | QFC / Qatar |
| EGP, Egyptian Pound | EG |
| OMR | OM |
| BHD | BH |
| GBP, Sterling | UK |
| EUR | EU / FR / DE / ES / IT / NL (insufficient alone — need other signal) |
| USD alone | Insufficient — may be any jurisdiction using USD for commercial contracts |

### 5. City / Geographic Cues

| Cue | Primary jurisdiction |
|---|---|
| Beirut, Jounieh, Tripoli (LB) | LB |
| Riyadh, Jeddah, NEOM, Mecca, Medina | KSA |
| Dubai | UAE-federal (escalate to DIFC if "financial centre", "DIFC Gate", or "DIFC Courts" mentioned) |
| Abu Dhabi | UAE-federal (escalate to ADGM if "ADGM", "Al Maryah Island", or "financial free zone" mentioned) |
| Sharjah, Ajman, RAK, Fujairah | UAE-federal |
| Cairo, Alexandria, Luxor | EG |
| Doha, Lusail | Qatar (QFC if financial context) |
| Muscat | OM |
| Kuwait City | KW |
| Manama | BH |
| Amman | JO |
| Casablanca, Rabat | MA |
| Tunis | TN |
| Algiers | DZ |
| Paris, Lyon, Marseille | FR |
| London, Manchester, Birmingham | UK-EW |
| New York, NYC | US-NY |
| San Francisco, Los Angeles | US-CA |
| Wilmington, Delaware | US-DE |

### 6. Language Cue (Weak Signal)

Language alone is an insufficient jurisdiction signal:
- Arabic → could be any of LB, KSA, UAE, EG, OM, KW, BH, QA, JO, MA, DZ, TN, IQ
- French → LB, FR, MA, TN, DZ, or any francophone jurisdiction
- English → UK, US, DIFC, ADGM, or any anglophone commercial context

**Important**: language ≠ jurisdiction. Always combine with at least one stronger signal.

### 7. Party / Entity Cue

If entity types or registration details are mentioned:
- "SAL" (Société Anonyme Libanaise) → LB
- "LLC" with AED pricing and Dubai address → UAE-federal
- "PJSC" (Public Joint Stock Company) → UAE-federal
- "JSC" (Joint Stock Company) with KSA context → KSA
- "SPC" (Single Person Company, DIFC) → UAE-DIFC
- "Ltd." alone → UK or international; combine with other signals
- "Inc." alone → US; combine with state cue

## Critical Rules

### Never Assume Jurisdiction

If the jurisdiction cannot be inferred with confidence ≥ 0.70, do not proceed with the request. Trigger [[conversation-clarifying-questions]] to ask:

"To give you accurate advice, I need to know which jurisdiction's law applies. Is this a [suggested option A based on context] or [option B] matter?"

Do not ask open-ended jurisdiction questions — offer 2–3 likely options based on available signals to make it easy for the user to confirm.

### DIFC vs UAE Federal — Always Distinguish

DIFC is a common-law jurisdiction within Dubai with its own distinct laws (DIFC Contract Law, DIFC Employment Law, DIFC Data Protection Law, DIFC Courts). Advice appropriate for UAE federal law may be wrong for DIFC and vice versa. If signals suggest a Dubai/UAE context but do not clearly establish DIFC vs federal, ask: "Is this in the DIFC (Dubai International Financial Centre) or outside the DIFC?"

Same logic for ADGM vs UAE federal.

### Multi-Jurisdiction Requests

If the user's situation clearly spans multiple jurisdictions (e.g., a KSA-incorporated company with DIFC-registered operations processing data from EU residents), flag all relevant jurisdictions and note that the response will address each separately where they differ.

## Output

```json
{
  "primary": "<jurisdiction iso code>",
  "secondary": ["<iso>", ...],
  "confidence": 0.0-1.0,
  "inferred_from": "<brief description of signals used>",
  "clarification_needed": true/false,
  "clarification_question": "<if clarification_needed, the question to ask>"
}
```

If `confidence < 0.70`, set `primary: "unknown"` and `clarification_needed: true`. Do not proceed with any substantive legal work until jurisdiction is established.

## Related Skills

- [[router-intent-detection]]
- [[router-practice-area-detector]]
- [[router-complexity-grader]]
- [[router-language-detector]]
- [[router-confidence-scorer]]
- [[conversation-clarifying-questions]]
