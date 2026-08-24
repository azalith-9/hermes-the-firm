---
name: voice-brand-podcast-show-notes
description: Use when generating show notes for a podcast episode featuring HAQQ Legal AI content, legal tech topics, MENA legal market commentary, or founder conversations. This skill defines the exact structure, word count, SEO requirements, timestamp format, pull-quote selection, and subscribe CTAs for podcast show notes that drive discovery and return listeners.
license: MIT
metadata: " id: voice-brand.podcast-show-notes category: voice-brand priority: P1 intent: [__voice-brand__, podcast, show-notes, content-marketing, SEO] related: - voice-brand-youtube-video-description - voice-brand-press-release-tone - voice-brand-linkedin-post-stephane source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice-brand'.
Registered as a flat plugin skill.
-->


# Podcast Show Notes

## When this applies

Use this skill when generating show notes for any podcast episode — whether a standalone HAQQ/Louis podcast, a guest appearance on another show, or a thought-leadership episode about the MENA legal market or LegalTech. The show notes serve two audiences simultaneously: search engines (SEO discovery) and existing subscribers (value delivery and navigation).

## Structure

Every episode's show notes contain these sections in this order:

### 1. Title
SEO-optimized. Should contain the episode's core topic and, where applicable, the guest's name and a specific angle.

- Good: "How AI is Changing Contract Review in the UAE — with [Guest Name], GC at [Company]"
- Bad: "Episode 12 — Great conversation with a legal expert"

The title should be usable as a web page `<title>` tag and as the podcast platform listing title.

### 2. Episode summary (1 paragraph)
A 3–5 sentence synopsis covering:
- Who is the guest (role, expertise, why they were invited).
- The central question or topic of the episode.
- The two or three most important insights or conclusions.

This paragraph appears in podcast directories and search results. Write for a reader who has not heard the episode and is deciding whether to listen.

### 3. Guest bio
- 2–4 sentences.
- Focus on credentials relevant to the episode topic, not the full LinkedIn profile.
- Include a link to their website, LinkedIn, or firm profile.
- If no guest, describe the host(s) briefly.

### 4. Key topics with timestamps

Format: `MM:SS — [Topic description]`

Example:
```
00:00 — Introduction and guest background
04:20 — Why MENA legal ops are still largely manual
11:45 — How AI contract review works in practice
22:10 — DIFC vs. onshore UAE: key contract differences
34:00 — Where the MENA legal market is heading in five years
42:30 — Rapid fire: three tools every GC should try
```

Aim for 6–12 timestamps. Timestamps should mark genuine topic shifts, not every sentence.

### 5. Mentioned resources

Everything the guest or host referenced:
- Books (title + author + link)
- Articles or reports (title + publication + link)
- Tools or products (name + URL)
- Cases or statutes mentioned (full citation where possible)

Present as a linked list. Do not omit resources that were mentioned — this section is valuable for listeners who want to go deeper.

### 6. Pull quotes

3–5 direct quotes from the episode. These are used:
- In social media promotion (LinkedIn, X/Twitter)
- In the email newsletter promotion of the episode
- As featured quotes on the episode page

Select quotes that are:
- Standalone (make sense without the full context)
- Memorable or surprising
- Quotable in one or two sentences (under 30 words ideally)

Format: `> "[Quote]" — [Name], [Role]`

### 7. Subscribe + share CTAs
- Links to subscribe on each major platform (Apple Podcasts, Spotify, YouTube, Google Podcasts, or whichever are active).
- Invitation to leave a review with a note on why it matters.
- Optional: link to share the episode.

Keep this section short and functional — one line per link.

## Length and tone

- Total word count: **500–1,000 words** (excluding the timestamps list, which can be long).
- Tone: professional but accessible. Not as formal as a legal document; not as casual as a tweet. Think: smart publication's podcast page.
- Write in third person for the summary and bio sections; first person ("we discussed", "I asked") is acceptable in the timestamp labels.

## SEO considerations

- Include the guest's name and their organization in the title and opening paragraph (these are common search terms).
- Include the episode's geographic or jurisdictional focus (e.g., "UAE", "MENA", "Saudi Arabia") where relevant — these are long-tail search terms.
- Link to related episodes within the show notes to improve internal linking.

## Related skills

- [[voice-brand-youtube-video-description]]
- [[voice-brand-press-release-tone]]
- [[voice-brand-linkedin-post-stephane]]
- [[voice-brand-tweet-thread-launch]]
