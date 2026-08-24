---
name: prompt-pack-professional-email-draft
description: Use when a lawyer needs to draft a professional email to a client, counterparty, or court explaining a legal issue, the firm's position, or a recommended course of action. Covers tone calibration, legal-position framing, privilege markers, and jurisdiction-appropriate formality. Useful for client updates, demand letters styled as emails, settlement proposals, and regulatory correspondence in MENA and international practice.
license: MIT
metadata: " id: prompt-pack.professional-email-draft category: prompt-pack practice_area: corporate-commercial jurisdictions: [UAE, DIFC, ADGM, KSA, LB, EG, EU, UK] priority: P2 intent: [communications, professional-email-draft, client-update, demand-notice] related: [prompt-pack-termination-letter, prompt-pack-settlement-agreement, heuristic-always-state-jurisdiction-first] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'prompt-pack'.
Registered as a flat plugin skill.
-->


# Professional Email Draft

## When to use this

Use this skill when a lawyer or legal professional needs to draft:

- A **client update email** — explaining the status of a matter, a legal risk, or a recommended next step.
- A **legal position letter** styled as an email — setting out the firm's interpretation of a contract clause or a party's rights.
- A **without-prejudice** settlement proposal sent by email.
- A **demand or notice email** — formal notice of breach, notice to cure, or notice of termination.
- A **regulatory correspondence email** — responding to a regulator's query or flagging a compliance matter.
- An **inter-party email** — transmitting a draft contract or responding to counterpart's comments at a professional level.

For long-form formal demand letters intended to be printed and delivered, consider using a dedicated letter-drafting skill rather than this email skill.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Recipient (role/relationship)** | Determines tone, formality, and what legal assumptions can be unstated | Ask: "Is this to your client, a counterparty's lawyer, or a regulator?" |
| **Subject matter / issue to explain** | Core of the email | Ask before drafting |
| **The legal position or recommended action** | The substantive point of the communication | Ask; do not invent a position |
| **Jurisdiction** | Affects privilege rules, tone norms, and whether Arabic/English/French is expected | Default: UAE (English) unless instructed otherwise |
| **Desired tone** | Professional default; can be more assertive (demand) or more collaborative (negotiation update) | Default: neutral professional |

## Optional inputs

- **Without-prejudice flag** — if this is a settlement communication, the email must include the correct without-prejudice header and comply with the privilege rules of the applicable jurisdiction.
- **Timeline or deadline** — if the email sets a deadline for action (e.g., "please respond within 14 days"), include the specific date, not a relative period.
- **Prior correspondence reference** — "further to our call of [date]" or "following your email of [date]".
- **Attachments to reference** — list documents being transmitted with the email.
- **Language** — Arabic emails to KSA counterparts are standard; bilingual emails (English/Arabic) are common in UAE.

## Document structure

A professional legal email has these components:

1. **Subject line** — specific and informative, not generic ("RE: [Matter Name] — Notice of Breach" not "Important Legal Matter"). For without-prejudice emails, "Without Prejudice" must appear in the subject line.
2. **Salutation** — "Dear [Name/Title]" in formal contexts. In Gulf practice, "Dear [First Name]" is acceptable for known counterparts; "Dear Counsel" or "Dear Sir/Madam" for unfamiliar recipients.
3. **Opening reference line** — "We write further to [event/call/prior email of date] regarding [matter]." One sentence; no padding.
4. **Body — issue statement** — state the issue or legal position clearly in the first paragraph. Do not bury the lead.
5. **Body — analysis or background** — factual context, relevant contractual provisions, or legal framework, in 1–3 short paragraphs. Use numbered paragraphs for complex points.
6. **Body — recommended action / request** — the specific action the recipient is being asked to take (or being informed of). Use imperative language proportionate to the tone: "We request that you..." (professional), "Please be advised that you are required to..." (assertive), "We would be grateful if you could..." (collaborative).
7. **Deadline** — if applicable, state a specific calendar date. Reference the contractual or statutory basis for the deadline if relevant.
8. **Closing** — "Please do not hesitate to contact us if you have any questions" (standard). For contentious matters: "We reserve all of our client's rights."
9. **Sign-off** — "Yours faithfully" (unknown recipient, formal) or "Yours sincerely" (known recipient, UK/MENA common-law convention). "Best regards" for less formal professional correspondence.
10. **Privilege footer** — for emails containing legal advice, include a privilege and confidentiality notice footer (standard for law firms).

## Jurisdictional / practice notes

### UAE and Gulf (English-language practice)
- "Without prejudice" is recognized under UAE courts as a principle, but the formal without-prejudice privilege (as a bar to using the communication in court) is less robustly developed in UAE onshore courts than in common-law courts. In DIFC/ADGM courts, without-prejudice privilege follows English common-law principles.
- Tone in Gulf legal practice: formal, relationship-aware; avoid blunt adversarial language in first contact — even demand letters are typically couched in deferential language before escalating.
- Arabic translations of key demand communications may be required for UAE onshore court proceedings.

### KSA
- Arabic is expected for all formal legal correspondence with Saudi counterparts and regulators.
- Bilingual emails (English + Arabic) are good practice for international-facing matters.
- Notarization (Tawtheq / كاتب العدل) is not required for standard legal emails but is sometimes needed for formal contractual notices.

### Lebanon
- French and Arabic are commonly used alongside English; match the language of the underlying contract.
- Lebanese courts accept Arabic, French, or English pleadings; professional emails often mirror the contract language.

### DIFC / ADGM courts
- Without-prejudice privilege follows English law principles and is robustly recognized.
- "Calderbank offers" (offers expressed "without prejudice save as to costs") are recognized in DIFC court procedure.

### EU / UK
- Mark settlement communications "Without Prejudice" prominently; "Without Prejudice Save as to Costs" where a costs protection is intended.
- GDPR/UK GDPR: avoid unnecessary disclosure of personal data in email chains with external parties.

## Drafting standards

- **One email, one issue.** Avoid multi-issue emails when formal; separate letters for separate legal matters preserve clarity and evidential value.
- **Use numbered paragraphs** for any email with more than three substantive points — it aids responses and creates a clean record.
- **Avoid legal Latin** in client-facing emails ("inter alia," "mutatis mutandis") unless the client is legally sophisticated. Use plain equivalents.
- **State facts before law.** Clients absorb context better when they understand what happened before they are told what it means legally.
- **Reserve rights.** Every contentious email should end with: "We reserve all rights" or "Nothing in this email constitutes a waiver of any of our client's rights."
- **Privilege header:** "Privileged and Confidential — Attorney-Client Communication" or equivalent; customize per jurisdiction.

## Common mistakes

- **Missing without-prejudice header** on a settlement email. If the email later becomes admissible because the header was absent, it can damage the client's position.
- **Concrete deadlines stated as relative periods.** "You have 14 days" is ambiguous about start and end; write "by [specific date], being 14 days from the date of this email."
- **Burying the call to action.** Lawyers often write extensive background before stating what they want; start with what you need, then explain why.
- **Sending draft emails with tracked changes or comments.** Always strip track-changes metadata before sending.
- **US-style aggressive tone in Gulf practice.** "We will take all necessary legal action" as an opening salvo can damage commercial relationships that the client wishes to preserve; calibrate to context.

## Related skills

- [[prompt-pack-termination-letter]]
- [[prompt-pack-settlement-agreement]]
- [[prompt-pack-statement-of-claim]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
