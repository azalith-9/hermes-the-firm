---
name: outreach-video-asset-library
description: Use when the legal AI product team needs to build, organise, or deploy a library of video assets for marketing, outreach, product demos, and educational content. Covers video formats, production guidance, SEO for video, and distribution strategy across platforms relevant to a legal professional audience. Triggers when creating or managing video content for a legal AI product.
license: MIT
metadata: " id: outreach.video-asset-library category: outreach intent: ['__outreach__', 'video', 'content', 'marketing', 'library'] related: - outreach-haqq-ai-viz - outreach-blog-preview-renderer - outreach-growth-agent-runner priority: P3 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'outreach'.
Registered as a flat plugin skill.
-->


# Video Asset Library

Video is underutilised in legal AI marketing: most competitors rely on text and static graphics. A well-produced 90-second explainer video converts better than a 1,000-word landing page for the majority of professional audiences. A structured video library serves both marketing and product education — the same content that explains the product to a potential user also trains new team members. This skill governs how to build and maintain that library.

## Purpose

Build and maintain a structured library of video assets that:
- Explains the product and its key capabilities to prospective users
- Provides jurisdictional and practice-area-specific educational content
- Supports the press and partner outreach effort (video press kits)
- Drives organic growth through YouTube/LinkedIn/platform SEO

## Video asset types

### 1. Product explainer (60–90 seconds)

The highest-priority video. Answers: "What is this product, who is it for, and why does it matter?"

Structure:
- 0–10s: hook — the problem (a MENA lawyer facing a multi-jurisdiction NDA at 11pm)
- 10–40s: the product in action — screen recording of the most impressive capability
- 40–70s: the benefit — what the user gets (speed, accuracy, coverage)
- 70–90s: CTA — "Try it free at [domain]"

Production requirements: professional narration or on-camera spokesperson; clean screen recording with no debug tools visible; brand-consistent colour scheme.

### 2. Feature walkthroughs (2–5 minutes)

One video per major feature:
- Contract review walkthrough
- Multi-jurisdiction comparison tool
- NDA drafting assistant
- IRAC analysis output

Format: screen recording with voiceover. These are primarily used in onboarding sequences and help centre content.

### 3. Jurisdiction explainers (3–5 minutes educational)

Short educational videos on key legal topics for the target audience:
- "UAE Employment Law in 5 Minutes"
- "DIFC vs UAE Onshore: Which Court?"
- "Non-Compete Clauses in KSA: What You Need to Know"

These drive SEO on YouTube and LinkedIn. They demonstrate expertise without being purely promotional.

Legal accuracy standard: these videos make legal statements — every statement must be verified and current. Add a disclaimer: "This video is for informational purposes only and does not constitute legal advice."

### 4. Case studies / testimonials (1–3 minutes)

Interview format with a named user (GC, managing partner, or legal associate):
- The problem they faced
- How they used the product
- The outcome

For legal professionals: get explicit written consent before naming them or their firm. Many lawyers cannot endorse products publicly due to bar association rules.

### 5. Conference / event content (variable)

Conference talks, demo recordings, panel discussions. Archive and repurpose:
- Full talk on YouTube
- 60-second highlight clip for social
- Quote cards from the talk (see [[outreach-haqq-ai-viz]])

## Library structure

Organise the video library with a consistent naming and metadata schema:

| Field | Description | Example |
|---|---|---|
| Asset ID | Sequential or structured ID | VID-2026-001 |
| Title | Descriptive title | "UAE Non-Compete Clauses Explained" |
| Type | Explainer / Walkthrough / Case study / Conference | Explainer |
| Duration | HH:MM:SS | 00:04:23 |
| Jurisdiction(s) | Target jurisdiction | UAE |
| Practice area | Relevant practice area | Employment |
| Status | Draft / Review / Published | Published |
| Publish date | Date live | 2026-03-15 |
| URLs | YouTube, LinkedIn, internal CDN | [links] |
| SEO keywords | Target keywords for video SEO | "UAE employment law", "non-compete UAE" |
| Transcript | Full transcript (for accessibility + SEO) | [file link] |
| Thumbnail | Custom thumbnail file | [file link] |

## Production guidelines

**Screen recordings:**
- Resolution: 1920×1080 minimum (4K preferred for 2026)
- Clean browser/desktop — hide bookmarks, extensions, personal data
- Use a test account, not a production account with real client data
- Cursor highlighting enabled

**On-camera:**
- Professional background or branded virtual background
- Stable lighting (ring light or two-point setup)
- Audio: USB condenser microphone; eliminate background noise

**Narration/voiceover:**
- Script reviewed for legal accuracy before recording
- Avoid legal jargon for explainer videos aimed at non-lawyers
- Pace: 130–150 words per minute for educational content

## Distribution

| Platform | Content type | Frequency |
|---|---|---|
| YouTube | All video types | All videos; SEO-optimised titles/descriptions |
| LinkedIn | Explainers, case studies, conference clips | 2× per month |
| Product website | Explainer + feature walkthroughs | Embedded on landing page and help centre |
| Email campaigns | Explainer for onboarding sequences | Linked in first onboarding email |

**YouTube SEO:** title format "[Jurisdiction] + [Topic] + [Year]". Description: first 150 characters are the snippet — lead with the most important information. Add timestamps for videos over 3 minutes.

## Accessibility

All videos must have:
- Closed captions (auto-generated then reviewed for legal terminology accuracy)
- Transcripts published alongside the video
- For Arabic-language content: Arabic subtitles reviewed by a native Arabic speaker with legal knowledge

## Legal accuracy compliance

Every video that makes a legal statement must:
1. Be reviewed by a qualified lawyer before publication
2. Include a verbal disclaimer: "This content is for informational purposes only and does not constitute legal advice."
3. Be dated — legal rules change, and viewers need to know when the content was produced
4. Be reviewed and updated (or marked "may be outdated") when the underlying law changes

## Related skills

- [[outreach-haqq-ai-viz]]
- [[outreach-blog-preview-renderer]]
- [[outreach-growth-agent-runner]]
- [[outreach-backlink-pr-campaign]]
