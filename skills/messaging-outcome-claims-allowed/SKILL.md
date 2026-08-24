---
name: messaging-outcome-claims-allowed
description: Use when a copywriter, marketer, or product manager needs to make a specific, measurable outcome claim in customer-facing copy for a legal AI assistant — such as time saved, accuracy rates, or productivity improvements — and needs to know the exact conditions under which such claims are permitted. Covers required evidence standards, disclaimer language, and how to frame quantitative claims for consumer and professional audiences without creating consumer protection or bar advertising liability.
license: MIT
metadata: " id: messaging.outcome-claims-allowed category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, outcome-claims, metrics, evidence, consumer-protection, bar-advertising] related: [messaging-outcome-claims-banned, messaging-compliance-checker, messaging-allowed-claims-consumer, messaging-allowed-claims-lawyer, messaging-hard-rule-bible-signoff-required] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Registered as a flat plugin skill.
-->


# Messaging — Outcome Claims Allowed

## When this applies

An **outcome claim** is any marketing statement that specifies a measurable result achieved by users of the product: hours saved per week, percentage reduction in review time, speed of draft generation, number of issues caught, cost avoided. Outcome claims are more powerful than capability claims — and proportionally more regulated.

This skill defines the conditions under which outcome claims are **permitted** in customer-facing copy. An outcome claim that passes these tests may appear in copy. One that does not is governed by [[messaging-outcome-claims-banned]].

---

## Behavior — Two-Test Gate

Every proposed outcome claim must pass both tests before use:

### Test 1 — Does a source exist?

The claim must be grounded in:
- **Internal user data**: analysed from actual product usage (e.g., session logs, task timing, user surveys)
- **Third-party research**: a published study, independent benchmark, or external analyst report
- **Customer-reported data**: validated testimonials or structured interviews with a defined methodology

A claim cannot be made because it seems likely or because similar companies make it. The source must exist, be documented, and be available for internal review.

### Test 2 — Is the claim correctly framed?

The claim must:
- Be expressed as an **average**, not a guarantee ("on average", "typically", "most users report")
- Include the **source or sample disclosure** wherever space allows, and always in the accompanying legal/disclaimer text
- Use **past or present tense** ("users saved…", "teams reduce…") rather than future promise tense ("you will save…")
- Not imply the outcome is **universal** or **guaranteed**

---

## Approved Claim Templates

These templates represent the standard approved formulations. Fill in the bracketed values from your data source:

| Claim type | Approved template |
|------------|------------------|
| Time saving (weekly) | "Saves [N] hours per week on average — based on data from [X customers / a survey of N users]" |
| Time saving (task-specific) | "Reduces [task name] time by [Y]% on average" |
| Draft generation speed | "First draft in under [N] minutes for [document type]" |
| Review speed | "Reviews a [N-page contract] in [X minutes] on average" |
| Accuracy / issue detection | "Catches [X] common issues missed in manual review — in our benchmark analysis of [N contracts]" |
| Coverage | "Covers [N] practice areas across [M] jurisdictions" |

### Required disclaimer language

Every outcome claim must be accompanied by a disclaimer. Format depends on surface:

**Standalone ad / social post:**
> "Average results; individual outcomes vary."

**Website / landing page:**
> "Based on [survey/data source] of [N] customers. Individual results vary based on use case, document complexity, and user experience."

**Sales deck:**
> "Average from customer survey data [date]. Methodology available on request."

---

## Evidence Standards by Claim Type

| Claim type | Minimum evidence required | Reviewer |
|------------|--------------------------|----------|
| "Saves [N] hours/week" | Survey of ≥ 50 users with defined methodology; statistical confidence |  Data + Legal |
| "Reduces review time by Y%" | Controlled benchmark comparison (same documents, human vs AI) | Data + Product |
| "Draft in under N minutes" | Reproducible demo across ≥ 20 document types at stated length | Product |
| Accuracy or issue-detection rate | Independent review or blind test methodology | Data + Legal |
| Customer satisfaction / NPS | Verified survey data; sample size and methodology disclosed | Data |

---

## Channel-Specific Requirements

| Channel | Disclaimer format |
|---------|------------------|
| Search/display ads | Disclaimer in ad copy or linked landing page |
| Social (Instagram, LinkedIn) | "Results vary" in caption; full methodology on linked page |
| Press release | Quote the source inline; add boilerplate note about averages |
| Sales deck | Footnote per slide with claim source; full methodology appendix |
| Email | Inline disclaimer; link to evidence page |
| Homepage | Full disclaimer block near claim; tooltip or modal with methodology |

---

## Examples

**Allowed:**
> "Louis reduces contract review time by 60% on average — based on a benchmark study of 200 commercial agreements reviewed by Louis vs a team of associates." *(includes source and average disclaimer)*

**Allowed:**
> "Saves 8 hours per week on routine drafting (average, user survey, N=120)." *(concise form with source)*

**Not allowed (see [[messaging-outcome-claims-banned]]):**
> "Louis will save you 10 hours every week." *(future tense, no source, no average qualifier)*

**Not allowed:**
> "The fastest legal AI — saves more time than any competitor." *(comparative superlative without defined methodology)*

---

## New Outcome Claims

Any outcome claim being used for the first time — or a claim with a new numerical value — requires the [[messaging-hard-rule-bible-signoff-required]] process before use. Do not publish new metrics without completing that process.

---

## Related skills

- [[messaging-outcome-claims-banned]]
- [[messaging-compliance-checker]]
- [[messaging-allowed-claims-consumer]]
- [[messaging-allowed-claims-lawyer]]
- [[messaging-hard-rule-bible-signoff-required]]
