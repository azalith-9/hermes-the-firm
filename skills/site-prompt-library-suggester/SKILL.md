---
name: site-prompt-library-suggester
description: Use when a site visitor navigates to the prompt library, searches for AI prompts for legal work, or uses the in-product prompt discovery feature. Manages the 152-prompt library — filterable by practice area, jurisdiction, and document type — with per-prompt actions (copy, share, save, try-in-product CTA). Helps lawyers and legal teams discover and reuse high-quality prompts for common legal AI tasks.
license: MIT
metadata: " id: site.prompt-library-suggester category: site jurisdictions: [__multi__] priority: P3 intent: [site, prompts, library, discovery, navigation] related: - site-ai-feature-router - site-legal-document-router - site-feature-router - site-solutions-router source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'site'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Prompt Library Suggester — Site Navigation

## Purpose

Manage and surface the platform's prompt library — a curated set of 152 legal AI prompts organized for browsing, filtering, copying, and direct use. The library serves as:
1. A **discoverability tool**: helps users who know they want to use legal AI but don't know how to phrase effective prompts.
2. A **best-practice resource**: demonstrates the right level of specificity, jurisdiction-tagging, and role-setting for effective legal AI prompts.
3. A **growth / SEO surface**: prompt library pages rank for "legal AI prompts" and "best prompts for [practice area]" queries.

## Inputs / signals

| Signal | Target |
|--------|--------|
| Direct `/tools/prompts` navigation | Prompt library landing page (unfiltered) |
| "AI prompts for lawyers", "legal prompts" | Prompt library landing page |
| "Prompts for [practice area]" | Filtered: `/tools/prompts?area=[area]` |
| "Prompts for [jurisdiction]" | Filtered: `/tools/prompts?jurisdiction=[jur]` |
| "NDA prompts", "contract review prompts" | Filtered by document type: `/tools/prompts?doc=[type]` |
| In-product "Suggest a prompt" | Surface top 3 relevant prompts from library based on current context |

## Prompt library architecture

### Scale
152 prompts as of current version. Each prompt entry contains:
- **Prompt text**: the actual prompt, ready to copy.
- **Title**: short human-readable name.
- **Description**: one sentence on when to use this prompt.
- **Practice area tags**: M&A, Employment, IP, Litigation, Corporate, Real Estate, etc.
- **Jurisdiction tags**: UAE, KSA, LB, DIFC, ADGM, GCC, UK, US, EU, Multi.
- **Document type tags**: NDA, employment agreement, SHA, lease, etc. (where applicable).
- **Skill level**: Beginner / Intermediate / Advanced (complexity of the prompt).

### Filter dimensions
- Practice area (multi-select).
- Jurisdiction (multi-select).
- Document type (multi-select).
- Skill level.
- Free text search within prompt text and description.

### Per-prompt actions
- **Copy**: one-click copy of the prompt text to clipboard.
- **Share**: generate a shareable link to this specific prompt.
- **Save**: add to the user's personal prompt collection (requires account).
- **Try in product**: deep-link to the AI chat with the prompt pre-loaded ("Try this prompt in Louis →").

## In-product prompt suggestion

When a user is mid-task in the AI product and appears to be struggling to frame a good query, surface 2–3 relevant prompts from the library:
> "Looking for a good starting point? Here are some prompts from the library that might help:"
> 1. [Prompt title] — [one-sentence description]
> 2. ...

Triggering conditions:
- User's query is very short (< 10 words) or very vague ("help me with a contract").
- User has rewritten their query multiple times in a short period.
- User explicitly asks "how should I phrase this?" or "what's a good prompt for...?"

## Sample prompt categories

### Drafting prompts (examples)
- "Draft a unilateral NDA governed by UAE law for disclosure to a potential strategic partner."
- "Draft a standard employment agreement for a UAE national employee in Abu Dhabi, in English and Arabic."
- "Draft a shareholders agreement for a DIFC-registered company with two co-founders."

### Review prompts (examples)
- "Review this NDA and flag any clauses that are unusual or unfavorable for the disclosing party."
- "Identify all material adverse change triggers in this acquisition agreement."
- "What are the key differences between this employment contract and UAE Labour Law requirements?"

### Research prompts (examples)
- "Summarize the key obligations of a UAE employer on employee termination under Federal Decree-Law No. 33 of 2021."
- "What are the main differences between DIFC arbitration and DIAC arbitration for commercial disputes?"
- "What are the mandatory clauses in a KSA employment contract under Saudi Labour Law?"

## Quality bar for library prompts

Each library prompt must:
- Produce a genuinely useful output when run as written.
- Be jurisdiction-specific where jurisdiction matters — "draft a UAE NDA" not "draft an NDA."
- Avoid ambiguity that would lead to a low-quality default output.
- Be tested against the AI model before publishing.
- Be reviewed and updated when underlying law changes.

## Related skills

- [[site-ai-feature-router]] — routing for AI feature queries (often overlaps with prompt library)
- [[site-legal-document-router]] — document library for template browsing
- [[site-feature-router]] — general feature routing
- [[site-solutions-router]] — persona-based routing that may surface relevant prompt categories
