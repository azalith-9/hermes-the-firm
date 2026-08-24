---
name: ops-error-classifier
description: Use when an error occurs anywhere in the legal AI request pipeline and a structured response decision is needed. Classifies errors into six categories (transient, provider, client-input, auth/quota, backend-bug, schema/data-integrity) and outputs the correct action (retry, failover, user guidance, upgrade flow, ticket, escalation) along with a user-facing message and an optional internal ticket reference.
license: MIT
metadata: " id: ops.error-classifier category: ops jurisdictions: [__multi__] priority: P2 intent: [error, ops, error-handling, retry, failover] related: [ops-crash-report-formatter, ops-bug-report-collector, ops-linear-triage-from-chat-bug-report, ops-subscription-erd-validator] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ops'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Ops — Error Classifier

## Purpose

Not all errors should be handled the same way. A timeout from an LLM provider is different from a malformed user upload, which is different from an expired API key, which is different from a schema bug. This skill classifies every error by type and outputs the correct action, user message, and internal routing — so that error boundaries in the frontend and middleware in the backend always respond appropriately.

## Classification schema

Errors are classified into six categories:

### 1. Transient
**Definition**: Network-level or infrastructure-level failures that are likely self-resolving.
**Examples**: request timeout, rate-limit (429), network disconnect, brief database unavailability.
**Action**: Automatic retry with exponential backoff (max 3 attempts). If all retries fail, escalate to Provider category.
**User message**: "Something went wrong — retrying automatically."
**Internal ticket**: None for first occurrence; flag if the same transient error recurs >3× in 5 minutes.

### 2. Provider
**Definition**: LLM provider (Anthropic, OpenAI, Google, etc.) returns a 5xx or sustained unavailability.
**Examples**: Anthropic 503, OpenAI 500, Gemini rate limit for the tenant's project.
**Action**: Fail over to the next configured provider in the failover chain (e.g., the agent Sonnet → GPT-4o → Gemini Pro). Log the failover.
**User message**: "We're experiencing a brief technical issue. Switching to an alternative AI provider."
**Internal ticket**: Create a linear note if the failover persists >10 minutes; page on-call if it persists >30 minutes.

### 3. Client input
**Definition**: The error is caused by the user's input or uploaded content.
**Examples**: Oversized file upload (>50MB), unsupported file format, corrupted PDF, prompt exceeds context limit.
**Action**: Do not retry. Return user-friendly guidance.
**User message**: Specific to the error — e.g., "This file is too large (max 50MB). Try compressing it or splitting into sections." Never say "bad input" — always describe what the user can do.
**Internal ticket**: None. Log for aggregate analysis only.

### 4. Auth / quota
**Definition**: The user or tenant does not have permission or credits for the requested operation.
**Examples**: Out of monthly credits, expired session token, API key revoked, BYO-key quota exhausted.
**Action**: Redirect to the appropriate resolution flow.
- Expired token → silent re-auth or login prompt.
- Out of credits → [[onboarding-upgrade-prompt-when-credits-low]].
- BYO-key quota → prompt user to check their API key settings.
**User message**: Context-appropriate (not a generic error).
**Internal ticket**: Log credit exhaustion events for burn-rate watcher. No ticket for auth flows.

### 5. Backend bug
**Definition**: An unhandled exception or logic error in the application code.
**Examples**: NullPointerException, unhandled promise rejection, wrong database query returning empty set unexpectedly.
**Action**: Show a generic error to the user. Create a P-level Linear ticket automatically.
**User message**: "Something went wrong on our end. The team has been notified."
**Internal ticket**: Auto-create in Linear with stack trace, session context, user ID (anonymized), and severity (auto-classified from impact). See [[ops-crash-report-formatter]] for formatting.

### 6. Schema / data integrity
**Definition**: Data in the database or a data model violates an expected constraint or schema.
**Examples**: User has two active subscriptions (violates 1-1 constraint), null field in a required column, foreign key pointing to a deleted record.
**Action**: Halt the operation. Create a DBA escalation ticket. Do not attempt to proceed with corrupt data.
**User message**: "We encountered a data issue with your account. Our team has been notified and will reach out within 24 hours."
**Internal ticket**: High-priority Linear issue assigned to the DBA or backend lead. Include the failing entity IDs (anonymized) and the violated constraint.

## Output schema

Every classified error produces the following output:

```json
{
  "errorClass": "transient | provider | client-input | auth-quota | backend-bug | schema-integrity",
  "action": "retry | failover | user-guidance | upgrade-flow | re-auth | p-level-ticket | dba-escalation",
  "userMessage": "<string — plain language, no jargon>",
  "internalTicket": {
    "create": true | false,
    "severity": "P0 | P1 | P2 | P3 | null",
    "assignee": "<team or role>",
    "summary": "<string>"
  },
  "retryable": true | false,
  "retryAfterMs": <number | null>
}
```

## Where this skill is used

- **Frontend error boundaries**: React error boundaries and API call wrappers call the classifier to determine whether to show a retry button, a guidance message, or a generic error screen.
- **Backend middleware**: API request handlers pass unhandled exceptions through the classifier before responding to the client.
- **Skill router**: when a skill invocation fails, the router uses the classifier to decide whether to retry with the same skill, switch to a fallback skill, or surface an error.

## Related skills

- [[ops-crash-report-formatter]] — formats backend-bug class errors into structured incident tickets
- [[ops-bug-report-collector]] — collects user-reported issues that may accompany classified errors
- [[ops-linear-triage-from-chat-bug-report]] — triage workflow for P-level tickets created by this classifier
- [[ops-subscription-erd-validator]] — used when the classifier detects schema-integrity errors related to billing
