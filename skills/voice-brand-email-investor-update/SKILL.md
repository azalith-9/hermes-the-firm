---
name: voice-brand-email-investor-update
description: Use when drafting a monthly investor update email for HAQQ Legal AI (Louis). This skill defines the exact format, section order, tone, and what to include in each section, ensuring updates are direct, metric-rich, and honest — the standard investors expect and the format that builds long-term credibility with the cap table.
license: MIT
metadata: " id: voice-brand.email-investor-update category: voice-brand priority: P1 intent: [__voice-brand__, investor-update, fundraising, communications] related: - voice-brand-email-cold-outreach-mena - voice-brand-linkedin-post-stephane - voice-brand-press-release-tone source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice-brand'.
Registered as a flat plugin skill.
-->


# Investor Update Email

## When this applies

Use this skill when drafting the monthly investor update for HAQQ Legal AI / Louis. Also applicable to any early-stage legal tech company writing investor updates where the founder wants a structured, honest, no-spin format.

## Core format

The investor update has exactly six sections, in this order:

### 1. Highlights (3–5 bullets)
The most important things that happened since the last update. Lead with the most consequential.

- Each bullet is one line: what happened + why it matters.
- Do not bury good news in qualifications. If revenue grew 40%, say "Revenue grew 40% MoM" at the top.
- Avoid bullet points that say nothing ("Continued executing on roadmap").

### 2. Metrics
Raw numbers. No narrative — investors will form their own interpretation.

Include, where applicable:

| Metric | What to report |
|--------|---------------|
| MRR | Monthly recurring revenue (and MoM % change) |
| ARR | Run-rate (if annualizing is meaningful) |
| MAU | Monthly active users (unique, not sessions) |
| NPS | Net Promoter Score + sample size |
| Churn | Monthly churn rate (user and revenue) |
| Runway | Months of runway at current burn rate |
| Burn | Gross monthly burn |
| Pipeline | Qualified pipeline value (if available) |

If a metric moved significantly (up or down), note it in the Wins or Challenges section — do not hide it here in raw numbers without acknowledgment.

### 3. Wins
What went well. Keep this honest — if it belongs here, it should be a real win, not a consolation prize.
- Deals closed (name the company if consented, else describe the profile).
- Key partnerships or integrations launched.
- Hires made (role + why it matters).
- Press coverage or notable mentions.
- Product milestones shipped.

### 4. Challenges
The most important section for building investor trust. Founders who consistently omit challenges destroy their credibility. Include:
- What is not working, specifically.
- What you tried and why it did not work.
- What you are doing about it.
- Open questions where you genuinely do not know the answer yet.

Do not hide challenges in the "Looking ahead" section.

### 5. Asks
Concrete, actionable requests from the investor. Be specific.

Good asks:
- "Introduction to [Name/Firm] — we are targeting their legal ops team and believe [Investor] knows the GC."
- "Advice on pricing model — we are choosing between per-seat and usage-based; would value 20 minutes."
- "Help with [specific hire] — we are struggling to find a senior sales lead with LegalTech experience in the Gulf."

Bad asks:
- "Let us know if you have any intros."
- "Happy to chat anytime."

### 6. Looking ahead
One-month and one-quarter goals. Keep them specific and measurable.

- "By end of June: reach 50 paying firms."
- "Q3: launch the Word plugin to existing customers."
- "This month: close the KSA government pilot."

## Tone

- Direct, honest, no spin.
- Active voice throughout.
- Write for someone who reads 30 of these a month. They want signal density, not prose elegance.
- Short paragraphs (two to four sentences max outside of metrics).
- No jargon, no startup buzzwords ("hockey stick", "best-in-class", "ecosystem").

## Format tips

- Send as plain-text email or a simple HTML email with minimal styling. Long-form Notion docs or Substack-style layouts read as performative.
- Subject line: "[Company] Investor Update — [Month Year]" — predictable subjects make archiving and search easy for investors.
- Length: 400–700 words for the narrative sections; the metrics table is additional.
- Send on a consistent day each month (e.g., the first Monday of the month). Consistency signals operational discipline.

## What not to do

- Do not omit the metrics section because the numbers are bad. Bad numbers + honest explanation builds more trust than silence.
- Do not ask for feedback on the update itself in the same email — it dilutes the asks.
- Do not send updates longer than 1,000 words unless there is a major event (fundraise close, acquisition, crisis) that warrants it.

## Related skills

- [[voice-brand-email-cold-outreach-mena]]
- [[voice-brand-linkedin-post-stephane]]
- [[voice-brand-press-release-tone]]
- [[voice-brand-tweet-thread-launch]]
