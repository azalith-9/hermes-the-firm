---
name: voice-brand-press-release-tone
description: Use when drafting a press release for HAQQ Legal AI / Louis — product launches, funding announcements, partnership news, new market entries, or executive appointments. This skill defines the AP-style press release format, tone rules, headline standards, quote conventions, boilerplate language, and MENA-specific distribution considerations.
license: MIT
metadata: " id: voice-brand.press-release-tone category: voice-brand priority: P1 intent: [__voice-brand__, press-release, PR, media, announcements] related: - voice-brand-linkedin-post-stephane - voice-brand-tweet-thread-launch - voice-brand-email-investor-update source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'voice-brand'.
Registered as a flat plugin skill.
-->


# Press Release Tone and Format

## When this applies

Use this skill when drafting press releases for:
- Product launches and major feature releases
- Funding rounds (seed, Series A, strategic)
- Partnerships, integrations, or distribution agreements
- Awards, certifications, or regulatory approvals
- Executive hires or board appointments
- New market entries (e.g., launching in KSA or Egypt)

## Standard format

Press releases follow a rigid, widely understood structure. Journalists scan them for the five Ws in order. Do not deviate from the structure.

### 1. Headline
- Factual, specific, and benefit-oriented — not a question, not clickbait.
- Format: `[Company] [Does/Announces/Launches] [Specific Thing] [Context]`
- Good: "HAQQ Legal AI Launches Arabic-Language Contract Review for GCC Law Firms"
- Bad: "The Future of Legal AI Has Arrived in the Middle East"
- Length: 80 characters or fewer for wire distribution.

### 2. Subhead (optional but recommended)
- One sentence that adds a key detail or context the headline could not fit.
- Example: "Platform is the first legal AI to offer fully bilingual Arabic-English contract analysis optimized for UAE and KSA jurisdictions."

### 3. Dateline
Format: `DUBAI, [Month Day, Year] —`
- Use the city where the company's primary office or the news originates.
- If a DIFC or ADGM address, still use "DUBAI" as the city.
- For Beirut-originating news: "BEIRUT, Lebanon —"

### 4. Lead paragraph
Must answer: What happened? Who did it? When? Where? Why does it matter?

All five answers in one tight paragraph (2–4 sentences). This is the paragraph a journalist may quote or reprint as the full story. It must stand alone.

Example:
> HAQQ Legal AI today launched Louis Pro, an AI-powered contract review platform purpose-built for MENA law firms, at GITEX Global in Dubai. The platform supports Arabic, English, and French contracts and provides clause-by-clause analysis calibrated to UAE federal law, DIFC, ADGM, and KSA commercial regulations. HAQQ Legal AI says early customers have reduced contract review time by an average of 65%.

### 5. Quote — CEO or relevant executive
- One compelling, attributable quote from the CEO, CTO, or the most relevant executive.
- The quote must add perspective or meaning — it should not repeat the lead paragraph.
- Write the way the executive actually talks, not in stiff corporate boilerplate.
- Good: "'Law firms in the Gulf have been underserved by AI tools built for US or UK markets. Louis was designed from day one for how MENA lawyers actually work,' said Stephane Boghossian, CEO of HAQQ Legal AI."
- Bad: "'We are proud to announce this exciting milestone that represents our commitment to excellence in the legal AI space.'"

### 6. Body paragraphs (2–4 paragraphs)
- Additional context: market size, problem being solved, how the product works at a high level.
- Supporting data: statistics, research, benchmarks, customer validation.
- A second quote from a customer, partner, or industry figure where available.

### 7. Company boilerplate
A standard two-to-three sentence description of HAQQ Legal AI that appears at the end of every press release. Keep it consistent — media databases store this for future coverage.

Example:
> About HAQQ Legal AI: HAQQ Legal AI builds AI-powered legal tools purpose-built for MENA and international markets. Its flagship product, Louis, supports Arabic, English, and French legal documents across UAE, KSA, Lebanon, Egypt, and GCC jurisdictions. The company is headquartered in Dubai and Beirut. Learn more at [website].

### 8. Contact information
- Name of the PR or media contact.
- Email address (a monitored inbox, not a personal address that may not be watched).
- Phone number (optional, but expected by wire services).

## Tone rules

| Do | Avoid |
|----|-------|
| Third-person throughout (never "we" or "I") | First-person voice |
| Factual and specific | Superlatives without evidence ("best", "most innovative") |
| Attribution for all claims | Unattributed statistics |
| Active voice in most sentences | Passive where the actor is clear |
| Length: 400–600 words | Longer without reason (funding announcements can run to 700) |

## MENA distribution considerations

- **Language**: issue in English as the primary release; issue a separate Arabic-language version (not a bilingual single release) for Arabic-language media (Al Arabiya Business, Gulf Business Arabic edition, regional newswires).
- **Wire services active in MENA**: PR Newswire MENA, Gulf News PR, WAM (for UAE government-related news), Saudi Press Agency (for KSA news).
- **Timing**: avoid Fridays (MENA weekend) and the last ten days of Ramadan — media coverage drops significantly.
- **Embargo requests**: MENA media organizations generally honor embargoes, but confirm the embargo terms explicitly in writing.

## Related skills

- [[voice-brand-linkedin-post-stephane]]
- [[voice-brand-tweet-thread-launch]]
- [[voice-brand-email-investor-update]]
- [[voice-brand-podcast-show-notes]]
