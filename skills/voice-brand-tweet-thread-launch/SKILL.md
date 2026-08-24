---
name: voice-brand-tweet-thread-launch
description: Use when drafting a launch announcement thread on X (Twitter) for a HAQQ Legal AI product release, feature launch, or major company milestone. This skill defines the 8–12 tweet structure, hook writing, proof-point sequencing, visual placement, and mobile-optimization rules for a launch thread that drives sign-ups and shares.
license: MIT
metadata: " id: voice-brand.tweet-thread-launch category: voice-brand priority: P1 intent: [__voice-brand__, twitter, launch-thread, social-media, product-launch] related: - voice-brand-linkedin-post-stephane - voice-brand-press-release-tone - voice-brand-youtube-video-description source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice-brand'.
Registered as a flat plugin skill.
-->


# Tweet Thread — Launch Announcement

## When this applies

Use this skill for major launch announcements on X (formerly Twitter): new product releases, significant feature drops, funding announcements, or company milestones. The launch thread is a distinct format from a single promotional tweet — it is 8–12 connected tweets that tell a story, building from hook to proof to invitation.

## Thread structure (8–12 tweets)

### Tweet 1 — Hook / announcement headline
The single most important tweet. The rest of the thread is only read if this lands.
- State the announcement plainly and with impact.
- Front-load the most compelling element.
- Good: "We just launched the first Arabic-native AI contract review platform. Thread 🧵"
- Bad: "Excited to announce something we've been working on for months. Stay tuned!"
- Do not save the news for tweet 3. Announce in tweet 1.

### Tweet 2 — Why this matters (the problem)
Context for readers who are not already sold.
- Name the problem being solved, specifically.
- Use a concrete number or market fact where possible.
- Example: "MENA law firms review hundreds of contracts a month. Most are still done manually, in Arabic and English, without AI tools built for local law."

### Tweet 3 — What was built (key features)
A tight description of the product or feature.
- 2–4 bullet points or a short paragraph.
- Features should be described in terms of outcomes, not technical specifications.
- "Review a UAE employment contract in under 2 minutes" is better than "Sub-2-minute inference at 99k tokens/s."

### Tweet 4 — Proof point
Social proof, benchmark data, or a customer outcome.
- A real result from a real user (anonymized or with permission).
- A performance benchmark from testing.
- A relevant market statistic.
- Example: "One partner at a Dubai law firm told us they cut their contract review time by 65% in the first week."

### Tweets 5–8 — Detail, behind the scenes, or depth
This is where the thread earns trust for the people who read all the way through. Options:
- How a key technical or design decision was made.
- A jurisdiction-specific insight (why MENA matters, what makes this different from US-centric tools).
- A mini-demo in screenshots or video.
- The story behind a specific feature.
- A "what we got wrong first" transparency moment.

One tweet per topic in this section. Keep each tweet self-contained — a reader should be able to understand it without reading the previous tweet.

### Tweet 9 — Roadmap teaser
What comes next. Brief and specific enough to be credible; not so detailed as to over-promise.
- Example: "Next up: Word plugin (June) and a KSA-specific regulatory library (Q3)."

### Tweet 10 — Founders' tag and thanks
Acknowledge the team, advisors, beta users, investors, or anyone who contributed. Tag where appropriate.
- Keep it genuine — a list of tags with no context feels like SEO spam.

### Tweets 11–12 — CTA
- Primary CTA: sign up, try the product, request a demo.
- Secondary CTA: share / retweet the thread, tag someone who should see it.
- Include a link (last tweet, not the hook tweet — links in tweet 1 can hurt algorithmic reach on some platforms).

## Format and mobile optimization

- **Character limit**: every tweet must be under 280 characters including spaces and the thread marker.
- **Visuals**: include an image, GIF, or short video clip every 2–3 tweets. Launch threads with no visuals see significantly lower engagement.
- **Numbering**: optional but helpful for long threads — "1/" at the end of the first tweet lets readers know it continues.
- **Line breaks**: use blank lines generously within tweets. Dense text blocks do not perform well on mobile.
- **Hashtags**: 0–2 per tweet, only if they are genuinely used by the target audience. Do not tag MENA with #MiddleEast — use #UAE, #KSA, #DIFC, or #MENA for accuracy.

## What not to do

- Do not save the announcement for a later tweet in the thread.
- Do not use vague superlatives ("most powerful", "game-changing", "revolutionary").
- Do not include more than one link per tweet (the algorithm deprioritizes multi-link tweets on most platforms).
- Do not write tweets that only make sense if you have read the previous tweet — each tweet should be partially standalone.

## Related skills

- [[voice-brand-linkedin-post-stephane]]
- [[voice-brand-press-release-tone]]
- [[voice-brand-youtube-video-description]]
- [[voice-brand-podcast-show-notes]]
