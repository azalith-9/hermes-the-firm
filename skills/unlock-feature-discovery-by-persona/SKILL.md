---
name: unlock-feature-discovery-by-persona
description: Use when the platform needs to surface relevant features to a newly onboarded user based on their persona (partner, associate, in-house counsel, law student, or consumer). This skill governs the pacing, sequencing, and content of per-persona feature reveals during the first 28 days, ensuring each user type encounters the capabilities most relevant to their work without being overwhelmed.
license: MIT
metadata: " id: unlock.feature-discovery-by-persona category: unlock priority: P0 intent: [__unlock__, onboarding, feature-discovery, persona-routing] related: - unlock-first-week-progressive-tour - unlock-skill-of-the-day - onboarding-feature-discovery-tour source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'unlock'.
Registered as a flat plugin skill.
-->


# Feature Discovery by Persona

## Purpose

New users do not all need the same features on day one. A partner managing a matter team needs the workspace and billing features first; a law student needs the IRAC coach and exam tracks. Surfacing the wrong capability too early creates noise; surfacing it too late means the user never discovers it.

This skill defines the canonical per-persona reveal schedule for Louis: what to surface, when to surface it, and the governing rules that prevent over-messaging.

## Personas and reveal schedule

### Partner (B2B senior — law firm partner or senior lawyer)

| Day | Feature unlocked |
|-----|-----------------|
| 1 | Document workspace + matter context setup |
| 3 | Skills router + observability dashboard |
| 7 | Firm KB integration + playbook customization |
| 14 | eFirm features (matter tracking, billing automation, team management) |
| 21 | Word plugin (draft and review without leaving Word) |
| 28 | Mobile app (full feature parity on iOS/Android) |

Partners are time-constrained and profit-conscious. Lead with productivity and business-impact features. Defer personal workflow tools until they are comfortable with the core.

### Associate (B2B mid — junior to mid-level lawyer)

| Day | Feature unlocked |
|-----|-----------------|
| 1 | Drafting + review templates (quickest path to value) |
| 3 | Skills library exploration (breadth discovery) |
| 7 | Personalization for personal workflow |
| 14 | Drafting board for complex multi-party matters |
| 21 | Mobile app |
| 28 | Pro / Business upgrade prompt (based on usage signals) |

Associates are heavy drafters and reviewers. They benefit from breadth early but need the advanced collaboration features only once they have built a habit.

### In-house counsel

| Day | Feature unlocked |
|-----|-----------------|
| 1 | Vendor contract review (immediate ROI on the most common task) |
| 3 | Friday newsletter pattern (legal updates for the business) |
| 7 | Internal client communication templates |
| 14 | Compliance gap checker |
| 21 | Multi-jurisdictional comparison tools |
| 28 | Team rollout pitch deck (for internal legal ops expansion) |

In-house users manage upward and laterally, not just legal work. Surface features that help them communicate legal risk to non-lawyers and justify the tool's existence internally.

### Law student (Justinian track)

| Day | Feature unlocked |
|-----|-----------------|
| 1 | IRAC coach + case explainer |
| 3 | Bar exam track selection (jurisdiction-specific) |
| 7 | Flashcard generation from statutes |
| 14 | Practice essays with AI grading + rubric feedback |
| 21 | Moot court rehearsal mode |
| 28 | Future-career planning and path options |

Students need scaffolded learning, not raw legal power tools. Match the reveal cadence to academic calendar rhythms where possible.

### Consumer (Louis Twin — self-represented or advice-seeking individual)

| Day | Feature unlocked |
|-----|-----------------|
| 1 | First question answered + empathic onboarding experience |
| 3 | Follow-up matter awareness (track open issues) |
| 7 | When to escalate to a real lawyer (guidance + referral) |
| 14 | Related-issues exploration (adjacent problems the user may not have raised) |
| 21 | Free public tools catalog (public-tool skills accessible without subscription) |

Consumer users are often anxious and legally unsophisticated. Empathy and clarity come before feature depth. Never surface billing or firm features to this persona.

## Governing rules

### Pacing
- **Maximum one feature reveal per day** — do not stack reveals even if the user is highly active.
- Reveals are delivered via in-app cards at login or at the natural moment of relevance (e.g., surface eFirm features when the user first creates a matter, not on a fixed calendar).

### Skip logic
- **Do not surface a feature the user has already discovered organically.** Track capability-trigger events (first document upload, first skill use, first billing interaction) and mark those branches as complete.
- **Allow user-driven discovery to override the schedule.** If the user organically reaches a day-14 feature on day 3, do not retroactively surface it again on day 14.

### Engagement tracking
Record the following for each reveal event:
- Feature ID and persona
- Surface date vs. scheduled date
- Whether the user clicked through or dismissed
- Whether the user actually used the feature within 7 days

Low click-through on a reveal warrants revisiting the copy or the timing, not suppression of the feature entirely.

### Persona detection
Persona is set at registration. It can be inferred or refined from:
- Account type (B2B firm seat vs. individual vs. student email domain)
- First queries (drafting a contract vs. asking about bar prep vs. consumer question)
- Explicit self-selection during onboarding

When persona is ambiguous, default to the associate track — it is the broadest and least likely to confuse.

## What to avoid

- Do not send competing reveals from two different personas if a user changed their persona mid-onboarding.
- Do not surface enterprise-tier features (eFirm, team management, billing) to consumer or student users — this creates confusion and devalues those features.
- Do not treat the schedule as a hard cron job. Contextual triggers outperform calendar-based delivery every time.

## Related skills

- [[unlock-first-week-progressive-tour]]
- [[unlock-skill-of-the-day]]
- [[onboarding-feature-discovery-tour]]
- [[unlock-power-user-shortcuts]]
