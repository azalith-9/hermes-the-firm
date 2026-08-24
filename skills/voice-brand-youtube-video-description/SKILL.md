---
name: voice-brand-youtube-video-description
description: Use when writing a YouTube video description for HAQQ Legal AI content — product demos, explainer videos, legal education content, founder interviews, or MENA legal market commentary. This skill defines the SEO-optimized hook, description structure, chapter timestamp format, link requirements, and subscribe CTA for descriptions that drive both discovery and watch-time.
license: MIT
metadata: " id: voice-brand.youtube-video-description category: voice-brand priority: P1 intent: [__voice-brand__, youtube, video-description, SEO, content-marketing] related: - voice-brand-podcast-show-notes - voice-brand-tweet-thread-launch - voice-brand-linkedin-post-stephane source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice-brand'.
Registered as a flat plugin skill.
-->


# YouTube Video Description

## When this applies

Use this skill when writing a YouTube description for any video on the HAQQ Legal AI / Louis channel: product demos, legal explainers, interview episodes, tutorial content, or event coverage.

YouTube descriptions serve two functions: (1) they influence the YouTube search algorithm, and (2) they give viewers who land on the page the information needed to decide whether to watch and where to find referenced resources.

## Structure

### 1. Hook — first 100–150 characters
The most critical section. YouTube shows only the first ~100 characters in search results and the first 2–3 lines before the "Show more" fold on the video page.

- State the core value of the video immediately.
- Include the most important keyword for this topic.
- Good: "How to review a UAE employment contract in under 2 minutes using AI — full walkthrough."
- Bad: "In this video we'll be taking a look at some of the things you can do with our platform."

Do not waste the hook on a generic opener.

### 2. Episode / video summary
2–4 sentences expanding on what the video covers. Write for a viewer who has not watched yet and is deciding whether it is worth their time.

Include:
- The specific topic or question the video answers.
- Who the audience is (lawyers in the UAE, law students, in-house counsel).
- What the viewer will be able to do or know after watching.

### 3. Chapter timestamps
YouTube automatically creates a chapter navigation bar when timestamps are in the description. Use this feature for videos over 5 minutes.

Format:
```
0:00 Introduction
1:30 The problem with manual contract review
4:15 Live demo — uploading a UAE employment contract
8:45 Reading the AI analysis output
12:20 How jurisdiction affects the analysis
16:00 Summary and next steps
```

Rules:
- Must start with `0:00`.
- At least three timestamps are required for YouTube to render the chapter bar.
- Chapter titles should be descriptive, not generic ("Part 1", "Section 2" are unhelpful).

### 4. Mentioned links
List every resource referenced in the video:
- Platform sign-up / free trial link (always first).
- Blog posts, whitepapers, or tools mentioned.
- Guest's LinkedIn, website, or firm profile.
- Related videos on the channel.

Format as plain URLs followed by a short description:
```
Try Louis for free: https://...
Blog post on UAE employment law: https://...
Guest's LinkedIn: https://...
```

### 5. Social and channel links
- LinkedIn, X (Twitter), website.
- Channel subscribe button + notification bell reminder: "Subscribe for weekly MENA legal AI content."

Keep this section brief — it is functional, not narrative.

## SEO considerations

- Include the main keyword phrase in the first 100 characters.
- Use secondary keywords naturally within the summary section (do not keyword-stuff).
- MENA-specific content should name specific jurisdictions (UAE, DIFC, KSA, Dubai, Riyadh) — these are long-tail search terms with high intent from the target audience.
- Video topic, guest name, and company name are all indexable in YouTube search — include each where relevant.

## Tone

- Plain and direct. This is a utility document for viewers, not marketing copy.
- Do not write the description in first person ("I talk about…") or second person ("You will learn…") — third person or imperative works better ("This video covers…" or "Watch to learn…").
- Match the register of the video content — a technical deep-dive for lawyers warrants more formal language than a product demo for general audiences.

## Length

- Minimum: 150 words (enough to provide context and support YouTube's indexing).
- Target: 250–400 words.
- Maximum: YouTube shows 5,000 characters but descriptions beyond 500 words rarely add indexing value.

## Related skills

- [[voice-brand-podcast-show-notes]]
- [[voice-brand-tweet-thread-launch]]
- [[voice-brand-linkedin-post-stephane]]
- [[voice-brand-press-release-tone]]
