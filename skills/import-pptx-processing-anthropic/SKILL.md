---
name: import-pptx-processing-anthropic
description: Use when migrating a PowerPoint (PPTX) document-processing skill originally built for the Anthropic the agent API into the mini-hermes-the-firm format. The adapter maps legacy slide-extraction configuration — text per slide, speaker notes, embedded tables, charts, and metadata — into the standard skill model. Relevant for legal teams processing board presentations, regulatory submissions in slide format, due-diligence summaries, and deal-team pitch decks.
license: MIT
metadata: " id: import.pptx-processing-anthropic category: import jurisdictions: [__multi__] priority: P3 intent: [__import__, pptx, powerpoint, document-processing, migration, anthropic] related: [import-docx-processing-anthropic, import-pdf-processing-anthropic, import-meeting-briefing-anthropic, multimodal-document-ingestion] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'import'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Import: PPTX Processing (Anthropic)

## What it does

This import adapter migrates a **PPTX (PowerPoint) document-processing skill** originally built for Anthropic's the agent API into the `mini-hermes-the-firm` standard format. Legal teams encounter PPTX files regularly: board decks for M&A transactions, regulatory filings in presentation format, due-diligence summary decks, compliance training materials, and client pitch books all arrive as PowerPoint files.

Unlike DOCX or PDF, PPTX organises content spatially across slides rather than linearly. The extraction must preserve the slide-by-slide structure, surface speaker notes (which often contain the real substance), and extract tables and charts that carry data relevant to legal analysis.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `extraction_mode` | Legacy `mode` | `slide_by_slide` |
| `speaker_notes` | Legacy `extract_notes` boolean | `true` |
| `tables` | Legacy `extract_tables` boolean | `true` |
| `charts` | Legacy `extract_charts` | `alt_text_only` (chart data not extractable without specialist tool) |
| `hidden_slides` | Legacy `include_hidden` boolean | `false` (legal risk — hidden slides may contain sensitive data) |
| `metadata_fields` | Legacy `doc_properties` | `[author, created, modified, title, company]` |
| `language` | Legacy `lang` | `auto-detect` |
| `output_format` | Legacy `format` | `markdown_slide_by_slide` |
| `chunk_size` | Legacy `chunk_tokens` | `2000` |

## Dry-run preview

```
IMPORT PREVIEW — pptx-processing-anthropic
Source shape   : Anthropic PPTX extraction config
Mode           : slide_by_slide
Speaker notes  : extracted
Tables         : extracted
Charts         : alt-text only (data extraction requires specialist tool)
Hidden slides  : excluded (flag to user)
Metadata       : author, created, modified, title, company
Output         : markdown_slide_by_slide
```

## Extraction pipeline (post-import)

1. **Parse PPTX XML**: unzip the `.pptx` container; read each slide's `ppt/slides/slideN.xml` and `ppt/notesSlides/notesSlideN.xml`.
2. **Slide metadata**: extract slide number, layout name, and master theme.
3. **Body text**: extract all text elements per slide, preserving logical reading order (title → sub-title → body → footer).
4. **Speaker notes**: extract from notes slides; append to the corresponding slide block.
5. **Tables**: serialise to markdown pipe tables; flag merged cells.
6. **Charts**: extract alt-text or title if present; note that chart data series require a separate Excel extraction step — flag to user.
7. **Hidden slides**: exclude by default; flag existence and count to user for manual review.
8. **Metadata**: extract document properties including author and company (potential privilege or confidentiality signals).

## Legal document considerations

- **Board presentations**: speaker notes often contain privileged legal advice or strategic information; flag the entire deck as potentially privileged if author is in-house or external counsel.
- **Due-diligence decks**: look for financial projections, representations, and warranties in tables — these may be incorporated by reference into transaction documents.
- **Regulatory submissions**: some regulators accept or request slide format; page/slide numbering must be preserved.
- **Hidden slides**: hidden slides are a known information-security risk in M&A (counterparty may have left sensitive data in hidden slides received via data room); always flag their existence.
- **Track-changes equivalent**: PPTX does not have tracked changes like DOCX, but comments on slides serve a similar function; extract and flag.

## MENA-specific notes

- Board presentations for UAE or KSA entities may be bilingual (Arabic/English); RTL slides require special handling.
- Saudi Aramco, ADNOC, and other sovereign entities often require Arabic as the primary language in board materials; flag if English-only.
- Investor decks for Gulf sovereign wealth funds (ADIA, PIF, Mubadala) frequently contain financial projections that may constitute representations; extract and flag for legal review.

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `corrupt_pptx` | File not valid ZIP/XML | Ask user to re-save from PowerPoint |
| `notes_missing` | No speaker notes in source | Skip notes extraction; note absence |
| `chart_data_unavailable` | Charts are images/OLE objects | Extract alt-text only; recommend manual data extraction |
| `hidden_slides_present` | Legacy included hidden slides | Flag to user; do not auto-include |
| `rtl_slide_reversal` | Arabic slides parsed LTR | Set RTL flag; re-extract |

## Related skills

- [[import-docx-processing-anthropic]]
- [[import-pdf-processing-anthropic]]
- [[import-meeting-briefing-anthropic]]
- [[multimodal-document-ingestion]]
- [[import-contract-review-anthropic]]
