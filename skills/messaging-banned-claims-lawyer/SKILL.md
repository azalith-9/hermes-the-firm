---
name: messaging-banned-claims-lawyer
description: Use when reviewing B2B copy, sales decks, LinkedIn posts, conference materials, or any content directed at lawyers, law firm partners, or in-house counsel for a legal AI assistant. Defines the specific displacement, commodification, and practice-threat framings that must never appear in professional-audience materials — because they trigger hostile rejection by the buyer audience, violate bar advertising norms, and undermine the product's partnership model with the legal profession.
license: MIT
metadata: " id: messaging.banned-claims-lawyer category: messaging priority: P1 intent: [messaging, banned, B2B, lawyer, sales, copy-review] related: [messaging-allowed-claims-lawyer, messaging-bridge-line, messaging-banned-claims-consumer, messaging-compliance-checker, messaging-outcome-claims-banned] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Registered as a flat plugin skill.
-->


# Messaging — Banned Lawyer Claims

## When this applies

This skill governs copy directed at **licensed legal professionals and law firm decision-makers** — partners, associates, in-house counsel, legal ops managers, and firm administrators. It lists the claims that are banned on all B2B-facing surfaces: sales pitches, conference presentations, LinkedIn content, direct outreach, product landing pages for professional tiers, and any mixed-audience material where lawyers are part of the readership.

Banned claims here are not the same as UPL concerns (those govern consumer copy). Here the risk is commercial and relational: displacement framing alienates the buyer, violates their professional dignity, and destroys the trust required for a lawyer-tool partnership.

---

## Behavior — The Absolute Prohibitions

The following claims and framings are **never permitted** on lawyer-facing or B2B surfaces.

---

## Banned Framing — Verbatim and Category

### Displacement of Lawyers or Staff

| Banned | Why |
|--------|-----|
| "Replaces associates" | Partners and senior lawyers are the buyers — they will not purchase a tool pitched as eliminating their team |
| "Cuts your team in half" | Staffing threat; triggers both buyer rejection and professional regulation concerns |
| "Outsource your work to AI" | Frames AI as a substitute for professional judgment; signals malpractice risk |
| "AI will do your job better" | Direct professional threat; the most hostile possible framing for a lawyer audience |
| Anything implying AI displaces lawyers | Any variant of displacement, substitution, or professional obsolescence framing |

### Revenue and Billing Model Threats

| Banned | Why |
|--------|-----|
| "Pass on the savings to your clients" | Directly attacks the lawyer's billing model; creates pressure to cut fees |
| "Slash your billing rates" | Same; implies the tool reduces the value of legal services |
| "Clients can do this without you" | Crosses into consumer displacement framing, undermining the professional relationship |

### Consumer-Style Framing on Lawyer Surfaces

| Banned | Why |
|--------|-----|
| "Anyone can do this!" | Commodifies legal expertise; signals the tool is a consumer-grade product |
| "No legal training needed" | Applied to lawyer surfaces, this is insulting to the buyer's identity and training |
| "DIY legal" | Consumer positioning; wrong register for professional audiences |

---

## Why These Rules Exist

### 1. Lawyer Audience Psychology
Legal professionals are trained in adversarial thinking and are acutely sensitive to displacement threats. A lawyer who reads "replaces associates" does not think "efficiency" — they think "this is a threat to my firm, my staff, and my business model." This framing reliably triggers rejection even from practitioners who are otherwise enthusiastic about legal technology.

### 2. Professional Dignity
Lawyers are licensed professionals with fiduciary obligations to clients. Claims that an AI tool "does your job better" attack both their professional self-concept and implicitly suggest they could delegate professional responsibility to a software product. This creates anxiety about malpractice and bar discipline exposure.

### 3. Buyer's Reality
In law firms, the purchase decision is made by partners and senior lawyers — the same people whose role the banned claims threaten. No rational buyer authorises a purchase that displaces themselves. The commercial logic of the banned-claims rule is straightforward: say these things and you will not close the sale.

### 4. Bar Rule Alignment
Professional responsibility rules in most jurisdictions (SRA, KSA Bar, Dubai Bar, Lebanon Bar Association, New York Bar) require that a licensed lawyer remain responsible for legal work product. Copy suggesting the AI "does the work" or "replaces" professional judgment creates a compliance issue for the firm and signals that the product does not understand this requirement.

---

## Replace With — Positive Alternatives

| Banned | Allowed replacement |
|--------|---------------------|
| "Replaces associates" | "Frees up associates for high-value, client-facing work" |
| "Outsource to AI" | "Augment your team with AI — speed up what takes time, elevate what takes judgment" |
| "AI does your job" | "AI accelerates your work — you remain in control of every output" |
| "Cuts your team in half" | "Expands your team's capacity without adding headcount" |
| "Pass on the savings" | "Deliver faster turnaround — without expanding costs" |
| "Anyone can do this" | "Built for legal professionals — with the depth and accuracy the profession demands" |

The substitution rule: if a claim implies lawyers become less necessary, reframe it to show lawyers becoming more valuable.

---

## Where These Bans Apply

- Sales decks and pitch materials at any stage (discovery, demo, proposal, contract)
- LinkedIn organic posts and sponsored content targeting legal professionals
- Conference presentations and exhibition materials
- Bar association partnership proposals
- Direct outreach emails and sequences to law firm contacts
- Product documentation and onboarding materials for professional tiers
- Case studies and white papers with lawyer audiences
- Any mixed-audience content (apply lawyer rules to the B2B sections)

---

## Examples

**Banned:**
> "Louis replaces your associates on routine drafting. One subscription, zero headcount."

**Banned:**
> "Cut your legal team's size by 30% in the first year."

**Banned:**
> "Pass on the AI savings to your clients and win on price."

**Allowed:**
> "Your associates spend hours on first drafts. Louis gives them a strong starting point in minutes — so they can focus on judgment and strategy."

**Allowed:**
> "Handle more matters with the same team. Louis handles the time-consuming parts; your lawyers handle the parts that require expertise."

---

## Edge Cases

| Situation | Rule |
|-----------|------|
| Journalist or analyst using displacement framing in coverage | Correct in interview; issue a clarification quote; do not republish the framing in marketing materials |
| Lawyer testimonial referencing "replaced my paralegal" | Do not feature or amplify; request revised quote framing expansion of capacity |
| Internal presentation to investor showing headcount efficiency | Permitted for investor-only materials with appropriate framing; not for any lawyer-facing surface |
| Research report citing X% productivity gain | Productivity claims are allowed; ensure the underlying methodology is sound and disclaim averages |

---

## Do not

- Apply consumer rules to lawyer audiences (wrong register; still fails, just for different reasons)
- Assume that a lawyer who describes the product positively using banned framing is endorsing that framing for marketing use
- Permit "just for this one deck" exceptions — banned claims in sales decks are the most consequential because they reach decision-makers directly
- Allow disclaimer-covered displacement claims ("Of course, Louis won't *really* replace your team…")

---

## Related skills

- [[messaging-allowed-claims-lawyer]]
- [[messaging-bridge-line]]
- [[messaging-banned-claims-consumer]]
- [[messaging-compliance-checker]]
- [[messaging-outcome-claims-banned]]
