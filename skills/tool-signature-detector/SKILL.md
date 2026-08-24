---
name: tool-signature-detector
description: Use when checking whether a contract PDF has been fully executed — i.e., all signature blocks are signed — or to identify where signature placeholders remain blank. Detects signature lines, executed wet-ink signatures, initials on pages, and official stamps/seals. Critical for execution verification workflows, document closing checklists, and flagging counterparty documents where execution status is unclear.
license: MIT
metadata: " id: tool.signature-detector category: tool jurisdictions: [__multi__] priority: P2 intent: [signature-detection, execution-check, document-closing, contract-verification] related: [tool-ocr-english, tool-ocr-arabic, tool-pdf-extractor, multimodal-scanned-pdf-handler] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Signature Detector

## What it does

The Signature Detector analyzes a contract or legal document (PDF or image) to:
1. Locate all signature blocks and signature placeholder lines
2. Determine whether each signature block has been executed (signed) or is still blank
3. Detect page initials, stamps, and seals
4. Return an execution status report showing which parties have signed and which have not

This is used primarily in execution verification — confirming that a contract is fully executed before treating it as binding — and in document closing checklists where multiple documents from multiple parties must all be signed before a transaction completes.

## When to use this

- User uploads a contract PDF and asks "Has this been signed?"
- Closing checklist requires confirming all documents are executed
- Counterparty sends a "signed" document that needs verification
- Reviewing a batch of historical contracts for execution status
- Document management triage — determining which contracts in a folder are signed vs unsigned

## Pipeline

### Step 1: Document ingestion
The document is first processed through [[tool-pdf-extractor]]. If the PDF has a text layer, text-layer extraction identifies signature block markers (`__________`, `Signed: ___`, "Signature:" etc.). If the document is scanned, [[tool-ocr-english]] or [[tool-ocr-arabic]] is invoked first.

### Step 2: Signature block detection

**Rule-based detection** (text layer):
- Regex patterns for signature line indicators: underscores (`_____`), dotted lines, labels ("Signature:", "Signed by:", "By:", "Authorized Signatory:", "توقيع:")
- Detection of party designation labels near signature lines ("For and on behalf of:", "Party A:", "Witness:")
- Date fields adjacent to signature lines ("Date: ___")

**Visual detection** (scanned or image-based):
- Classify regions of the page by visual features:
  - Horizontal lines in the lower third of the page → candidate signature blocks
  - Handwritten-style strokes in a signature region → executed signature
  - Absence of strokes / blank space → unsigned
- Confidence score per detection

### Step 3: Execution analysis
For each detected signature block:
```json
{
  "page": 8,
  "party": "Party B — Acme Corp",
  "blockType": "signature_line",
  "status": "executed" | "blank" | "uncertain",
  "confidence": 0.88,
  "detectedContent": "ink_present",
  "hasWitness": true,
  "witnessStatus": "executed",
  "hasDateField": true,
  "dateStatus": "filled"
}
```

### Step 4: Initials on pages
Some contracts require initials on each page (common in Lebanon, French law contracts, and notarized documents):
- Detect bottom-of-page initial regions
- Classify as initialed / blank
- Report which pages are missing initials

### Step 5: Stamps and seals
Official stamps and company seals are common in MENA contracts:
- **Types**: circular company stamps, rectangular government stamps, notarial seals, "Apostille" stamps
- Detection: identify circular/rectangular ink regions with uniform pressure
- **Do not transcribe** stamp text unless quality is high — note the presence and location
- Flag: "Company stamp detected — page X" vs "No stamp detected — verify if required by counterparty"

### Step 6: Execution status summary
```json
{
  "overallStatus": "partially_executed" | "fully_executed" | "unsigned" | "uncertain",
  "parties": [
    {
      "partyLabel": "Party A — Seller",
      "signaturePage": 12,
      "status": "executed",
      "initialsPages": [1, 2, 3, 4, 5, "all_present"]
    },
    {
      "partyLabel": "Party B — Buyer",
      "signaturePage": 12,
      "status": "blank",
      "initialsPages": [1, 2, 3, "page_4_missing"]
    }
  ],
  "stamps": [{ "page": 12, "type": "company_stamp", "detected": true }],
  "warnings": ["Party B signature block is blank", "Page 4 initials missing for Party B"]
}
```

## Jurisdictional execution requirements

Execution requirements differ materially across jurisdictions:

| Jurisdiction | Typical requirements | Notes |
|---|---|---|
| DIFC / ADGM | Simple signature; witness optional for deeds | Common law formalities; e-signature generally accepted |
| UAE onshore | Signature + company stamp preferred; notarization for real property | Stamp not legally mandatory but culturally expected |
| KSA | Signature + company stamp; notarization (توثيق) for real property and certain corporate acts | Arabic version must be signed if bilingual |
| Lebanon | Both parties sign + initial each page; notarization (تصديق كاتب العدل) for most commercial contracts | Failure to initial every page can raise authenticity issues |
| France | Signature at bottom; initialing of pages for multi-page contracts (paraphé) is standard | Electronic signatures accepted under eIDAS |
| Egypt | Signature + company stamp; official certification (توثيق) via notary for major contracts | Arabic version is authoritative |
| UK | Signature for simple contracts; witness for deeds | Electronic signatures accepted under Law Commission guidance |

The detector flags when required elements are missing based on the jurisdiction setting.

## Electronic signature detection

Electronic signatures have specific visual patterns:
- **DocuSign**: blue/purple "DocuSign" banner + certificate text at document end
- **Adobe Sign**: similar footer + certificate
- **HelloSign / Dropbox Sign**: signature image with certificate block
- **Simple e-signature** (typed name in signature field): detect as "e-signature — typed"
- **Wet-ink scan**: handwritten signature on paper then scanned

Each type is classified in the output. For DocuSign/Adobe Sign certificates, the tool also extracts the timestamp and signer email from the certificate block.

## Limitations

- Cannot verify the **authenticity** of a handwritten signature (i.e., whether it was made by the named person) — this requires a forensic document examiner
- Cannot confirm **authority to bind** the entity — check the corporate registry tool for this
- Electronic signatures: can detect their presence but cannot verify the underlying PKI certificate without access to the signing platform's API
- Very low-quality scans: confidence drops; mark blocks as "uncertain" requiring human review

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| All signature blocks uncertain | Low confidence on all blocks | Re-request higher-quality scan; escalate to human review |
| Complex signature page layout | Multi-column signature block not parsed | Flag for manual check |
| Non-standard execution format | Parties sign on separate counterparts | Detect "EXECUTED AS A DEED" / "COUNTERPART" wording; adjust expectations |
| Arabic-only document | Signature labels in Arabic not recognized | Route through [[tool-ocr-arabic]] first; use Arabic signature label patterns |

## Related skills

- [[tool-ocr-english]] — required for scanned English documents before signature detection
- [[tool-ocr-arabic]] — required for scanned Arabic documents before signature detection
- [[tool-pdf-extractor]] — text-layer extraction that feeds signature block text patterns
- [[multimodal-scanned-pdf-handler]] — full scanned document pipeline including this tool
