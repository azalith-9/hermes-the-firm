---
name: growth-push-notif-templates
description: Use when generating, selecting, or configuring push notification copy for the Louis mobile and web app. Provides a complete library of notification templates organized by type — re-engagement, matter-specific, skill discovery, credit warnings, and collaboration — along with channel specifications, frequency rules, and personalization guidance. Ensures notifications are specific, timely, and non-intrusive, respecting user preferences and quiet hours.
license: MIT
metadata: " id: growth.push-notif-templates category: growth priority: P0 intent: [__growth__, push-notifications, re-engagement, mobile, personalization] related: [growth-email-onboarding-sequence, growth-referral-prompt, growth-win-back-inactive, growth-nps-prompt] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'growth'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Growth — Push Notification Templates

## Purpose

Push notifications are the highest-immediacy channel in Louis's user communication stack. Used well, they bring users back at the exact moment a task, deadline, or collaborative action is waiting for them. Used poorly, they erode trust and drive uninstalls. This skill defines the template library, the rules, and the channel architecture.

## Notification types and templates

### Re-engagement (inactive user)

Triggered when a user has not opened the app in N days. Templates calibrated by days-since-last-use:

| Days inactive | Template | Tone |
|---|---|---|
| 3 days | "Your matters miss you. 3 new updates waiting." | Gentle reminder; implies work is pending |
| 7 days | "Quick legal question? Louis is ready in 1 tap." | Low-friction re-entry offer |
| 14 days | "Try the new [feature name]. Built for you." | Feature discovery; implies product has improved since last visit |
| 30+ days | See [[growth-win-back-inactive]] | Escalate to win-back sequence |

**Do not use** generic "We miss you!" copy — it reads as automated and impersonal. Every re-engagement notification should imply a specific, real reason to return.

### Matter-specific notifications

Triggered by matter-level events. These are the highest-value notifications because they are directly relevant to work in progress.

| Event | Template |
|---|---|
| Closing deadline approaching (3 days) | "Acme MSA closing in 3 days — review checklist?" |
| Filing deadline tomorrow | "Deadline tomorrow: response to Khoury complaint" |
| Counterparty action (e.g., document signed) | "Your client just signed the NDA — what's next?" |
| Colleague comment on matter | "Lazar commented on Acme MSA" |
| Approval pending | "New approval pending in Drafting Board" |

**Specificity rule**: always use the actual matter name or counterparty name where available. "Your document" is worse than "Acme MSA." The goal is to make the user feel the notification is about their real work, not a generic product prompt.

### Skill router / discovery

Triggered when usage data suggests a user would benefit from a skill they have not tried:

| Trigger | Template |
|---|---|
| User has drafted 3+ NDAs but never used review skill | "Try /review NDA — catches issues you might miss. Saves 20 minutes." |
| User is active in employment matters but hasn't tried employment contract drafting | "Did you know Louis routes 973 specialized skills? Try draft.employment-contract." |
| New skill launched in user's practice area | "New skill: [skill name] for [jurisdiction]. Try it now." |

Keep skill templates to one concrete action and one stated benefit. Do not stack multiple prompts in one notification.

### Skills of the day

A rotating educational/discovery prompt surfaced once per day to active users:

> "Today's featured skill: draft.shareholders-agreement — suitable for UAE onshore and KSA."

This notification fires only if: the user has been active in the past 7 days and has not already used the featured skill. Rotate through the skill catalog; never repeat within 30 days for the same user.

### Credit and plan warnings

| Event | Template |
|---|---|
| 20% credits remaining | "20% credits left this month — plan accordingly." |
| 10% credits remaining | "Running low — 10% credits left. Top up or upgrade." |
| Credits exhausted | "You're out of credits. Upgrade or wait for your reset on [date]." |
| Reset notification | "Your credits reset today. Ready for a new month?" |

Tone should be informational, not panicked. Do not use urgency-bait language ("ACT NOW"). Credit warnings should feel like a helpful heads-up, not a pressure tactic.

### Collaboration and approval

| Event | Template |
|---|---|
| Comment added to shared document | "[Name] commented on [Document Name]" |
| User mentioned in a comment | "[Name] mentioned you in [Document Name]" |
| Approval requested | "[Name] requested your approval on [Document Name]" |
| Document shared | "[Name] shared [Document Name] with you" |

Collaboration notifications must use real names and real document names. Generic "you have a notification" is not acceptable.

## Best practices

### One CTA per notification
Every notification implies exactly one action. If a notification tries to do two things at once (re-engage AND upsell AND discover a feature), it does none of them. Choose the primary action and build the copy around it.

### Specific over generic
"Acme MSA" is better than "your document." "20% credits left" is better than "low balance." Specificity signals that the system knows the user's actual context, which increases trust and click-through.

### Time-zone aware delivery
Do not deliver notifications between 10pm and 7am in the user's local timezone. MENA users span UTC+2 (LB, EG) to UTC+4 (UAE, KSA). The platform must use the user's detected or set timezone for delivery windows.

### Frequency cap
- Hard cap: maximum 3 notifications per day, regardless of trigger.
- Preferred: average 1 per day for non-matter-specific notifications.
- Matter-specific (deadline, co-worker action): no daily cap — these are urgent and user-authorized.

### Personalization depth
Use `user.active_matters`, `user.recent_skills`, `user.role`, and `user.jurisdiction` to select and customize templates. A notification that reflects the user's real context converts; a generic one trains the user to ignore them.

## Channel architecture

| Channel | Use case | Max frequency |
|---|---|---|
| iOS APNs | Native iOS app notifications | 3/day (soft cap) |
| Android FCM | Native Android app notifications | 3/day (soft cap) |
| Web push | Browser-based push (in-browser, desktop/mobile) | 2/day |
| Email digest | Lower frequency, higher information density; daily summary of unactioned items | 1/day |

For matter-specific deadline reminders, all channels may fire simultaneously if the deadline is < 24 hours. For re-engagement and skill discovery, choose one channel per notification to avoid duplication.

## User preferences and consent

- All notifications require explicit opt-in (iOS/Android system permission + in-app preference).
- The in-app notification settings page (`/settings → Notifications`) must expose per-category toggles: matter reminders, re-engagement, skill discovery, credit warnings, collaboration.
- Honor quiet hours: user-configurable window (default: 10pm–7am local time) during which only critical notifications (expired deadline) are delivered.
- One-tap unsubscribe from any notification category must work within the OS notification settings; the platform must respect `unsubscribed_categories` in the user profile.
- A/B test notification variants — track open rate and conversion; sunset underperforming variants within 30 days.

## Related skills

- [[growth-email-onboarding-sequence]]
- [[growth-referral-prompt]]
- [[growth-win-back-inactive]]
- [[growth-nps-prompt]]
