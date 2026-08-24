---
name: onboarding-template-of-the-day
description: Use when a new user is in their first week of using a legal AI assistant and the system must surface a daily micro-prompt or featured template to build habit, expand discovered capabilities, and reduce early churn. The template-of-the-day is a lightweight daily engagement nudge — one relevant document template or legal task — displayed on the home screen or in a daily notification during the first 7 days of use.
license: MIT
metadata: " id: onboarding.template-of-the-day category: onboarding jurisdictions: [__multi__] priority: P2 intent: [onboarding, engagement, habit, template, progressive-disclosure, first-week] related: [onboarding-empty-state-prompts, onboarding-first-prompt-suggestion-by-persona, onboarding-feature-discovery-tour, onboarding-persona-detection-questions] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'onboarding'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Onboarding — Template of the Day

## When this applies

The template-of-the-day (TOTD) is a **day 1–7 onboarding micro-flow** that surfaces one featured legal template or task prompt per day to new users. It is part of the week-one progressive onboarding arc (referenced as `unlock.first-week-progressive-tour`). Its purpose is narrow and specific:

1. **Habit formation**: give new users a reason to return each day during the critical first week
2. **Progressive capability disclosure**: each day reveals a different product capability, preventing the feature-dump problem of showing everything at once
3. **Reducing early churn**: the #1 churn trigger for legal AI is "didn't know what to do next" — TOTD solves this
4. **Persona-appropriate depth**: templates escalate from simple (day 1) to complex (day 7) as the user gains confidence

TOTD is a **suggestion**, not a requirement. It appears on the home screen as a highlighted card and optionally as a push notification. It is dismissible and will not reappear after dismissal.

---

## Behavior — The Daily Card

Each day, one template card appears on the home screen. The card contains:

| Element | Content |
|---------|---------|
| Label | "Today's template" |
| Template name | Short, descriptive (e.g., "Simple NDA — vendor relationship") |
| One-line description | What the template does and when it is useful |
| Jurisdiction tag | Applicable jurisdiction(s) |
| Persona tag | Who it is for (optional; only if persona-specific) |
| CTA | "Use this template" → opens pre-populated composer or drafting board |
| Secondary CTA | "Not today" → dismisses the card; does not count as a "use" |

The card refreshes at midnight local time. If the user uses the template on day 3, day 4's template is still shown (TOTD is a daily suggestion, not a reward for completion).

---

## 7-Day Template Sequence

The default sequence escalates from simple documents (day 1) to more complex ones (day 7). The sequence is **persona-aware** — the table below shows the consumer default and the lawyer variation.

| Day | Consumer / SME template | Lawyer template |
|-----|------------------------|----------------|
| Day 1 | Basic NDA — mutual, simple | Mutual NDA — commercial relationship (standard market terms) |
| Day 2 | Employment offer letter review | Employment contract review checklist |
| Day 3 | Freelancer / service agreement | Services agreement — vendor-side review |
| Day 4 | Tenancy / lease explainer | Commercial lease — key terms summary |
| Day 5 | Simple will / estate planning starter | Shareholders agreement — key clauses overview |
| Day 6 | Business formation FAQ | Cross-border contract — governing law and dispute resolution |
| Day 7 | Data privacy consent template | Data processing agreement — controller / processor |

**Jurisdiction personalisation:** Where the user's jurisdiction is set, templates are pre-configured for that jurisdiction (e.g., "NDA — mutual, UAE law" rather than generic "mutual NDA"). This increases relevance and reduces the friction of jurisdiction selection before using the template.

---

## Notification Logic

| Notification type | Condition | Timing |
|------------------|-----------|--------|
| In-app home card | Always | Shown on every home screen visit |
| Push notification | User has opted in to notifications | 9:00 AM local time, Monday–Friday only |
| Email digest (optional) | User has opted in to email | Once during the 7-day window (day 3 or 4); not daily |

**Do not** send a push notification on weekends unless the user's locale treats Saturday/Sunday as working days (e.g., GCC — Sunday through Thursday work week).

---

## Anti-Patterns to Avoid

| Anti-pattern | Fix |
|---|---|
| Showing templates that are too advanced for a first-time user | Day 1 template must be genuinely simple — a basic NDA, not a cross-border M&A clause |
| Repeating the same template | Each day a distinct template; track user's template history |
| Forcing template use before the user can access the product | TOTD is a suggestion on the home screen; never a gate |
| Sending daily push notifications after day 7 | TOTD is a first-week feature only; notifications stop after day 7 (or earlier if the user dismisses) |
| Ignoring persona | A consumer user should not see "cross-border M&A integration checklist" on day 1 |

---

## Analytics — Success Metrics

Track these metrics to assess and improve TOTD:

| Metric | Target |
|--------|--------|
| TOTD card impression rate | >80% of day-1 to day-7 users see at least one TOTD card |
| TOTD click-through rate | >30% of impressions result in "Use this template" click |
| Day-7 retention | Users who used ≥3 TOTD templates retain at 7 days at higher rate than those who used 0 |
| Template completion rate | % of users who clicked "Use this template" and produced a first draft |

Low click-through on a specific day → the template is not relevant or is too complex for that day in the sequence → swap template and re-test.

---

## Integration with the Broader Onboarding Arc

TOTD is one layer of the week-one progressive onboarding. The full arc:
1. **Day 0**: [[onboarding-feature-discovery-tour]] (synchronous tour on first sign-in)
2. **Days 1–7**: Template of the Day (daily async nudge)
3. **Day 3–5**: Skills discovery nudge (surface the skills library based on usage patterns)
4. **Day 7+**: [[onboarding-persona-detection-questions]] re-surface if quiz was skipped
5. **Week 2+**: Regular product engagement; TOTD replaced by contextual feature discovery

---

## Related skills

- [[onboarding-empty-state-prompts]]
- [[onboarding-first-prompt-suggestion-by-persona]]
- [[onboarding-feature-discovery-tour]]
- [[onboarding-persona-detection-questions]]
- [[onboarding-b2c-vs-b2b-fork]]
