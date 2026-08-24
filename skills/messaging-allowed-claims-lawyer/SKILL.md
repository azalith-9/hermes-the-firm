---
name: messaging-allowed-claims-lawyer
description: Use when drafting or reviewing B2B copy, sales decks, LinkedIn content, conference materials, or partnership proposals directed at lawyers, in-house counsel, or law firm decision-makers. Defines the permitted productivity, quality, and workflow claims for a legal AI assistant targeting professional legal practitioners. Pair with messaging-banned-claims-lawyer to understand the full boundary.
license: MIT
metadata: " id: messaging.allowed-claims-lawyer category: messaging priority: P0 intent: [messaging, B2B, lawyer, marketing, claims, productivity, law-firm] related: [messaging-banned-claims-lawyer, messaging-bridge-line, messaging-allowed-claims-consumer, messaging-compliance-checker, messaging-outcome-claims-allowed] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Registered as a flat plugin skill.
-->


# Messaging — Allowed Lawyer Claims

## When this applies

This skill governs all copy directed at **licensed legal professionals and law firm decision-makers**: practicing solicitors, advocates, barristers, in-house counsel, legal operations managers, managing partners, and firm administrators who are evaluating or using a legal AI assistant in their professional practice. It applies to:

- Sales decks and pitch materials
- LinkedIn organic and sponsored content
- Conference and legal tech expo presentations
- Bar association and CLE program partnerships
- Direct outreach emails and sequences
- Product landing pages for professional tiers
- Case study and white-paper content
- Word-of-mouth referral materials shared between lawyers

If the surface has a **mixed audience** (lawyers and non-lawyers), default to the more conservative consumer rules for shared claims, and add a lawyer-specific section only if audience segmentation is confirmed.

---

## Behavior — The Permitted Frame

Lawyers are highly skeptical of technology claims. The permitted frame is **professional tool — augmentation of expert capacity**, not replacement, disruption, or democratization of legal practice. Every claim must respect:

1. The lawyer's expertise and professional judgment as primary
2. The AI as a force multiplier for that judgment
3. Concrete, defensible productivity metrics (when cited, cite the source)
4. Compliance with bar advertising rules (no results guarantees, no comparative performance claims without substantiation)

---

## Allowed Framing (Verbatim and Paraphrased)

| Claim type | Allowed formulation |
|------------|---------------------|
| Productivity | "10x productivity on routine drafting" (substantiate with user data) |
| Collaboration | "Built with lawyers, for lawyers" |
| Platform | "Mobile + desktop workbench — works wherever you do" |
| Time saving | "Save hours on contract review" (average; cite if specific number) |
| First drafts | "Generate first drafts in minutes" |
| Research | "Find precedents and statutory references in seconds" |
| Jurisdictions | "Multi-jurisdictional coverage — LB, UAE, KSA, DIFC, ADGM, UK, EU, US" |
| Integration | "Compatible with your existing workflow (Word, email, document management)" |
| Accessibility | "Available wherever you are — mobile, desktop, Word plug-in" |
| Customisation | "Per-firm customisation: firm playbooks, templates, matter-specific configurations" |
| Consistency | "Consistent quality across every associate, every matter" |
| Client service | "Faster turnaround — better client communication" |

All framing that quantifies time or productivity must be tied to documented internal data or customer survey results and disclaimed as averages.

---

## Allowed Outcomes for Lawyers

These outcome-level claims are permitted in lawyer-directed marketing when accurately substantiated:

- **Productivity gains**: faster drafting, research, and review cycles (cite hours/week or % improvement with source)
- **Quality consistency**: the assistant catches issues that slip through rushed human review
- **Speed**: research, drafting, and review measurably faster for routine work types
- **Better client communication**: faster status updates, clearer explanatory memos
- **Mobile workflow**: full legal capability accessible from phone and tablet — field, court, travel
- **Firm differentiation**: first-mover advantage in tech-enabled practice positioning

---

## Tone for Lawyer Marketing

| Dimension | Guidance |
|-----------|----------|
| Register | Professional, competent, peer-to-peer — never talk down |
| Specificity | Lawyers respond to concrete metrics and worked examples, not abstract aspirations |
| Expertise respect | Frame AI as augmenting the lawyer's irreplaceable judgment, not performing it |
| Bar-rule awareness | Do not make claims that would violate the advertising rules of the targeted bar (KSA, Dubai, DIFC, Lebanon Bar Association, SRA, etc.) |
| No hype | Avoid breathless "revolutionary" language; prefer precise capability descriptions |
| Trust building | Reference law firm clients (with permission), bar partnerships, and security certifications |

---

## Channel-Specific Rules

### LinkedIn
- Thought leadership preferred: "What I learned reviewing 500 Saudi employment contracts with AI"
- Case studies and workflow walk-throughs perform well
- Avoid: "AI will change everything" — too generic and triggers skepticism
- Tag bar associations and legal tech communities for organic reach

### Bar Associations and CLE Programs
- Position as a practice management tool eligible for CLE credit (in jurisdictions that allow technology-focused CLE)
- Emphasise security, confidentiality, and professional responsibility alignment
- Provide whitepapers on ethical use of AI in legal practice to accompany product demos

### Legal Technology Conferences (MENA Legal Tech, GITEX, etc.)
- Demo-driven; lead with the workflow, not the technology
- Show the before/after on a contract review task
- Measure ROI in hours per matter, not vague efficiency claims

### Direct Sales Outreach
- Personalise by firm size and practice area
- Enterprise pitch: emphasise eFirm configuration, team management, usage analytics
- Solo/small firm pitch: emphasise speed-to-first-draft and mobile capability
- Always reference the specific jurisdictions the firm practices in

### Word of Mouth
- Provide referral materials (one-pager, short demo video) suitable for sharing between lawyers
- Lawyer-to-lawyer recommendations are highest-trust — invest in making existing users advocates
- Testimonials: allowed only with documented consent and factual accuracy review

---

## Examples

**Allowed:**
> "Louis generates the first draft of an NDA in under two minutes — our associates use the extra hour for client work."

**Allowed:**
> "Coverage across Lebanon, KSA, UAE, DIFC, and ADGM in one workbench — no more tab-switching between jurisdictions."

**Not allowed (see [[messaging-banned-claims-lawyer]]):**
> "Replace your associates with Louis."

**Not allowed:**
> "Louis does your job better than you."

---

## Edge Cases

| Situation | Rule |
|-----------|------|
| Lawyer testimonial referencing "replacing staff" | Do not publish; request a revised quote |
| ROI calculator showing headcount reduction | Reframe as "capacity expansion" not "headcount reduction" |
| Comparison with a named competitor | Factual comparisons allowed; results comparisons require substantiation; seek legal review |
| Claims about specific legal outcomes | Never allowed — see [[messaging-banned-claims-lawyer]] |
| Claim about passing bar exam | Novelty/awareness only; do not frame as replacing bar study or competence |

---

## Do not

- Suggest the product replaces or diminishes the role of lawyers (direct conflict with the lawyer buyer's professional identity)
- Claim specific case wins, settlement amounts, or outcome percentages
- Use consumer-style "anyone can do this" framing on lawyer surfaces
- Imply the product displaces associates, juniors, or paralegal staff
- Use "cheaper than hiring" framing on B2B materials — lawyers find this threatening to their billing model

---

## Related skills

- [[messaging-banned-claims-lawyer]]
- [[messaging-bridge-line]]
- [[messaging-allowed-claims-consumer]]
- [[messaging-compliance-checker]]
- [[messaging-outcome-claims-allowed]]
