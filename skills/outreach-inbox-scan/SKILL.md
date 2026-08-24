---
name: outreach-inbox-scan
description: Use when the legal AI product team needs to triage and respond to inbound outreach — journalist inquiries, partnership requests, user support escalations, investor notes, and press coverage alerts. Scans and categorises inbox items, drafts responses at appropriate priority, and surfaces high-value opportunities that require immediate action. Triggers when asked to process or prioritise inbound communications for a legal AI product.
license: MIT
metadata: " id: outreach.inbox-scan category: outreach intent: ['__outreach__', 'inbox', 'triage', 'response', 'PR', 'partnerships'] related: - outreach-growth-agent-runner - outreach-backlink-pr-campaign - outreach-press-list-enriched - outreach-payment-recovery-flow priority: P3 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'outreach'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Inbox Scan

Inbound communications are the highest-signal input for a growth-stage legal AI product: a journalist reaching out has 10x the conversion value of a cold outreach. Missing or slow-responding to a press inquiry, partnership request, or investor note can cost a coverage placement, a deal, or a funding conversation. This skill governs rapid inbox triage and response drafting.

## Purpose

Scan and triage inbound communications to:
1. Surface time-sensitive opportunities (press inquiry, investor note, partnership)
2. Categorise all inbox items by type and priority
3. Draft responses at the right tone and level of detail for each category
4. Flag items that require legal or executive review before responding

## Inputs

| Input | Description | Required |
|---|---|---|
| Inbox content | Email thread, message, or platform notification to process | Yes |
| Sender context | Who sent it — journalist, investor, user, partner, unknown | Infer from email domain/content if not stated |
| Response urgency | Any stated deadline or context-implied time sensitivity | Default: 24h SLA for press; 48h for others |

## Triage categories

| Category | Trigger signals | Priority | Response SLA |
|---|---|---|---|
| Press / journalist inquiry | "writing a piece", "reporting on", "comment on", publication domain | 🔴 CRITICAL | 4 hours |
| Investor / due diligence | "investing in", "portfolio", "diligence", VC/family office domain | 🔴 CRITICAL | 4 hours |
| Partnership request | "collaborate", "integration", "partnership", bar association / law firm domain | 🟡 HIGH | 24 hours |
| User support / feedback | "bug", "problem with", "how do I", "love the product" | 🟡 HIGH | 24 hours |
| Sales / commercial inquiry | "pricing", "enterprise", "demo", "quote" | 🟡 HIGH | 24 hours |
| Recruiting / HR | Job application, recruiter outreach | 🟢 NORMAL | 72 hours |
| Generic / cold | Generic pitch, newsletter, vendor outreach | 🟢 LOW | Weekly batch |
| Spam | Unsolicited, irrelevant, suspicious links | ⚪ SKIP | Archive |

## Response drafting

### Press inquiry response

Keep it brief and fast. The journalist is on a deadline.

```
Subject: Re: [their subject line]

Hi [Name],

Thank you for reaching out. I'm happy to help.

[2–3 sentences of direct, quotable response to their specific question]

Happy to jump on a quick call if that's easier — I'm available [two specific slots].

Best,
[Name]
[Title, Company]
[Phone]
```

Rules:
- Never say "no comment" — offer something useful even if you can't answer the specific question.
- Every quoted statement should be accurate and defensible — it will be published.
- Provide one specific data point or insight they can use even if you decline to comment on the main question.
- Always offer a call — moving to voice doubles conversion rate.

### Partnership response

```
Hi [Name],

Thanks for reaching out about [specific partnership idea].

[Brief statement of genuine interest or fit — one sentence]

[One clarifying question to understand their ask]

Happy to set up a call this week. What's your availability?

Best,
[Name]
```

### Investor inquiry response

Do not draft an investor response without founder/executive review. Flag immediately and escalate.

Template to send to founder: "Inbound from [Name/Fund]. They [describe inquiry]. Recommend responding within 4 hours. Draft: [brief draft for review]."

### User support response

```
Hi [Name],

Thank you for reaching out. [Acknowledge their specific issue in one sentence.]

[Resolution or next step — direct and concrete.]

If you need anything else, reply here or reach me at [email].

Best,
[Name]
```

## Coverage alerts

When a press mention or backlink is detected:
1. Verify the mention is accurate (no corrections needed)
2. Amplify: share on social with a thank-you to the publication
3. Track in the backlink/press log for [[outreach-backlink-pr-campaign]] reporting
4. Respond to the journalist on social or by email to nurture the relationship for future coverage

## What to avoid

- Delayed press responses — journalists move on quickly; 4 hours is the practical maximum
- Over-formal language in partnership emails — sound like a person, not a legal document
- Forwarding investor inquiries to a generic inbox without flagging to a decision-maker
- Ignoring negative feedback or critical user reports — these are the highest-value product signals

## Related skills

- [[outreach-growth-agent-runner]]
- [[outreach-backlink-pr-campaign]]
- [[outreach-press-list-enriched]]
- [[outreach-payment-recovery-flow]]
