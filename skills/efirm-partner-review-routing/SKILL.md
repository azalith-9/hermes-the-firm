---
name: efirm-partner-review-routing
description: Use when a document, decision, or action in the eFirm system requires partner-level review and approval before it can proceed. The skill defines the routing logic — which partner receives what type of review, at what threshold, with what SLA — and ensures that nothing requiring senior judgment is auto-processed or lost in a workflow queue. Part of the eFirm firm-management product suite.
license: MIT
metadata: " id: efirm.partner-review-routing category: efirm jurisdictions: [__multi__] priority: P2 intent: [review-routing, approval, escalation, governance, workflow] related: - efirm-matter-creation-flow - efirm-conflict-check - efirm-engagement-letter-draft - efirm-document-versioning-rule - efirm-team-handoff-summary source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Partner Review Routing

## When to use this

Use this skill to:
- Define which items in the eFirm workflow require partner review before proceeding.
- Route a specific document or decision to the correct partner based on matter type, risk level, and available capacity.
- Track the status of pending partner reviews and escalate overdue approvals.
- Set up the routing rules for a new firm or practice group deploying eFirm.

Partner review routing is the governance backbone of a law firm's operations. Without it, junior lawyers may unknowingly take on conflict-riddled matters, send unapproved fee quotes, or file documents without supervisory sign-off.

## Items that always require partner review

The following workflow items must never be auto-processed without partner sign-off:

| Item | Routing target | SLA |
|---|---|---|
| New matter opening — conflict check result | Conflicts partner | 24 hours (business) |
| Engagement letter — before transmission to client | Responsible partner | 48 hours |
| Fee quote — before transmission to client | Responsible partner | 48 hours |
| Document marked vEXEC or vFINAL | Responsible partner | 24 hours |
| Invoice exceeding threshold (e.g., >$50,000) | Billing partner | 48 hours |
| Write-down above threshold (e.g., >10% of matter fees) | Billing partner | 48 hours |
| Trust account exception (negative balance, imbalance) | Managing partner | Immediate |
| AML flag at client intake | Compliance partner | Immediate |
| Conflict-check "Concern" result | Conflicts partner | 24 hours |
| Conflict-check "Conflict" result | Managing partner | Immediate |
| External filing (court, regulator) | Responsible partner | Before filing |
| Opinion letter | Responsible partner + senior review partner | 48 hours |

## Routing logic

### By responsibility type

| Review type | Default routing | Fallback if unavailable |
|---|---|---|
| Matter governance (conflict, engagement) | Responsible partner | Managing partner |
| Billing and financial | Billing partner | CFO / Finance director |
| AML / compliance | Compliance partner | Managing partner |
| Specific practice advice | Practice group head | Most senior available partner in practice |
| Urgent external filing | Responsible partner | Named emergency backup partner |

### By urgency level

| Level | Trigger | SLA | Escalation if missed |
|---|---|---|---|
| Immediate | Trust account exception; AML flag; active conflict | Within 2 business hours | Managing partner alert |
| Urgent | Court filing deadline T-1; conflict concern | Within 4 business hours | Managing partner alert |
| Standard | Engagement letter; fee quote; invoice approval | Within 48 business hours | Reminder at T+24h; escalate at T+48h |
| Routine | KB addition approval; template update | Within 5 business days | Reminder at T+3 days |

### By document threshold

Firms may set financial thresholds above which additional sign-off is required:

| Threshold | Requirement |
|---|---|
| Fee quote > $[X] | Managing partner co-sign |
| Write-down > $[Y] | Billing partner approval |
| Invoice > $[Z] | Billing partner review before dispatch |
| Matter budget overrun > 20% | Responsible partner + client notification |

Thresholds should be set in firm configuration and referenced here.

## Review workflow

1. **Item reaches review queue**: eFirm creates a review task assigned to the designated partner.
2. **Notification**: partner receives alert (push + email) with:
   - Item type and description
   - Matter reference
   - Required action (approve / reject / amend + resubmit)
   - Deadline
   - Link to the item in eFirm
3. **Partner action**:
   - **Approve**: item proceeds; timestamp recorded; audit log entry written.
   - **Reject with comments**: item returned to originator with partner comments.
   - **Request amendment**: item held; partner adds notes; originator revises and resubmits.
4. **SLA tracking**: if review is not completed within SLA, an escalation is sent to the next level in the chain.

## Delegation rules

Partners may delegate review authority under defined conditions:
- Delegation must be recorded in eFirm (who delegated what to whom, for what period).
- Only delegation to another partner or senior counsel is permitted; delegation to associates is not allowed for the categories above.
- Delegations expire automatically after the specified period.
- The delegating partner remains responsible for all items approved under their delegation.

## Out-of-office handling

When a partner is on leave:
- eFirm auto-routes items to the designated backup partner.
- Backup assignment is set by the managing partner at the start of any absence > 1 business day.
- If no backup is set, items escalate to the managing partner.

## Audit trail

Every review action is recorded:
- Item ID + type
- Submitted by + timestamp
- Reviewed by (actual reviewer, not just assigned partner) + timestamp
- Action taken
- Any comments
- Final status

The audit trail is immutable and forms part of the matter file for all matter-related items.

## Common failures

- **Partner as rubber stamp**: if partners approve without reading, the routing system provides false assurance. Quality review requires training and a firm culture of responsibility.
- **No escalation**: a review item that sits unanswered is as dangerous as no review. Escalation paths must be live and tested.
- **Wrong routing target**: if the conflicts partner is also the responsible partner (conflicted reviewer), route to an independent senior partner.
- **Excessive items in queue**: if partners are overwhelmed with routine approvals, the firm should consider raising financial thresholds or delegating more routine items to senior counsel.

## Related skills

- [[efirm-matter-creation-flow]]
- [[efirm-conflict-check]]
- [[efirm-engagement-letter-draft]]
- [[efirm-document-versioning-rule]]
- [[efirm-team-handoff-summary]]
