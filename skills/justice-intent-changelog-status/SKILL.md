---
name: justice-intent-changelog-status
description: Use when a user asks about recent product updates, feature releases, what's new in Louis, the development roadmap, known issues, or the current status of a requested feature. Handles changelog queries, roadmap transparency, feature-request acknowledgment, and bug/issue status updates. Routes to the appropriate channel (public changelog, status page, GitHub issues) and provides a structured, honest update within the bounds of what can be disclosed.
license: MIT
metadata: " id: justice.intent.changelog-status category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, changelog, product-updates, roadmap, feature-request, status, release-notes] related: [justice-intent-book-call, justice-intent-career-application, justice-human-handoff] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Justice Intent — Changelog & Status

## When this applies

This intent fires when a user asks about:
- What has changed or been released recently in Louis
- Whether a specific feature they requested has been built
- The current status of the platform (downtime, degraded performance)
- The product roadmap and upcoming features
- A known bug or issue and when it will be fixed

It is a **product transparency and user communication flow** — part of HAQQ's accessibility and trust-building mission.

---

## Context: Justice as accessibility

The "Justice" category covers HAQQ's accessibility mission. Changelog transparency is part of accessibility: users — especially the legal professionals and underserved individuals who depend on Louis — deserve to know what the tool can and cannot do, what is changing, and how to give feedback. Opacity erodes trust; transparency builds it.

---

## Detection patterns

### Strong signals
- "What's new in Louis?"
- "Have you added [feature] yet?"
- "I requested [feature] — is it on the roadmap?"
- "The system seems slow / broken — is there an outage?"
- "What's the latest update?"
- "What version are you on?"
- "Is [bug/issue] fixed yet?"

### Moderate signals (confirm before routing)
- "Does Louis support X?" — could be capability question, not changelog
- "I noticed this changed" — investigate first, then confirm if it's a known change or a bug

---

## Behavior

### Step 1: Identify the query type
| Query type | Routing |
|---|---|
| Recent releases / what's new | Public changelog or release notes link |
| Feature request status | Acknowledge; check roadmap; give honest answer |
| Known bug / issue | Acknowledge; provide status; give ETA if available |
| Platform outage / performance | Route to status page; provide incident status |
| Roadmap inquiry | Share what can be disclosed; explain what is on the horizon |

### Step 2: Respond honestly and specifically

**For changelog queries:**
"Here's what's been updated recently in Louis: [link to changelog or summary of recent releases]. The most recent release included: [top 2–3 changes]."

**For feature request status:**
- If feature is on the roadmap: "Yes, [feature] is planned. Based on current priorities, we expect to release it in [timeframe or 'next quarter']. I'll note your interest."
- If feature is not yet committed: "That's not on the current roadmap, but it's a great suggestion. You can submit it at [feedback channel] and the team reviews all requests."
- If feature request was already received: "We have this in our backlog — thank you for the reminder. I can't promise a specific date, but it has been logged."

**For bug/issue status:**
- If known issue: "Yes, this is a known issue. The team is working on it. Current status: [investigating / fix in progress / fix deployed in vX.X]."
- If not recognized: "I don't see a known issue matching that description. Can you share more details? I'll escalate to the team."

**For platform status/outage:**
"Check our status page at [status.haqq.ai or equivalent] for real-time uptime information. If you're seeing an issue not reflected there, please report it at [support channel]."

### Step 3: Capture feedback (if applicable)
If the user has a feature request or bug report:
- Confirm: "Would you like me to log this as feedback for the product team?"
- If yes: capture the request in structured form and route to the feedback pipeline
- Acknowledge: "Done — the product team reviews all feedback. Thank you."

---

## Changelog format

When providing a changelog summary, use this structure:

```
## Louis — Recent Updates

### [Version X.X / Month Year]
- **New**: [Feature name] — [1-line description]
- **Improved**: [Feature name] — [1-line description]
- **Fixed**: [Issue] — [1-line description]

### [Previous version / date]
...
```

If no structured changelog is available, summarize the most significant recent changes in plain language: "The most notable recent change is [X], which [benefit to user]."

---

## Do not

- Do not promise features that are not committed on the roadmap
- Do not give ETAs you cannot stand behind — "we're working on it" is better than a specific date that gets missed
- Do not dismiss feature requests — always acknowledge and route to feedback channel
- Do not be evasive about known bugs — honesty about known issues builds more trust than denial
- Do not disclose confidential roadmap items (competitive or strategic plans not intended for public disclosure)

---

## Roadmap disclosure guidelines

| Item | Can disclose | Cannot disclose |
|---|---|---|
| Features announced publicly or in beta | Yes | — |
| Features in the public GitHub issues / roadmap | Yes | — |
| Internal sprint items not yet announced | No | Keep as "in progress" |
| Strategic partnerships not yet announced | No | "We're exploring partnerships in this space" |
| Pricing changes | Only if already announced | — |
| Upcoming jurisdictions | Only if publicly committed | — |

---

## Edge cases

| Scenario | Handling |
|---|---|
| User is angry about a missing feature | Acknowledge their frustration; explain the current status honestly; offer a workaround if one exists; log the escalated feedback |
| User claims a feature was promised by the team | Verify: "Can you share more context about where you heard that?" — do not confirm or deny without checking |
| User asks about a competitor's feature | Confirm Louis's current capability; do not disparage competitors; log as potential feature gap if Louis doesn't have it |
| User asks for a live demo of a new feature | Route to [[justice-intent-book-call]] for a human-led demo |

---

## Related skills

- [[justice-intent-book-call]]
- [[justice-intent-career-application]]
- [[justice-human-handoff]]
