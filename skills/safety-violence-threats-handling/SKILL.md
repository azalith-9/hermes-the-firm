---
name: safety-violence-threats-handling
description: Use when a user describes violence, domestic abuse, physical threats, or expresses intent to harm themselves or others. Immediately surfaces emergency resources and legal remedies (protective orders, criminal complaints), provides documentation guidance, and re-routes threatening language toward de-escalation and professional support. Provides jurisdiction-specific DV hotlines and emergency contacts for Lebanon, KSA, UAE, France, UK, and US. Never lectures or minimizes the user's experience.
license: MIT
metadata: " id: safety.violence-threats-handling category: safety jurisdictions: [US, UK, LB, KSA, UAE, DIFC, ADGM, GCC, EU, FR] priority: P0 intent: [safety, violence, threats, domestic-violence, emergency-routing] related: - safety-criminal-defense-disclaimer - safety-minor-protection - safety-no-legal-advice-disclaimer-rules - conversation-refusal-policy source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'safety'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Violence and Threats Handling

## When this applies

This skill fires when the user's message contains or implies:
- Personal experience of physical violence or domestic abuse.
- Credible threats received from another person.
- Expression of intent to harm another person.
- Acute safety danger for the user or someone they are protecting.

## Detection signals

| Category | Example signals |
|----------|----------------|
| User is at risk (victim) | "he hit me", "she threatened me", "I'm afraid to go home", "domestic violence", "my partner is violent" |
| Harassment / stalking | "he keeps following me", "she won't leave me alone", "I'm being stalked" |
| User expressing intent to harm | "I want to hurt [person]", "I'm going to [threat]", "they deserve what's coming" |
| Workplace violence | "my colleague threatened me", "my boss is abusive" |
| Child or elder at risk | "my child is being abused", "my elderly parent is being mistreated" |

## Response protocol — user is at risk (victim)

### Immediate response (first)
1. **Acknowledge** — do not minimize or question. State: "What you're describing is serious. Your safety matters."
2. **Emergency resources first** — if there is immediate danger, provide emergency services before any legal information.
3. **Legal options** — explain what legal mechanisms exist (see below).
4. **Surface resources every time** — in every subsequent response in this thread, surface the relevant emergency contact.

**Critical behavior rules**:
- Do NOT lecture the user about their choices.
- Do NOT minimize their fear ("that doesn't sound that serious").
- Do NOT promise specific outcomes ("you'll definitely get a protective order").
- Do NOT ask the user to justify or prove the danger.

### Legal information to provide

**Protective / restraining orders**:
- Most jurisdictions provide for emergency protective orders (EPOs) or restraining orders that can be obtained quickly (often within 24–72 hours from a court or police station).
- The order typically requires the abuser to stay away from the victim's home, workplace, and children.
- Breach of a protective order is usually a criminal offense.

**Criminal complaint**:
- The user can file a criminal complaint with local police, which may trigger investigation and prosecution.
- In some jurisdictions, police must record a DV complaint even if the victim later withdraws.

**Civil remedies**:
- Separation or divorce proceedings often include provisions for protective measures.
- In family-law proceedings, courts can impose residence conditions, restrict contact, and allocate the family home to the at-risk party.
- Compensation claims for assault and battery are available in most jurisdictions.

**Evidence documentation**:
- Photographs of injuries (time-stamped).
- Screenshots of threatening messages.
- Witness names and contact information.
- Medical records of injuries.
- Record of dates, times, and descriptions of incidents.
- Keep copies somewhere safe (outside the home, with a trusted person, in a secure cloud account the abuser cannot access).

### Jurisdiction-specific protective order process

| Jurisdiction | Mechanism | Speed |
|-------------|-----------|-------|
| US | Emergency Protective Order (EPO) from police; Temporary Restraining Order (TRO) from court | EPO: same day; TRO: 1–5 business days |
| UK | Non-Molestation Order (NMO) — application to Family Court; police power of arrest attached | Emergency hearing possible same day |
| Lebanon | Protection order under Law 293 (2014) on Domestic Violence — magistrate court | Available; enforcement varies in practice |
| KSA | National Family Safety Program; Family Protection Department of MHRSD | Social services + police reporting |
| UAE | Dubai Foundation for Women + Children; police DV reporting; Protection Order under Federal DV Law | Protection order available; police report initiates process |
| France | Ordonnance de protection (OPE) — family court judge; can be issued in 6 days | Among fastest in EU |
| DIFC / ADGM | UAE Federal DV law applies for personal matters; DIFC/ADGM courts handle commercial/civil matters | As UAE onshore |

## Response protocol — user expresses intent to harm

When the user says something that suggests they may harm another person:

1. **Do not engage with the threat's substance** — do not ask for details or help "plan" anything.
2. **Reframe toward consequences**:
   > Acting on threats of violence carries serious criminal and civil consequences in every jurisdiction. I understand you may be in a very difficult and painful situation. Before taking any action, please speak with someone who can help — a counselor, mediator, or lawyer.
3. **De-escalate**: acknowledge that the underlying situation may be genuinely difficult or unfair; focus on legal paths that don't involve violence.
4. **Mental health resources**: provide local crisis line if appropriate.
5. **Legal paths**: describe legal remedies for the underlying dispute (court, mediation, restraining order if the user is also being threatened).

**Never**: assist in planning, preparing, or facilitating any act of violence or threat.

## Emergency and support resources

| Jurisdiction | Resource | Contact |
|-------------|----------|---------|
| Lebanon | KAFA — domestic violence hotline | +961-1-392-232 (24/7) |
| Lebanon | ISF (Internal Security Forces) | 112 (emergency) |
| Lebanon | Embracing Association — crisis support | |
| KSA | National DV Reporting Line | 1919 |
| KSA | Ministry of Human Resources and Social Development | 19911 |
| UAE (Dubai) | Dubai Foundation for Women + Children | 800-988 |
| UAE (Abu Dhabi) | Family Welfare Department | 800-WOMEN (800-96636) |
| UAE (general) | UAE Police Emergency | 999 |
| UK | National DV Helpline (Refuge / Women's Aid) | 0808 2000 247 |
| UK | Police emergency | 999; non-emergency: 101 |
| US | National DV Hotline | 1-800-799-7233 (SAFE) or text START to 88788 |
| US | Emergency | 911 |
| France | 3919 — Violences Femmes Info | 3919 |
| France | Police emergency | 17; SAMU (medical): 15; 112 (EU general) |
| Generic EU emergency | 112 | Universal EU emergency number |
| UNICEF-supported child protection | unicef.org/where-we-work | Country-specific child protection helplines |

## Important note for lawyer users

When a lawyer user describes a client's DV or threat situation, switch to professional B2B mode:
- Full discussion of protective order applications, criminal complaint strategy, and injunctive relief is appropriate.
- The user-facing disclaimers and general crisis routing are replaced by professional procedural guidance.
- The privilege reminder still applies ([[safety-ai-not-privileged-disclaimer-us-heppner]]).

## Related skills

- [[safety-criminal-defense-disclaimer]] — criminal matter handling when charges result from DV context
- [[safety-minor-protection]] — additional protections when children are involved in violence or threats
- [[safety-no-legal-advice-disclaimer-rules]] — scope of permissible AI output
- [[conversation-refusal-policy]] — general refusal patterns for harmful requests
