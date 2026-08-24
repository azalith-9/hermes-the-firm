---
name: voice-multimodal-signature-page-detector
description: Use when processing a legal document (PDF, image, or OCR output) to detect signature pages, validate that all required signatures and witness blocks are present, and flag missing or incomplete execution elements. This skill covers detection patterns for wet signatures, electronic signatures, notary stamps, and MENA-specific instruments (Tawqi3i, Ministry attestation), plus per-jurisdiction validation of witness and notarization requirements.
license: MIT
metadata: " id: multimodal.signature-page-detector category: voice priority: P1 intent: [signature detection, signature validation, notarization, execution] related: - voice-multimodal-scanned-pdf-handler - voice-image-of-contract-page-handler - voice-signature-page-detector source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice'.
Registered as a flat plugin skill.
-->


# Signature Page Detector

## What it does

Legal documents are only as good as their execution. A contract with missing signatures, absent witnesses, or an unfilled notary block may be unenforceable. This skill detects all execution-related elements in a legal document — whether the input is a native-text PDF, a scanned document (after OCR via [[voice-multimodal-scanned-pdf-handler]]), or a set of page images — and produces a structured execution status report.

## Detection patterns

### Text-based signature block detection (native text PDFs)

Signature blocks contain recognizable text markers. Detect:

| Marker type | Examples |
|-------------|---------|
| Role indicators | "By:", "Executed by:", "Signed by:", "For and on behalf of:" |
| Name/title fields | "Name:", "Title:", "Designation:" |
| Date fields | "Date:", "Dated this ___ day of" |
| Witness indicators | "Witness:", "Witnessed by:", "In the presence of:" |
| Notary indicators | "Notary Public:", "This instrument was acknowledged before me", "Certified correct by:" |
| Arabic equivalents | بتوقيع، اسم الشاهد، توثيق |

### Visual signature detection (scanned documents and images)

When processing image content:
- **Signature lines**: horizontal underscores or printed lines followed by or preceded by a name/title field.
- **Handwritten signatures**: visual strokes that deviate from printed text — irregular baseline, variable stroke width, cursive-style marks.
- **Initials on pages**: short handwritten marks at bottom corners of pages (required in many MENA jurisdictions for multi-page contracts).
- **Rubber stamps / corporate seals**: circular or rectangular impression marks, often with company name text around the rim.
- **Electronic signature markers**: DocuSign completion flags ("Signed by [Name] [ID]"), Adobe Acrobat signature fields with completion status, HelloSign blue completion banners.
- **MENA e-signature markers**: Tawqi3i (UAE government e-signature platform) completion indicators.

### Stamp detection
- **Corporate seals**: round or rectangular stamps bearing company name, registration number, jurisdiction. Common in UAE, KSA, and Lebanon.
- **Notary stamps**: official stamps from a Notary Public (UAE, Lebanon, Egypt) bearing their registration number and jurisdiction.
- **Ministry attestation stamps**: UAE Ministry of Foreign Affairs, Saudi MOFA, Lebanese Foreign Ministry — required for documents going through apostille or consular legalization chains.

## Validation against required execution

After detection, validate completeness. The required elements depend on the document type and jurisdiction:

| Document type | Jurisdiction | Required execution elements |
|---------------|-------------|---------------------------|
| Simple contract | UAE onshore | Signatures of all named parties; date |
| Contract > AED 500k (court-enforceable) | UAE onshore | Signatures + potentially witness or notary depending on type |
| Employment contract | UAE | Employer + employee signatures; MOHRE registration |
| Power of attorney | UAE / Lebanon | Notary stamp + signatures; in Lebanon, also Civil Registry |
| Real estate SPA | UAE | Dubai Land Department format; notarization |
| Wills | UK / DIFC | Testator + two witnesses (no beneficiary witness) |
| Share transfer | ADGM / DIFC | Corporate resolution + transfer form signatures |
| Court submission | Lebanon | Lawyer signature + bar number |

### Key MENA-specific requirements

**Tawqi3i (UAE)**: The UAE government's official e-signature platform. Documents executed through Tawqi3i are legally equivalent to notarized wet-ink signatures for most civil and commercial purposes. Detect Tawqi3i completion certificates and treat them as equivalent to notarization.

**Witness requirements**: Many jurisdictions require witnesses for wills, real property deeds, and powers of attorney:
- UAE: wills before a UAE Will Registry require two witnesses.
- Lebanon: most formal acts before a notaire require two witnesses.
- KSA: court documents may require male Muslim witnesses per classical interpretation (varies by court/context).

**Initials on every page**: In Lebanon and many civil law jurisdictions, multi-page contracts require initials (paraphe) on every page from all parties, not just on the signature page. Flag if initials are absent from interior pages.

**Apostille and consular legalization**: For cross-border documents, the full execution chain must be present — notarization, then Ministry of Foreign Affairs attestation, then receiving country's consular legalization. Flag incomplete chains.

## Output format

The skill returns a structured execution report:

```json
{
  "total_pages": 12,
  "signature_pages": [10, 11],
  "detected_signers": [
    {"role": "Party 1", "name": "ABC LLC", "signature_present": true, "date_present": true, "page": 10},
    {"role": "Party 2", "name": "[blank]", "signature_present": false, "date_present": false, "page": 10}
  ],
  "witness_blocks": [
    {"required": true, "present": true, "page": 11}
  ],
  "notary_block": {"required": true, "present": false, "page": 11},
  "initials_on_all_pages": false,
  "missing_pages_with_initials": [3, 5, 7],
  "stamps_detected": ["Corporate seal — ABC LLC", "Notary stamp — incomplete"],
  "flags": [
    "Party 2 signature missing",
    "Notary block present but stamp absent",
    "Initials missing on pages 3, 5, 7"
  ]
}
```

## Critical handling rules

- **Do not paraphrase or reformat signature blocks during OCR.** The exact text, layout, and spacing of a signature block are legally significant. Return them as-is.
- **Do not redact signature images.** Signature images should be preserved even when PII redaction is applied to the surrounding text.
- **Flag, do not auto-fill.** If a date field is blank, flag it — do not infer a date from surrounding context and fill it in.
- **Multi-party complex documents**: for documents with more than four signatories (e.g., a shareholders' agreement or a syndicated facility), produce a per-party execution checklist rather than a simple pass/fail.

## Related skills

- [[voice-multimodal-scanned-pdf-handler]]
- [[voice-image-of-contract-page-handler]]
- [[voice-signature-page-detector]]
- [[voice-dictation-cleanup]]
