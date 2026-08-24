---
name: router-tool-selector
description: Use to select the minimal toolset required to fulfill a request. Defaults to no tools and adds tools only when there is a clear, specific reason — preventing unnecessary RAG retrieval, web search, or paid API calls that add latency and cost without improving response quality. Consumes the output of the skip-RAG gate, tier-awareness gate, and complexity grader to produce a final tools array for the response pipeline.
license: MIT
metadata: " id: router.tool-selector category: router priority: P0 intent: [__router__] related: [router-skip-rag-when-not-needed, router-tier-aware, router-complexity-grader, router-confidence-scorer] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'router'.
Registered as a flat plugin skill.
-->


# Tool Selector

## Purpose

Every tool activated in the response pipeline has a cost: latency, compute, and potentially a per-call API charge (for the legal data hunter and some web search providers). The tool selector's job is to activate the minimum set of tools that genuinely improves the response, and nothing more.

**Default: no tools.** Start from zero and add tools only when each addition clears a concrete justification.

## Available Tools

| Tool ID | What it does | When to use |
|---|---|---|
| `tool.RAG-firm-knowledge` | Searches the eFirm tenant's own KB (precedents, templates, matter documents, internal policies) | User references "our contract", "our template", "our standard", "the matter" — and a workspace is active |
| `tool.RAG-personal-knowledge` | Searches documents uploaded by the user in their personal store | User uploaded a document and references it by name or as "the document I uploaded" |
| `tool.RAG-public-legal-corpus` | Searches Louis's curated public legal corpus (MENA statutes, regulations, guidance, legal encyclopedias) | Deep-research complexity; user asks about current law in a jurisdiction where the corpus provides verified text |
| `tool.legal-data-hunter` | Paid API: 6.3M laws + 18M cases across 50+ jurisdictions | Jurisdiction or topic not covered by public corpus; user explicitly needs verified statute text or case citation that cannot be found in corpus |
| `tool.web-search-orchestrator` | Fresh web search (Bing/Google + scraping) | Freshness matters (amendments in last 6 months, recent rulings, regulator bulletins); do NOT use for statute text the model already knows |
| `tool.calculator-eosg` | End-of-service gratuity (UAE, KSA, LB, EG) | User provides hire date, termination date, salary, jurisdiction — and wants an EOSG calculation |
| `tool.calculator-interest` | Statutory or contractual interest calculation | User asks for interest calculation with a principal, rate, and period |
| `tool.calculator-deadline` | Limitation period / procedural deadline calculation | User asks when a deadline expires given a start date and jurisdiction |
| `tool.calculator-stamp-duty` | Stamp duty / transfer tax calculation | User asks for the applicable stamp duty on a transaction value in a specific jurisdiction |
| `tool.OCR-arabic` | OCR Arabic text from an image or PDF scan | Input is a scanned image with Arabic text |
| `tool.OCR-english` | OCR English text from a scan | Input is a scanned image with English text |
| `connector.linear` | Read/write Linear tickets | eFirm context: user manages matters in Linear |
| `connector.hubspot-CRM` | Read/write HubSpot CRM records | eFirm context: CRM integration active |
| `connector.stripe` | Read Stripe billing data | eFirm context: billing integration active |

## Decision Rules

Apply rules in this order. Each rule adds a specific tool to the activated set; rules are additive.

### Rule 1 — Skip RAG entirely for clean-query requests

**Source**: [[router-skip-rag-when-not-needed]] result

If the skip-RAG gate returns `skip_rag: true`, do not add any RAG tool to the active set. This rule overrides all others for RAG decisions.

### Rule 2 — Activate firm RAG when workspace is scoped

If `skip_rag: false` AND the user's session has an active workspace/matter AND the request is about a specific document or matter:
→ Add `tool.RAG-firm-knowledge`

Cite results as `[Firm KB]` in the response. Never present firm KB results as verified legal authority — they are the firm's own documents.

### Rule 3 — Activate personal RAG when user document is referenced

If `skip_rag: false` AND the user uploaded a document AND references it in the current message (by name or as "the document", "the file", "the contract"):
→ Add `tool.RAG-personal-knowledge`

### Rule 4 — Activate public corpus RAG for deep-research

If complexity is `deep-research` AND the question requires verified statute/regulation text beyond model training:
→ Add `tool.RAG-public-legal-corpus`

Cite results as official source names (e.g., "UAE Federal Decree-Law No. 33 of 2021 — confirmed via public corpus"). Do not add this tool for `medium` or `short-answer` requests.

### Rule 5 — Activate web search only for freshness

If the question requires information from the last 6 months (recent amendments, regulatory guidance, new rulings):
→ Add `tool.web-search-orchestrator`

Do NOT add web search to verify statute text that the model already has in training — it adds latency without improvement and risks returning low-quality web results instead of authoritative text.

### Rule 6 — Legal data hunter only when corpus is insufficient

If the relevant jurisdiction or topic is not covered in the public corpus AND the question requires a specific statute citation or case text:
→ Add `tool.legal-data-hunter`

This is a paid API call. Use sparingly. Flag in the response that a paid data lookup was used.

### Rule 7 — Activate calculator for arithmetic tasks

If the intent is `calculate` AND the relevant calculator tool is identifiable (EOSG, interest, deadline, stamp duty):
→ Add the relevant `tool.calculator-*`

Do not activate calculators for simple mental arithmetic. Only for jurisdiction-specific statutory calculations with multiple variables.

### Rule 8 — Activate OCR when input is a scan

If the input includes an image or PDF scan (detected via attachment type or user statement "I'm attaching a scanned document"):
→ Add `tool.OCR-arabic` or `tool.OCR-english` based on language

### Rule 9 — Activate connectors only in eFirm context

Connector tools (Linear, HubSpot, Stripe) are only available and appropriate when:
- The tenant is an eFirm tenant
- The user's request specifically involves CRM data, matter data, or billing data
→ Add the relevant connector

Never activate connectors on consumer or public-access surfaces.

## Tier Check

After assembling the candidate tools list from Rules 1–9, apply the tier filter from [[router-tier-aware]]:

- Remove any tool that is not available in the user's current tier
- For each blocked tool: note it in the output with the tier it requires
- If a blocked tool is essential to answer the question: surface an upgrade CTA before proceeding without the tool

## Output

```json
{
  "tools": ["<tool-id>", ...],
  "tools_blocked_by_tier": [
    { "tool": "<tool-id>", "required_tier": "<tier>", "why_needed": "<short>" }
  ],
  "reason": "<one sentence explaining the active tool selection>"
}
```

An empty `tools` array is a valid and common output — it means the model answers from training with no external retrieval.

## Common Failure Modes to Avoid

- Activating RAG on every request "just in case" — a common mistake that kills latency
- Activating web search for statute text questions — the model knows the statute; web search adds noise
- Activating the legal data hunter for well-covered jurisdictions — the model + public corpus can handle UAE, KSA, LB, EG without a paid call
- Activating calculators for trivial arithmetic — "add 30 days to a date" does not need a calculator tool

## Related Skills

- [[router-skip-rag-when-not-needed]]
- [[router-tier-aware]]
- [[router-complexity-grader]]
- [[router-confidence-scorer]]
- [[router-intent-detection]]
