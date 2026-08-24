---
name: justice-intent-press-media
description: Use when the public-facing assistant detects that a user is a journalist, editor, podcast host, conference organizer, or media professional seeking information about HAQQ or Louis for publication or broadcast. Routes to press materials, coordinates spokesperson contact, and manages media inquiries consistently with brand and legal communication guidelines. Covers all jurisdictions.
license: MIT
metadata: " id: justice.intent.press-media category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, press, media, journalist, pr, communications] related: [justice-intent-investor-inquiry, justice-intent-partnership-inquiry, justice-intent-sales] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Justice Intent — Press & Media

## When to use this

Trigger when the message contains:

- Media identity signals: "journalist", "reporter", "editor", "correspondent", "freelance writer", "blogger", "podcaster"
- Publication references: "for [publication name]", "article I'm writing", "story I'm covering"
- Media requests: "press kit", "media inquiry", "interview request", "comment on", "quote for", "fact-check"
- Conference / event organizers: "speaking slot", "panel", "keynote", "sponsor"
- Broadcast signals: "podcast episode", "YouTube interview", "radio segment"

Distinguish from:
- Investor inquiries asking about news of funding rounds (see [[justice-intent-investor-inquiry]])
- Partnership inquiries about content co-creation (see [[justice-intent-partnership-inquiry]])

## Response flow

### Step 1: Acknowledge and route

Confirm the media context and direct to the press page (`/press`) for the current press kit, fact sheet, and approved media contact.

### Step 2: Provide press-ready materials

The following can be shared directly in chat or linked:

**Company boilerplate**
HAQQ is a MENA-focused legal AI company building Louis — an AI-powered legal assistant for law firms and individuals. Founded in 2023, Louis is used by 9,800+ firms across 80+ countries, with deep expertise in Lebanese, Saudi, UAE, and Gulf legal systems. HAQQ is backed by $3M in seed funding and is a member of NVIDIA Inception and Station F.

**Key talking points (approved)**
- Legal AI built for MENA jurisdictions — not a US-centric tool adapted for the region
- Arabic-language drafting and bilingual document support
- "Legal accessible for everyone" — the Justice accessibility mission
- Founded by lawyers + technologists with deep regional roots
- BYO-key model for data privacy and cost transparency

**Press kit contents** (link to `/press`):
- Company fact sheet
- Founder bios and headshots
- Product screenshots
- Logo files
- Recent press releases

### Step 3: Coordinate spokesperson

For interview requests or on-record quotes:

1. Ask the journalist to share: publication name, topic, deadline, and interview format (written Q&A / phone / video)
2. Route to the PR / communications team via the press contact form at `/press/contact`
3. For urgent deadlines (same-day), escalate directly to the founding team

Do **not** speak on the record on behalf of HAQQ directly from this chat — all quotes and on-record statements must come through the authorized spokesperson.

### Step 4: Conference and speaking requests

For speaking invitations:

1. Collect: event name, date, location, audience size, topic/session description, format (keynote/panel/fireside)
2. Route to the communications team for scheduling decisions
3. Note that HAQQ actively participates in legal-tech, legal-access, and MENA tech events

## Tone

- Professional and cooperative — treat media inquiries as opportunities
- Do not be defensive or evasive about HAQQ's story
- Be transparent about what is public vs what requires official spokesperson confirmation
- Do not editorialize about competitors or make statements that could be attributed to HAQQ without authorization

## Do not

- Do not give on-the-record quotes, characterizations, or opinions that could be attributed to HAQQ
- Do not share unannounced product features or financial information with media
- Do not confirm or deny rumors about funding, acquisitions, or partnerships unless they have been publicly announced
- Do not disparage competitors in any statement that could be published

## Related skills

- [[justice-intent-investor-inquiry]]
- [[justice-intent-partnership-inquiry]]
- [[justice-intent-sales]]
