---
name: router-platform-aware
description: Use to detect the deployment surface (web, mobile, voice, API, Word plugin, email) and apply appropriate output shaping rules — word limits, formatting style, citation placement, and structure depth. Runs in every response pipeline before the response is composed. Ensures that a mobile user does not receive a wall of markdown, a voice user does not receive bulleted lists, and an API caller does not receive narrative text when JSON was expected.
license: MIT
metadata: " id: router.platform-aware category: router priority: P0 intent: [__router__] related: [router-persona-selector, router-language-detector, router-complexity-grader, router-intent-detection] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'router'.
Registered as a flat plugin skill.
-->


# Platform-Aware Output Shaping

## Purpose

The same response rendered on different surfaces reads very differently. Full markdown with nested headers and code blocks is ideal on a web interface; it is unreadable when spoken aloud or pasted into a Word document. This skill detects the surface and shapes output accordingly — applying word limits, formatting constraints, and structural rules that make each response feel native to its surface.

Platform detection runs before the response is drafted, not after. It is not post-processing — it shapes the drafting instructions given to the response generator.

## Supported Surfaces

### `web` (default)

The default assumption when no surface signal is present.

**Rules**:
- Full markdown supported: `##` headings, `**bold**`, `_italic_`, tables, code blocks, ordered and unordered lists
- Citations inline in the body: "[Statute reference]" or "(Art. 47 UAE Federal Decree-Law No. 33 of 2021)"
- Heading depth: up to `###` (3 levels); deeper nesting degrades readability
- Response length: no hard cap; use length appropriate to the complexity grade from [[router-complexity-grader]]
- Tables: appropriate for comparison tasks, checklists, and structured output

### `mobile`

Detected when:
- User agent identifies a mobile browser or mobile app
- Session metadata flags mobile surface
- Explicit API parameter `surface: "mobile"`

**Rules**:
- Hard cap on non-document responses: approximately 300 words (~400 tokens)
- Paragraph-first, not header-first: lead with the answer in prose; use headers only if the response has 3+ distinct sections that benefit from navigation
- Bullet lists: 3–5 items maximum per list; no nested lists
- No wide tables: tables with 4+ columns do not render well on mobile; convert to a list or a 2-column name/value format
- Heading depth: maximum 2 levels (`##` only)
- Citations: summarized at the end ("Sources: [1] UAE Labour Law Art. 43") rather than inline, to avoid cluttering the response body

### `voice`

Detected when:
- Input arrives via STT (speech-to-text) pathway
- Session metadata flags voice surface
- User is on a voice-enabled interface (smart speaker, voice-first app)

**Rules**:
- **Prose only**: no markdown of any kind — no bullets, no headers, no code blocks, no tables
- **No inline citations**: citations cannot be "heard" — collect them at the end: "Sources: first, [statute]; second, [case]"
- **Maximum 150 words per response**: approximately 60 seconds of spoken output; beyond this, user retention drops sharply
- **Natural spoken transitions**: "First…", "Next…", "Also…" instead of bullets
- **No special characters**: em-dashes, parenthetical insertions, slashes — these interrupt natural speech rhythm
- **Numbers**: spell out short numbers ("thirty days") rather than numerals; percentages can be "fifteen percent"

### `word-plugin`

Detected when:
- Session identifies the Microsoft Word add-in or similar document plugin surface

**Rules**:
- **Pure text**: no markdown beyond `**bold**` and `_italic_` (which map to Word bold/italic); no headers (Word has its own heading styles)
- **Track-change-friendly**: produce text in a format that can be easily copied into track-changes mode; use brackets for alternatives: "[Option A / Option B]"
- **No emoji or special symbols** that may not render correctly across Word versions
- **Numbered lists**: use plain `1.` numbering rather than markdown `*` bullets — Word handles numbered lists better
- For clause drafting: produce the clause text on its own, then a brief commentary section below (separated by a line), so the lawyer can copy the clause directly

### `email`

Detected when:
- Session identifies an email composition plugin
- The request is explicitly to "draft an email" or "write a response to this email"

**Rules**:
- Greeting + body + sign-off in the tenant's configured voice
- No markdown in the body — email clients vary; use plain paragraphs
- Subject line suggestion where appropriate
- Limit to 200–300 words for most business emails; escalate to "formal legal letter" format for legal notices

### `api`

Detected when:
- Session identifies a direct API call without a UI surface
- No system prompt indicating a UI-rendering surface

**Rules**:
- **Structured JSON only** for data responses — no narrative wrapper
- For document drafting: return the document text as a JSON string value within a structured response object
- No greeting, preamble, or sign-off
- Citations: include in a structured `sources` array in the JSON response
- Errors and uncertainty: return as structured JSON with `confidence` and `caveats` fields, not as prose apologies

## Detection Priority

1. Explicit API parameter `surface: "<id>"` — highest priority
2. User agent / session metadata from the SDK or platform layer
3. System prompt signals (e.g., "You are operating in the Word plugin context")
4. Default to `web` if no signal

## Output

```json
{
  "surface": "web|mobile|voice|word-plugin|email|api",
  "max_tokens_out": <integer or null>,
  "format": "markdown|prose|json|track-changes|email",
  "heading_depth": <integer — max heading level>,
  "inline_citations": true/false,
  "tables_ok": true/false
}
```

## Related Skills

- [[router-persona-selector]]
- [[router-language-detector]]
- [[router-complexity-grader]]
- [[router-intent-detection]]
