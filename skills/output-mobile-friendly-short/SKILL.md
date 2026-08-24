---
name: output-mobile-friendly-short
description: Use when the agent must adapt its output for mobile surfaces — short chat responses, in-app legal answers, or any context where the user is on a small screen or expects a concise result. Enforces hard word limits, removes wide tables, and strips verbose hedging. Triggers on mobile UI signals, short-form question context, or explicit brevity requests.
license: MIT
metadata: " id: output.mobile-friendly-short category: output intent: ['__format__', 'mobile', 'brevity', 'short-form'] related: - output-voice-friendly-short - output-partner-memo-style - output-irac-structure priority: P0 source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'output'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Mobile-Friendly Short Output

Legal AI on mobile has a fundamentally different contract with the user: they are not reading a memo, they are getting a quick answer — often one-handed, often mid-meeting. Dense paragraphs, wide tables, and exhaustive hedging all fail on a phone screen. This skill governs how the agent compresses without losing accuracy.

## When this applies

Activate when:
- The interface signals a mobile context (narrow viewport, app shell, voice trigger)
- The user asks a quick factual or triage question
- The task is a quick check rather than a formal deliverable
- The user explicitly requests "brief", "quick", "short", or "summarise"

Do **not** activate for:
- Formal document drafting (use [[output-markdown-legal-doc]])
- Full legal opinions (use [[output-irac-structure]] + [[output-partner-memo-style]])
- Research memos with citation requirements

## Hard limits

| Content type | Hard cap |
|---|---|
| Chat / question answers | 300 words |
| Draft documents in mobile | 800 words |
| Tables | Max 3 columns |
| Heading depth | Max H2 (no H3 or deeper) |
| Sentence length | ≤ 15 words preferred |

If an accurate answer cannot fit in 300 words, give the answer in 300 words and offer an expansion: "Need the full analysis? Ask me to expand."

## Structure rules

**Bottom line first.** Every mobile answer opens with the direct answer in one sentence. No preamble, no context restatement.

**Bullets over paragraphs.** Lists are faster to scan on a phone. Use them for any enumeration of 3+ items.

**Cut the context restatement.** Do not echo the user's question back. They know what they asked.

**One alternative, not several.** If options exist, give the best one and note "there are other approaches — tap to see." Do not present 3 parallel drafts.

**Sources at the bottom, not inline.** Citations are important but they disrupt reading on small screens. Collect them: "Sources: UAE FDL 33/2021 art 10; Cabinet Decision 1/2022" — at the bottom, one line.

## Confidence signal

Replace verbose hedging with a single confidence indicator:

| Signal | Meaning |
|---|---|
| ✅ | High confidence — well-established rule, directly applicable |
| ⚠️ | Moderate confidence — rule applies but fact-specific; legal review recommended |
| 🚫 | Low confidence — uncertain, actively contested, or jurisdiction unclear — do not act without qualified legal advice |

Place this indicator at the start of the answer, before the bottom line.

## What gets cut on mobile

- Long introductory context re-statements
- Multiple alternative draft options (offer one + expansion prompt)
- Extended qualification paragraphs ("it depends on X, Y, Z, and many other factors")
- Table of authorities / full citations (compressed to a Sources footer)
- Nested list hierarchies deeper than 2 levels

## What stays — always

- The direct answer
- The key legal rule with its jurisdiction and article reference
- The concrete next step or action
- Any critical warning (jurisdiction mismatch, missing facts, urgent deadline)

## Example — before and after

**Before (desktop-style):**
"This is a nuanced area of law. Under UAE Federal Decree-Law 33/2021 on the Regulation of Labour Relations, specifically Article 43, which deals with notice periods for fixed and indefinite term contracts, an employee working under an indefinite-term contract is entitled to a minimum notice period that depends on the length of service: 30 days for employees with less than 5 years of service, and the period may be extended by the contract..."

**After (mobile):**
✅ UAE notice period (indefinite-term contract):
- Under 5 years service: 30 days minimum notice
- 5+ years: check contract — may be longer
- Source: UAE FDL 33/2021 art 43

Need the full breakdown? Ask me to expand.

## Related skills

- [[output-voice-friendly-short]]
- [[output-partner-memo-style]]
- [[output-irac-structure]]
- [[output-inline-citations-with-pinpoints]]
