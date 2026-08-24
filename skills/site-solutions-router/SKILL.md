---
name: site-solutions-router
description: "Use when routing a site visitor or in-app user to the persona-specific solutions page that matches their professional role or use case. Covers six personas: lawyers (law firms), in-house counsel, law students, SME founders, enterprises, and consumers (B2C). Detects persona from explicit role statement, navigation behavior, or profile data, and routes to /solutions/[slug]. Also used for in-app 'Is this for me?' queries and sales-intent conversations."
license: MIT
metadata: " id: site.solutions-router category: site jurisdictions: [__multi__] priority: P1 intent: [site, routing, persona, solutions, navigation, sales] related: - site-feature-router - site-ai-feature-router - site-legal-document-router - site-compare-us-router source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'site'.
Registered as a flat plugin skill.
-->


# Solutions Router — Persona-Based Site Navigation

## Purpose

Route users to the `/solutions/:slug` page that best matches their professional role and use case. Different personas have substantially different needs from a legal AI platform — a law-firm partner cares about billing efficiency and matter-quality; an SME founder cares about self-serve contract review without legal fees. The solutions pages make the value proposition concrete and persona-specific, improving conversion from "I found this tool" to "this is for me."

## Solution pages — persona map

| Persona | URL slug | Primary audience | Key value proposition |
|---------|---------|-----------------|----------------------|
| Lawyers (private practice) | `/solutions/lawyers` | Law firm associates, partners, counsel | Faster drafting, research, matter triage; AI as leverage for billable output |
| In-house counsel | `/solutions/in-house-counsel` | Corporate legal department teams | Contract volume management, risk triage, faster turnaround to business clients |
| Law students | `/solutions/law-students` | LLB/JD students, trainee lawyers | Research tool, drafting practice, moot/exam prep |
| SME founders | `/solutions/sme-founders` | Startup founders, small business owners | Self-serve contract review, template access, reduce lawyer spend on routine matters |
| Enterprises | `/solutions/enterprises` | Large corporate legal and procurement teams | Bulk contract review, compliance monitoring, integration with enterprise systems |
| Consumers (B2C) | `/solutions/consumers` | General public, individuals with legal questions | Legal information, document preparation, access to justice |

## Routing logic

### Detection inputs (in priority order)
1. **Explicit persona statement**: user says "I'm a lawyer", "I'm a startup founder", "I'm in-house at a bank" → direct route.
2. **Profile data**: user is authenticated and profile records their role → route to matching solution.
3. **Navigation context**: user arrived via a lawyers-specific campaign URL (`?utm_campaign=law-firms`) → route to `/solutions/lawyers`.
4. **Behavioral signals**: user searches for "eFirm", "billing", "matter management" → lawyers; "contract review for my company" → in-house counsel; "student", "moot" → law students.
5. **"Is this for me?" query**: explicit question about fit → show persona options and route to best match.
6. **No signal**: show all six solution options on the `/solutions/` index page.

### Routing rules
```
1. Detect persona from inputs (see above).
2. Map to solution slug:
   - "lawyer", "solicitor", "advocate", "barrister", "law firm", "partner" → /solutions/lawyers
   - "in-house", "GC", "legal dept", "corporate counsel" → /solutions/in-house-counsel
   - "student", "law school", "LLB", "bar prep", "trainee" → /solutions/law-students
   - "founder", "startup", "SME", "entrepreneur", "CEO", "small business" → /solutions/sme-founders
   - "enterprise", "procurement", "legal ops", "large company" → /solutions/enterprises
   - "individual", "personal", "my case", "help me" (no professional context) → /solutions/consumers
3. Route to /solutions/[slug] with tracking parameters.
4. Track persona identification + page view for conversion analytics.
```

## In-app usage

### "Is this for me?"
When a user asks directly whether the platform suits their role:
1. Ask one clarifying question if role isn't clear: "Are you a practicing lawyer, in-house counsel, law student, or using this for your own business?"
2. Route to matching solution page.
3. Offer to continue helping with their task.

### Sales-intent conversations
When a user is clearly evaluating the platform for purchase or trial activation:
1. Identify persona.
2. Surface the solution page URL.
3. Offer to demonstrate the most relevant features for that persona.
4. Link to pricing page if appropriate.

### Marketing-page to in-app link
Solution pages on the public site should deep-link into the app at the most relevant starting point for that persona:
- Lawyers → in-app contract review or research start.
- In-house counsel → in-app contract intake or clause library.
- SME founders → in-app NDA or service agreement template.
- Consumers → in-app legal information chat.

## Critical constraints

### Messaging consistency
The solutions pages must match actual product capabilities for that persona. Do not:
- Promise features that don't exist for that persona.
- Use lawyer-audience messaging on consumer pages (and vice versa).
- Claim jurisdiction coverage that the product doesn't have.

### Disclaimer placement
- Consumer page (`/solutions/consumers`): must include the legal-information-not-advice disclaimer prominently.
- Lawyers page (`/solutions/lawyers`): no general disclaimer needed (they are the qualified professionals); a brief note on AI verification obligations is appropriate.

See [[safety-no-legal-advice-disclaimer-rules]] for disclaimer surface rules.

## Related skills

- [[site-feature-router]] — feature-specific routing that may follow persona routing
- [[site-ai-feature-router]] — routing to specific AI feature pages
- [[site-legal-document-router]] — document library routing (often persona-filtered)
- [[site-compare-us-router]] — competitive comparison pages (often accessed by lawyers evaluating)
