---
name: outreach-growth-agent-runner
description: Use when the legal AI product team needs to orchestrate a multi-step growth experiment — combining content creation, outreach sequencing, press targeting, analytics, and feedback loops. Acts as the coordinator skill that chains together individual outreach skills into a coherent growth campaign. Triggers when a growth experiment or campaign run is requested, not just a single content or outreach task.
license: MIT
metadata: " id: outreach.growth-agent-runner category: outreach intent: ['__outreach__', 'growth', 'orchestration', 'campaign', 'experiment'] related: - outreach-backlink-pr-campaign - outreach-blog-preview-renderer - outreach-inbox-scan - outreach-press-list-enriched - outreach-userflow-analyzer priority: P3 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'outreach'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Growth Agent Runner

Individual outreach skills (blog posts, press lists, backlink campaigns) are building blocks. The growth agent runner chains them into an end-to-end campaign that starts from a growth hypothesis, executes coordinated actions, and measures outcomes. This is the orchestration layer.

## Purpose

Run a coherent growth experiment for a legal AI product, coordinating:
1. Hypothesis definition — what are we testing and what is success?
2. Asset creation — blog posts, landing pages, lead magnets
3. Outreach execution — press, social, partner, community
4. Inbox and response management — triage inbound leads and coverage
5. Analytics — did it work?

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Growth hypothesis | "Publishing a multi-jurisdiction non-compete guide will generate 50 backlinks and 200 signups" | Must be specified |
| Campaign timeframe | Week / month / quarter — determines scope | 4-week sprint |
| Available resources | What can actually be executed (writing bandwidth, PR budget, tools) | Lean / founder-led |
| Target audience segment | Who are we trying to reach in this campaign? | MENA in-house GC |
| Success metrics | What does winning look like? | Signups, backlinks, press mentions |

## Campaign logic

### Step 1 — Define the hypothesis

A growth experiment must be falsifiable:
> "We believe that publishing a free MENA employment law guide will generate X qualified leads via SEO in Y weeks because MENA GCs search for this content and there is low competition."

Without a clear hypothesis, you cannot measure success or learn from failure.

### Step 2 — Select the growth levers

For a legal AI product, the highest-leverage growth channels are:

| Channel | Why it works | Skills to activate |
|---|---|---|
| SEO + content | Lawyers search for answers — be the answer | [[outreach-blog-preview-renderer]] |
| PR + backlinks | Domain authority + direct traffic from professional publications | [[outreach-backlink-pr-campaign]] |
| Community | Legal communities (bar associations, LinkedIn groups, Chambers) | Bespoke per community |
| Product virality | Users who share output or invite colleagues | [[outreach-userflow-analyzer]] |
| Email / direct outreach | Warm introductions to GCs and legal ops heads | [[outreach-inbox-scan]] |

Choose 1–2 channels per sprint. Do not try to run all channels simultaneously with limited resources.

### Step 3 — Create the assets

Trigger the relevant content skills:
- Blog post: [[outreach-blog-preview-renderer]]
- Press list: [[outreach-press-list-mena]] or [[outreach-press-list-europe]] depending on target
- Video assets: [[outreach-video-asset-library]]

Ensure each asset has a clear CTA (call to action) that drives to a measurable conversion event (signup, demo request, download).

### Step 4 — Execute outreach

- Press pitches: sequence per [[outreach-backlink-pr-campaign]] — D0, D7, D14 follow-up
- Social: publish blog post with social copy; engage in comments
- Community: share in relevant legal communities with a value-first framing (not promotional)
- Direct: send personalised intro emails to 20–50 target GCs using [[outreach-inbox-scan]] triage for inbound responses

### Step 5 — Monitor and triage

- Daily: check inbox for journalist responses, inbound leads, coverage alerts ([[outreach-inbox-scan]])
- Weekly: check analytics — traffic, signups, backlinks gained
- Respond to coverage within 24 hours; amplify press mentions on social

### Step 6 — Measure and debrief

At the end of the sprint, produce a one-page growth debrief:

```
Campaign: [Name]
Hypothesis: [Statement]
Levers activated: [List]
Results:
  - Backlinks gained: [N] (target: [T])
  - Press mentions: [N]
  - Traffic to landing page: [N]
  - Signups / conversions: [N]
  - Cost: [£/$ or hours]
Verdict: ✅ Hypothesis confirmed / ⚠️ Partial / 🚫 Failed
Learnings: [What we know now that we didn't before]
Next sprint: [Adjusted hypothesis or new channel to test]
```

## Quality bar

- Every growth action must map to a measurable outcome. "We sent some emails" is not a campaign result.
- Legal AI growth content must maintain the accuracy standard — a viral post with a legal error is worse than no post.
- Growth experiments should be run in 4-week sprints with a defined hypothesis, not open-ended "let's try things" initiatives.

## What to avoid

- Running too many channels simultaneously — dilutes focus and makes attribution impossible
- Vanity metrics (social impressions, followers) without conversion tracking
- Growth content that sacrifices legal accuracy for shareability
- Outreach to journalists without a genuine news hook

## Related skills

- [[outreach-backlink-pr-campaign]]
- [[outreach-blog-preview-renderer]]
- [[outreach-inbox-scan]]
- [[outreach-press-list-enriched]]
- [[outreach-userflow-analyzer]]
- [[outreach-video-asset-library]]
