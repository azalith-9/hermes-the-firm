---
name: ref-long-documents-50pp
description: Use as a reference guide for processing legal documents that exceed approximately 50 pages — the point at which direct full-text prompting becomes inefficient or exceeds context window limits. Covers chunked processing, outline-first strategies, targeted section analysis, vector embedding for semantic search, and tool-call patterns for agent-based document navigation. Applies to due diligence packages, M&A data rooms, long-form contracts, regulatory filings, and litigation bundles.
license: MIT
metadata: " id: ref.long-documents-50pp category: ref priority: P1 intent: [__ref__, long-documents, chunking, processing, document-analysis] related: - ref-anti-patterns - ref-verification - multimodal-scanned-pdf-handler - public-tool-case-summarizer-public - public-tool-contract-summarizer-public source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ref'.
Registered as a flat plugin skill.
-->


# Reference — Long Documents (50+ Pages)

## Scope

Any legal document exceeding approximately 50 pages — a long-form contract, an M&A due diligence data room, a regulatory submission, a multi-day arbitration hearing bundle, a legislative comment package — requires a different processing strategy from short documents. Pasting the full text into a prompt has three problems:

1. **Token cost:** Long documents consume a disproportionate share of the context window, leaving little room for the AI to reason and respond
2. **Attention diffusion:** AI models do not read every word with equal attention across very long contexts; material near the middle of a very long prompt is more likely to be mischaracterized or overlooked
3. **No targeting:** Pasting the full text and asking "summarize this" produces a generic summary; targeted analysis of specific clauses, sections, or risk areas requires targeted extraction

This reference sets out the strategies for handling long documents efficiently.

---

## Strategy 1 — Outline first, then targeted analysis

The single most effective approach for large documents:

**Step 1 — Extract the structure**
Prompt the AI to read the document (or a chunk if it is very long) and produce only a structural outline:
- For a contract: article numbers, headings, and one-sentence summary per article
- For a judgment: procedural history, issues, findings, and outcome — without detail
- For a data room: document names, dates, and one-line description per document

**Step 2 — Identify priority sections**
From the outline, identify which sections require detailed analysis. In an M&A context, this might be the representations and warranties, the material adverse change definition, and the closing conditions — not the boilerplate.

**Step 3 — Targeted analysis per section**
Analyze each priority section in isolation: paste only that section, with full context about what it is, and apply the relevant review skill.

This approach produces better output than a single "analyze everything" prompt because each targeted analysis has the full context window available for reasoning.

---

## Strategy 2 — Chunked processing with rolling summary

For very long documents where even the outline is too long to process in one pass:

**Process:**
1. Divide the document into chunks of approximately 5,000–8,000 words (roughly 15–25 pages)
2. For each chunk: produce (a) a summary of key provisions and (b) a list of flagged issues
3. At the end of all chunks: consolidate the summaries and flag lists into a master document

**Key rule:** Each chunk summary must include enough context to stand alone — the consolidated summary must make sense without re-reading the full document.

**Variant — Rolling context:** Pass the summary of chunk N as context when processing chunk N+1. This allows the AI to detect cross-chunk issues (e.g., a definition in Article 1 that affects a clause in Article 47).

---

## Strategy 3 — Scanned PDF extraction

Many long legal documents arrive as scanned PDFs (executed contracts, court files, physical records). These cannot be processed as text until the text is extracted.

**Apply [[multimodal-scanned-pdf-handler]]** for:
- OCR extraction of scanned PDFs
- Handling dual-column Arabic / English layouts
- Handling handwritten notes or stamps on official documents
- Quality-checking the extraction before analysis

**Quality threshold:** If OCR confidence is below 90%, the extracted text may contain errors that corrupt the analysis. Flag low-confidence extractions and prompt the user to provide a cleaner source.

---

## Strategy 4 — Vector embedding for semantic search

For very large document sets (a data room with 200+ documents) where even chunked processing of each document is impractical:

**Approach:**
1. Generate vector embeddings for each document chunk (using the platform's embedding model)
2. When a specific question arises ("does any document contain a change-of-control provision?"), run a semantic search against the embedding store to retrieve the most relevant chunks
3. Analyze only the retrieved chunks, not the full document set

**Applications in legal work:**
- Due diligence: "Does any contract in this data room contain a most-favored-nation clause?"
- Litigation discovery: "Which of these 500 emails discusses the project delivery date?"
- Regulatory audit: "Which of these policies reference the PDPL's data subject rights obligations?"

This approach converts a document review task from a linear sequential process into a query-driven one — dramatically more efficient for large sets.

---

## Strategy 5 — Agent tool-call patterns for document navigation

For platform implementations with tool-calling (MCP) enabled:

**Preferred pattern:**
1. Tool call: `load_document(path)` — indexes the document and returns a structural outline
2. Tool call: `navigate_to_section(article_id)` — retrieves the specific section text
3. Tool call: `analyze_clause(section_text, analysis_type)` — runs the appropriate review skill on the isolated clause
4. Tool call: `compile_findings()` — assembles the section-level findings into a master report

This pattern is more reliable than a single large prompt because:
- Each tool call is atomic and independently verifiable
- The agent can navigate back to earlier sections if a later clause depends on an earlier definition
- The output is structured and traceable to specific document sections

---

## Anti-patterns to avoid

| Anti-pattern | Consequence |
|---|---|
| Pasting entire 100-page contract in one prompt | Poor attention across the document; high token cost; generic output |
| Chunking without rolling context | Misses cross-clause dependencies; definition in one chunk may be undefined in another |
| Accepting low-quality OCR output without checking | Numerical errors (contract price, dates) may be corrupted; changes the legal analysis |
| Using a single "summarize everything" prompt for a data room | Produces a generic summary; misses specific risk areas that require targeted analysis |
| Forgetting to verify chunk boundaries cut logical units | A chunk that cuts in the middle of an article produces an incomplete analysis of that article |

---

## Decision guide

| Document length | Approach |
|---|---|
| < 20 pages (machine-readable) | Single prompt; use the relevant review or drafting skill directly |
| 20–50 pages (machine-readable) | Outline first → targeted section analysis |
| 50–150 pages (machine-readable) | Chunked processing with rolling summary |
| > 150 pages or scanned | OCR extraction → vector embedding → semantic search, or tool-call navigation |
| Multi-document data room (50+ documents) | Vector embedding with semantic search; document-by-document review only for priority documents |

---

## Related skills

- [[ref-anti-patterns]]
- [[ref-verification]]
- [[multimodal-scanned-pdf-handler]]
- [[public-tool-contract-summarizer-public]]
- [[public-tool-case-summarizer-public]]
