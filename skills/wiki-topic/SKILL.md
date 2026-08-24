---
name: wiki-topic
description: Use as a catch-all topic discovery skill when a user asks about a subject domain that may not yet have a dedicated skill, or when the router cannot confidently match the user's question to an existing skill. Surfaces relevant existing skills and reference packs for any new domain, and provides a methodology for scoping the legal dimensions of unfamiliar topics.
license: MIT
metadata: " id: wiki.topic category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, topic discovery, domain scoping, skill discovery, catch-all] related: [wiki-research, wiki-skill, wiki-strategy, wiki-startup, wiki-space, wiki-tech] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Topic Discovery — Catch-All Reference

## Scope

This skill fires when a user introduces a domain that does not cleanly match any dedicated skill in the registry, or when the system needs to surface relevant knowledge across multiple areas. It is a structured first-response for unfamiliar or cross-domain questions.

---

## Purpose

Not every legal question maps neatly to a single skill. Users ask cross-cutting questions ("I need to set up a space company in KSA"), cite unfamiliar jurisdictions ("can you help with Qatari insurance regulation?"), or introduce novel domains ("what are the legal issues with web3 gaming in the UAE?"). This skill provides a repeatable discovery methodology rather than a content-specific answer.

---

## Discovery Methodology

### Step 1 — Identify the Primary Domain

What is the user's question fundamentally about? Decompose into:
- **Subject matter**: what industry or legal area? (technology, employment, IP, finance, real estate, criminal, etc.)
- **Jurisdiction**: which country or free zone? (UAE, KSA, LB, EG, DIFC, ADGM, UK, US, EU, or cross-border)
- **Task type**: what does the user want to do? (draft, review, research, understand, advise, comply, dispute)

### Step 2 — Check the Registry for Existing Skills

Search the registry (`[[_REGISTRY.md]]`) for:
- Exact match on subject matter + jurisdiction
- Partial match on subject matter (different jurisdiction)
- Adjacent skill that covers part of the domain

Present the closest matching skills with a brief explanation of what each covers, so the user can pick the most relevant entry point.

### Step 3 — Map the Legal Dimensions

For domains without an existing skill, use this framework to map the legal dimensions:

| Dimension | Questions to ask |
|-----------|----------------|
| Corporate / commercial | Is there an entity? Contracts? Deal structure? |
| Regulatory / licensing | Does the activity require a license or permit? Ongoing compliance? |
| Employment | Are people being hired? What jurisdiction's labor law applies? |
| IP | Is there technology, content, or branding involved? Who owns it? |
| Data / privacy | Is personal data being collected or processed? Which data protection law applies? |
| Tax | What tax registrations or implications arise? VAT? Withholding? Corporate tax? |
| Litigation / dispute | Is there a dispute? What forum and governing law? |
| Finance / capital | Is capital being raised? Lending? Equity? Crypto? |
| Real estate | Is property involved? Lease or ownership? Registration? |
| Cross-border | Does the transaction span multiple jurisdictions? Conflict of laws? |

### Step 4 — Surface Jurisdiction-Specific Gaps

If the jurisdiction is unfamiliar (e.g., Qatar, Bahrain, Kuwait, Jordan, Iraq, Tunisia):
- Note the jurisdiction's legal tradition (civil law, mixed, Islamic law overlay)
- Identify the primary regulatory bodies
- Flag that the skills in this library have primary coverage of LB, KSA, UAE (incl. DIFC/ADGM), EG, FR, UK, US, EU — for other jurisdictions, conclusions should be verified with local counsel

### Step 5 — Provide an Orientation and Next Steps

Give the user:
1. A brief orientation on the domain's key legal issues (using verified, general knowledge — no invented statute numbers)
2. The closest existing skills that partially address the question
3. A clear recommendation: which skill to run next, or what specific legal questions to bring to local counsel

---

## Domain-to-Skill Quick Reference

Use this table as a starting-point map. It is not exhaustive — consult the full registry for the complete list.

| Domain | Primary skills | Notes |
|--------|---------------|-------|
| Startup incorporation | [[workflow-startup-incorporation-pack]], [[draft-articles-of-association]] | Jurisdiction-specific variants |
| Contract review | [[review-contract-redline]], [[workflow-contract-redline-20min]] | Contract type matters |
| Employment hire | [[workflow-hire-employee-pack]], [[draft-employment-contract-uae]] | Jurisdiction-specific |
| Employment termination | [[workflow-fire-employee-pack]], [[draft-termination-letter]] | Jurisdiction-specific |
| NDA | [[workflow-nda-triage-red-yellow-green]], [[draft-nda-mutual]] | Bilateral vs unilateral |
| Due diligence | [[workflow-full-due-diligence-pack]] | Transaction type matters |
| Fundraising / VC | [[workflow-investment-round-closing-pack]], [[wiki-vc-startups]] | Round stage matters |
| Brand / trademark | [[workflow-brand-protection-pack]], [[draft-trademark-application]] | Jurisdiction-specific |
| Data privacy / GDPR | [[workflow-gdpr-implementation-pack]], [[draft-privacy-policy]] | PDPL parallel for MENA |
| Dispute / litigation | [[workflow-dispute-pre-litigation-pack]], [[draft-demand-letter]] | Pre-litigation focus |
| Lease / real estate | [[workflow-lease-negotiation-pack]], [[draft-commercial-lease]] | Commercial vs residential |
| Space / launch | [[wiki-space]] | Emerging regulatory area |
| Strategy / GTM | [[wiki-strategy]], [[wiki-sales]] | Context-dependent |
| Research methodology | [[wiki-research]] | Cross-jurisdictional |
| Tech / AI | [[wiki-tech]] | Regulatory rapidly evolving |
| VC / startup funding | [[wiki-vc-startups]], [[wiki-startup]] | MENA ecosystem focus |

---

## When to Escalate Beyond AI

This system is designed for legal professionals and informed users; it is not a substitute for legal advice. Recommend escalation to qualified local counsel when:
- The jurisdiction is not covered by existing skills (e.g., Iraq, Libya, sub-Saharan Africa outside OHADA)
- The question involves criminal liability
- The question involves an ongoing or imminent litigation with a short statutory deadline
- The factual situation is highly complex or the stakes are very high
- The user is seeking advice that will be directly relied upon without further professional review

---

## How to Use This Pack

This pack fires automatically when the router cannot find a better match. It can also be invoked explicitly by a user who wants to explore the skill library or understand what coverage exists for a new domain.

The output should always guide the user to the most relevant next skill, not attempt to answer the full question from this generic catch-all position.

---

## Caveats & Currency

The topic registry is a living document. New skills are added as new domains are developed. Absence of a skill for a domain does not mean the domain is outside the system's capability — it may just mean the skill has not been authored yet.

## Related Skills

- [[wiki-research]]
- [[wiki-skill]]
- [[wiki-strategy]]
- [[wiki-startup]]
- [[wiki-space]]
- [[wiki-tech]]
- [[wiki-vc-startups]]
