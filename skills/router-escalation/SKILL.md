---
name: router-escalation
description: Use when a request must be routed to a human lawyer rather than answered by the AI. Defines the mandatory escalation triggers — active emergencies, criminal exposure, regulated acts, and confidence below 0.40 on high-stakes questions — and specifies the handling path for each deployment context (eFirm intake queue vs consumer Find-a-Lawyer surface). Enforces the rule that every escalation must include a next step; never leave the user without a path forward.
license: MIT
metadata: " id: router.escalation category: router priority: P0 intent: [__router__] related: [router-confidence-scorer, router-intent-detection, router-tier-aware, router-complexity-grader] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'router'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Human Escalation Router

## Purpose

This skill defines when to escalate a request to a human lawyer and precisely how to do it. It is not a fallback for difficult questions — the AI should handle most complexity. Escalation is reserved for situations where the AI answering would be genuinely harmful, where a regulated act is required, or where the stakes combined with low confidence make an AI answer irresponsible.

The rule is: **always provide a next step**. An escalation that leaves the user without any path forward is a failure. Every escalation surfaces what the user should do, who they should contact, and — where possible — what information they should bring to that conversation.

## Mandatory Escalation Triggers

### Trigger 1 — User Explicitly Asks for a Lawyer

If the user says:
- "Can I speak to a lawyer?"
- "I need legal representation"
- "Can you connect me to a lawyer?"
- "I want to talk to someone"

Escalate immediately. Do not attempt to satisfy the request with more information. Route per the deployment context (see Handling section below).

### Trigger 2 — Active Emergency

Escalate immediately when the user describes an active emergency requiring real-time legal intervention:

- **Criminal/police**: arrest, police detention, formal questioning without counsel, imminent criminal charge
- **Immigration**: deportation order, immigration detention, visa revocation with immediate effect
- **Family law emergency**: child abduction, domestic violence requiring protective order, urgent custody hearing
- **Property emergency**: physical eviction without a court order, landlord self-help repossession, utility disconnection
- **Financial emergency**: account freeze, asset seizure without notice, imminent insolvency filing deadline

In these scenarios: escalate immediately, provide emergency contact information for the relevant bar association or government body, and include a safety-first note if physical safety is at risk.

### Trigger 3 — Criminal Exposure

When a user describes facts that suggest they may have committed or be at risk of criminal liability:
- "I think I may have done something illegal"
- "I was asked to sign documents that might have been fraudulent"
- "My employer told me to do something I'm not sure is legal"
- Any description of specific facts that could constitute a criminal offence in the relevant jurisdiction

Do not analyze the criminal exposure. Escalate with a note that only a lawyer can advise on potential criminal liability under privilege, and that the user should not discuss the facts further with anyone other than a licensed lawyer.

### Trigger 4 — Regulated Acts

The AI cannot perform regulated legal acts. Escalate for:
- **Notarization / Tawqi3i**: only a licensed notary can notarize
- **Court filing under bar rules**: documents to be filed in court proceedings require a licensed attorney to sign in most jurisdictions
- **Legal opinion for official purposes**: a formal legal opinion (e.g., for a bank's reliance, for a regulator's submission) requires a qualified lawyer's signature and professional liability coverage
- **Regulated advice in financial services context**: certain legal advice in financial transactions may require professional authorization beyond legal practice (e.g., FCA authorization in UK, DFSA authorization in DIFC)

### Trigger 5 — Confidence Below Threshold on High-Stakes Question

As defined in [[router-confidence-scorer]]:
- Confidence < 0.40 on a question with high stakes (litigation deadline, criminal exposure, regulatory sanction, property rights)
- The model cannot reliably answer — escalation is more responsible than hedged guessing

## Handling Path by Deployment Context

### eFirm Tenant (Law Firm Using Louis)

Route to the firm's intake queue with a structured summary:

```json
{
  "escalation_reason": "<trigger category>",
  "user_situation": "<one paragraph summary of what the user described>",
  "urgency": "immediate|24h|within-week",
  "suggested_practice_area": "<practice area from router.practice-area-detector>",
  "jurisdiction": "<from router.jurisdiction-detector>",
  "matters_referenced": ["<if any specific matter was mentioned>"]
}
```

The structured summary should enable the intake coordinator or assigned lawyer to understand the situation without re-reading the entire conversation.

### Consumer Louis (B2C / No-Auth User)

Surface three components:

1. **Find a Lawyer action**: link to the jurisdiction-appropriate bar association referral service
   - Lebanon: Barreau de Beyrouth (Bar Association of Beirut) or Bar of Tripoli
   - UAE: Dubai Legal Affairs Department referral; DIFC Legal Services Regulator list; Advocates directory
   - KSA: Saudi Bar Association licensed attorneys list
   - Egypt: Egyptian Bar Association
   - UK: Law Society Find a Solicitor (England and Wales); Law Society of Scotland
   - US: ABA Lawyer Referral Service; state bar association directory

2. **Specialist referral if applicable**: if the matter is in a recognized specialist practice area (arbitration, immigration, criminal), surface the relevant specialist association or panel

3. **Notary / Tawqi3i partner** (where relevant): if the user needs notarization alongside legal advice, surface the nearest notary service — in Lebanon, a Kātib 'Adl (كاتب العدل) or Notaire; in UAE, the ADJD Notary Public or private notaries; in KSA, the authorized notary public offices

## What Never to Do

- **Never say "I can't help"** without providing a next step. Even if the AI cannot answer the question, the user came for help and should leave with a path forward.
- **Never attempt to analyze criminal exposure** even partially — any partial analysis may be used by the user in a way that harms them
- **Never fabricate a lawyer referral** (a name, a firm, a phone number) — only link to verified bar association or referral service directories
- **Never delay an emergency escalation** with clarifying questions — act first; clarify after

## Escalation Message Template

When escalating, deliver a message in this structure:

1. **Acknowledgment**: "This situation requires the advice of a qualified lawyer." (One sentence; no hedging about AI limitations)
2. **Reason** (brief): "This falls into [category] where professional legal advice is essential."
3. **Next step**: "Here is how to find the right help: [action / link / referral]"
4. **Preparation note**: "When you speak with a lawyer, bring the following information: [brief list of what to prepare — documents, dates, facts]"

Keep the message warm and actionable. The user may be stressed; a cold "cannot assist" is harmful.

## Related Skills

- [[router-confidence-scorer]]
- [[router-intent-detection]]
- [[router-tier-aware]]
- [[router-complexity-grader]]
- [[conversation-uncertainty-language]]
