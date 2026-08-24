---
name: ops-linear-triage-from-chat-bug-report
description: Use when a bug report or feature request collected from in-product chat needs to be classified, assigned, prioritized, and scheduled in Linear. Covers severity heuristics (P0–P3), component routing (frontend/backend/skill-router/auth/billing), team assignment rules, SLA-based due dates, and Slack notification — the downstream step after the bug-report-collector or feature-request-collector runs.
license: MIT
metadata: " id: ops.linear-triage-from-chat-bug-report category: ops priority: P1 intent: [ops, linear, triage, bug, severity] related: [ops-bug-report-collector, ops-feature-request-collector, ops-crash-report-formatter, ops-error-classifier] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Ops — Linear Triage from Chat Bug Report

## Purpose

A bug report collected in-chat is raw material. Triage converts it into an actionable Linear issue with the right owner, priority, and due date. Poorly triaged bugs fall through the cracks; over-triaged bugs waste engineering time on edge cases while real problems wait. This skill defines the rules for getting triage right every time.

## Inputs

This skill receives the output of [[ops-bug-report-collector]] or [[ops-feature-request-collector]]:
- User description (in their words)
- Auto-collected session metadata
- Preliminary severity from the collector
- Component hint (if the collector detected one)
- Persona (lawyer / consumer / enterprise)
- Surface (web / mobile / word-plugin)

## Triage steps

### Step 1 — Receive and verify

Pull the newly created Linear issue from the `LOUIS-BUGS` or `LOUIS-FEATURES` project. Confirm:
- Title is descriptive (not "bug" or "error")
- Description includes user context and session metadata
- PII redaction has been applied (no raw names, emails, document content)

If any of these are missing, add them before proceeding.

### Step 2 — Classify by component

Determine which engineering domain owns the issue:

| Component | Indicators | Owner |
|-----------|------------|-------|
| Frontend | UI rendering issue, browser console error, React component failure, layout bug | Frontend lead |
| Backend / API | HTTP 5xx, database error, API response format issue, server-side logic bug | Backend lead |
| Skill router | Wrong skill invoked, router fallback triggered unexpectedly, skill composition error | AI team |
| Auth | Login failure, session expiry, permission denied error | Backend lead / Security |
| Billing | Subscription state incorrect, payment failure not handled, credit not applied | Ops lead |
| Infrastructure | Database timeout, memory exhaustion, cold-start latency spike | Infra/DevOps |

When in doubt, assign to the most likely owner and leave a comment with the uncertainty noted.

### Step 3 — Classify severity

| Level | Definition | Examples |
|-------|------------|---------|
| **P0** | Full or partial outage; data loss; security vulnerability; loss of a client's saved work | App down for all users; a saved draft was deleted; SQL injection found |
| **P1** | Feature broken for a significant portion of users; payment processing failure; frequent crashes that block work | PDF upload fails for all users; payment webhook not firing; skill router always falls back |
| **P2** | Edge-case failure; affects a small number of users; workaround available | Arabic RTL rendering glitch in a specific browser; date format wrong in one jurisdiction |
| **P3** | Cosmetic; non-blocking; nice-to-have fix | Spinner animation jank; button text slightly misaligned |

When the user is a **paid tier** user and the bug blocks their paid feature, automatically elevate one severity level (P3 → P2, P2 → P1). Paying customers have a higher SLA expectation.

### Step 4 — Set due date based on severity

| Severity | Target resolution |
|----------|------------------|
| P0 | 24 hours from report |
| P1 | 1 week from report |
| P2 | 1 month from report (or next sprint) |
| P3 | Backlog; no fixed date |

Due dates are targets, not hard deadlines — but they should be set in Linear so that missed SLAs surface visibly in the weekly ops review.

### Step 5 — Assign

Set the assignee to the component owner (from Step 2). If the component owner is unclear, assign to the engineering lead who triages the morning standup queue.

### Step 6 — Notify

- For P0: immediately post to `#incidents` Slack channel and page the on-call engineer.
- For P1: post to `#bugs-p1` Slack channel with a link to the Linear issue.
- For P2/P3: no Slack notification; visible in the Linear project view.
- If the user opted in to updates, add them as a subscriber on the Linear issue.

## Anti-patterns to avoid

| Anti-pattern | Why it's harmful |
|---|---|
| Over-triaging: full P0/P1 treatment for every report | Desensitizes the team to alerts; burns engineering cycles on low-impact issues |
| Under-triaging: marking a real P1 as P2 because it only affects one user | If that user is a key enterprise account, the impact is disproportionate |
| No owner set | Unowned bugs languish; nobody feels accountable |
| No due date | Bugs marked but not scheduled are effectively invisible |
| PII in Linear | A serious compliance risk; redact before triage, not after |

## Weekly triage review

The product/engineering lead runs a weekly review of the triage queue:
- All P2 bugs open >14 days are re-evaluated (upgrade to P1 or close as won't fix)
- All unassigned bugs are assigned
- P3 bugs open >90 days are closed or promoted
- Feature requests with >5 unique requesters are moved from `LOUIS-FEATURES` to the roadmap backlog for prioritization

## Related skills

- [[ops-bug-report-collector]] — the upstream collection step that feeds this triage skill
- [[ops-feature-request-collector]] — the parallel upstream for feature requests
- [[ops-crash-report-formatter]] — produces the structured crash ticket that may also feed this triage
- [[ops-error-classifier]] — classifies errors before they become Linear issues
