---
name: tool-email-drafter
description: Use when drafting professional legal emails to clients, opposing counsel, court clerks, or regulatory authorities. Adapts tone, formality, greeting, and sign-off to recipient role, matter status, and regional norms — warmer for clients, formal and on-record for opposing counsel, procedural for court clerks, and region-aware (MENA formal, US direct, UK polite-formal). Outputs structured email with subject line, greeting, max 3-paragraph body, and bullet action items.
license: MIT
metadata: " id: tool.email-drafter category: tool jurisdictions: [__multi__] priority: P2 intent: [email, drafting] related: [outreach-payment-recovery-flow, efirm-client-update-email-draft, tool-calendar-integration, pa-workflow-transactional] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'tool'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Tool — Email Drafter

## What it does

Drafts professional legal emails adapted to the recipient's role, the relationship history, the matter's status, and regional communication norms. Produces a structured email — subject line, greeting, body (max 3 paragraphs), bullet-format action items, and a contextually appropriate sign-off.

## Inputs

| Field | Type | Required | Notes |
|---|---|---|---|
| `recipientRole` | enum | Yes | `client`, `opposing_counsel`, `court_clerk`, `regulator`, `transaction_counterparty` |
| `purpose` | string | Yes | One-sentence description of the email's objective |
| `matterStatus` | enum | No | `transactional_negotiation`, `active_dispute`, `pre_litigation`, `settlement`, `closed` |
| `region` | enum | No | `MENA`, `UK`, `US`, `EU`, `FR` — affects formality, greeting, sign-off |
| `language` | enum | No | `en`, `ar`, `fr` — defaults to `en` |
| `subjectRef` | string | No | Matter reference number for subject line |
| `attachmentContext` | string | No | Description of any attachment being referenced |
| `tone` | enum | No | `formal`, `collaborative`, `firm`, `urgent` — overrides default tone for role |

## Tone and style matrix

| Recipient | Default tone | Greeting style | Sign-off |
|---|---|---|---|
| Client | Warm, accessible, reassuring | "Dear [Name]" | "Kindly" / "Warm regards" |
| Opposing counsel | Formal, on-record, precise | "Dear [Mr/Ms/Dr] [Surname]" | "Yours faithfully" / "Yours sincerely" |
| Court clerk | Procedural, neutral, brief | "Dear Sir/Madam" | "Yours faithfully" |
| Regulator | Formal, deferential, complete | "Dear [Title]" | "Yours faithfully" |
| Transaction counterparty | Collaborative but professional | "Dear [Name]" | "Best regards" |

### Regional adjustments

**MENA (Arabic/Gulf context):**
- Formal openings expected; "I trust this email finds you well" is standard
- Religious greetings ("As-salamu alaykum") are appropriate when the relationship has established them; do not introduce without context
- Avoid directness that can be perceived as brusque in Gulf communication style
- Arabic-language emails should be offered in parallel when the recipient's primary language is Arabic
- KSA: correspondence with government entities should be in Arabic; formal titles (Your Excellency / معالي) used where appropriate

**UK:**
- Polite-formal; indirect requests preferred over demands
- "I write to you in connection with..." rather than "I'm emailing about..."
- "Yours faithfully" (when opening "Dear Sir/Madam") vs "Yours sincerely" (when using recipient's name)

**US:**
- Direct and brief; one paragraph per point
- Active voice; no archaic legal phrases
- "Best regards" or "Best" for most commercial relationships

**France:**
- Elaborate formal courtesy opening expected (e.g., "Veuillez agréer, Maître, l'expression de mes salutations distinguées")
- "Maître" for lawyers; "Monsieur/Madame le Juge" for court officials
- French-language emails strongly preferred for French counterparties

## Structure template

```
Subject: [Matter Ref] — [Topic] — [Action Required (if urgent)]

Dear [Greeting],

[Paragraph 1 — Context: why you are writing; 2–4 sentences]

[Paragraph 2 — Substance: what you are communicating, requesting, or proposing; 3–5 sentences or bullet list]

[Paragraph 3 — Next steps / action items — bullet format preferred]

[Optional closing courtesy sentence]

[Sign-off],
[Sender name]
[Title] | [Firm]
[Contact details]
[Matter reference]
```

## Special email types

### Active dispute — opposing counsel

- Every email is potentially discoverable or submitted to court. Avoid admissions, expressions of uncertainty, or non-legal pleasantries that could be taken out of context.
- Mark privileged instructions clearly: "This email contains privileged legal advice."
- Do not make settlement offers in correspondence not marked "Without Prejudice / Without Prejudice Save as to Costs."
- In MENA contexts: written communications to opposing counsel in Arabic may be required for domestic court proceedings.

### Payment recovery / AR chase

For accounts-receivable chase emails, use [[outreach-payment-recovery-flow]] which provides the full escalation sequence (soft reminder → formal demand → pre-litigation notice).

### Client update emails

Routine matter updates should follow the [[efirm-client-update-email-draft]] template which includes standardised matter-status codes and billing transparency.

## Output example

```
Subject: M-2026-034 — NDA Negotiation — Revised Clause 8 Attached

Dear Ms. Al Mansouri,

I write further to our call yesterday regarding the proposed amendments to the mutual NDA
between your company and [Counterparty].

Please find attached a revised draft with tracked changes. The key amendment concerns
Clause 8 (Governing Law), which we have revised to reflect our agreement to use DIFC
law as the governing law. All other provisions remain unchanged from the previous draft.

We would be grateful if you could review and revert at your earliest convenience. If
the revised clause is acceptable, we can move to final execution this week.

Kindly,
[Name]
[Title] | [Firm]
Ref: M-2026-034
```

## Failure modes

| Failure | Response |
|---|---|
| Opposing counsel email in active dispute without Without Prejudice flag | Warn user; offer to add WP header |
| Arabic email requested but no Arabic translation available | Return English draft with note; offer Arabic translation via separate step |
| Government email in KSA without Arabic | Warn that Arabic is required; offer Arabic parallel draft |
| Missing matter reference | Prompt user to confirm or skip; do not omit silently |

## Related skills

- [[outreach-payment-recovery-flow]]
- [[efirm-client-update-email-draft]]
- [[tool-calendar-integration]]
- [[pa-workflow-transactional]]
