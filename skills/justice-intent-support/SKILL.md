---
name: justice-intent-support
description: Use when the public-facing assistant detects that a user needs product support — reporting a bug, asking for help with a workflow, requesting account assistance, or escalating a billing or access issue. Routes to the help center, support ticketing, and direct escalation paths. Also handles the accessibility/justice dimension where a user in a legally vulnerable situation needs urgent help beyond product support. Covers all jurisdictions.
license: MIT
metadata: " id: justice.intent.support category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, support, bug, help, account, billing, escalation] related: [justice-intent-how-to, justice-intent-chitchat, justice-intent-feature-question, justice-intent-sales] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Registered as a flat plugin skill.
-->


# Justice Intent — Support

## When to use this

Trigger when the message indicates the user needs assistance with the product or account — not a legal question, not a sales question, but a support need:

- Bug reports: "Louis isn't working", "I'm getting an error", "the review didn't run", "document won't upload"
- Account / access issues: "I can't log in", "I forgot my password", "my subscription isn't active", "I can't access my documents"
- Billing issues: "I was charged incorrectly", "I need a refund", "change my plan", "cancel subscription"
- Workflow confusion: "I don't understand how to [X]" (product workflow — see [[justice-intent-how-to]] for distinction)
- Feature not working as expected: "The translation came out wrong", "The review missed important clauses"
- Escalation requests: "I need to speak to someone", "I want to escalate this"

Also trigger when a user appears to be in a legally urgent situation requiring human help beyond AI assistance — this is the Justice accessibility dimension:

- Signals of vulnerability: "I have a hearing tomorrow", "I'm being evicted", "I've been arrested", "I have no money for a lawyer"

## Response pattern

### Product / account support flow

**Step 1: Acknowledge the issue**
Confirm you understand the problem. Do not ask the user to repeat themselves if the issue is clear.

**Step 2: Try in-chat resolution**
For common issues, resolve directly:

| Issue | In-chat resolution |
|---|---|
| Login problem | Direct to `/forgot-password`; check if account email is correct |
| Billing question | Route to `/account/billing`; note that plan changes take effect at next cycle |
| Document upload failure | Check file format (PDF, DOCX, TXT supported); check file size limit; try refresh |
| Review didn't run | Ask if they confirmed the review job; check the job queue at `/account/jobs` |
| Wrong output | Offer to re-run with a clarifying instruction; flag for model feedback if systematic |

**Step 3: Route to help center**
For issues not resolvable in chat: route to `/help` (searchable knowledge base). Specific help article slugs if available:
- Password reset → `/help/account/reset-password`
- Billing → `/help/billing`
- Upload limits → `/help/documents/upload`
- API errors → `/help/api`

**Step 4: Create a support ticket**
For unresolved issues or anything requiring human review:
- Route to `/support/contact` or the in-app support widget
- Ask the user to describe: what they were trying to do, what happened, what they expected to happen
- Include account email in the ticket for faster lookup

**Step 5: Escalate for critical issues**
High-severity escalation triggers:
- Data loss (documents not accessible)
- Security concern (unauthorized access, data breach)
- Billing dispute above [threshold]
- Enterprise SLA breach

For these: flag immediately to the support operations team; do not defer to async ticket.

### Justice / vulnerability support flow

When a user signals they are in a legally urgent or vulnerable situation:

1. Acknowledge their situation with empathy — do not immediately route to a help page
2. Assess: is this a product support need OR a legal aid need?
3. For legal aid needs: provide immediate, accessible legal information in plain language (see [[justice-intent-legal-research]])
4. Flag relevant pro-bono and legal-aid resources in their jurisdiction:
   - Lebanon: Beirut Bar Association legal aid committee; various NGOs
   - UAE: DIFC Courts Pro Bono program; DLA Piper Pro Bono
   - KSA: Ministry of Justice legal aid office
   - France: Aide Juridictionnelle; ADIJ
   - UK: Legal Aid Agency; Citizens Advice
   - US: Legal Services Corporation grantees; state bar referral programs
5. If the situation is urgent (hearing today, imminent harm): prioritize real-time guidance and direct to emergency legal services

## Tone rules

- Empathetic and calm — support users are often frustrated
- Action-oriented — give a next step immediately, don't just explain the problem
- No defensive responses to bug reports — acknowledge and act
- Dignity-preserving for vulnerability cases — never make a user feel their situation is too small or too complicated

## Do not

- Do not dismiss user reports as user error without investigating
- Do not route vulnerable users to a generic help page — handle with directness
- Do not promise resolutions on timelines the team cannot commit to
- Do not ask users to re-enter data that was lost due to a product error

## Related skills

- [[justice-intent-how-to]]
- [[justice-intent-chitchat]]
- [[justice-intent-feature-question]]
- [[justice-intent-sales]]
- [[justice-intent-legal-research]]
