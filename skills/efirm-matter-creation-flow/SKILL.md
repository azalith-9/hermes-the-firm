---
name: efirm-matter-creation-flow
description: Use when opening a new legal matter in the eFirm system — the skill standardizes the full creation workflow, from client lookup through conflict-check, fee structure, and engagement-letter generation to downstream system provisioning (DMS folder, team access, billing setup, audit log). This is the gateway process that gates all substantive legal work. P0 — all downstream eFirm skills depend on a properly created matter record.
license: MIT
metadata: " id: efirm.matter-creation-flow category: efirm jurisdictions: [__multi__] priority: P0 intent: [create matter, new matter, matter opening, onboarding, workflow] related: - efirm-client-intake-form - efirm-conflict-check - efirm-engagement-letter-draft - efirm-fee-quote-builder - efirm-deadline-tracker source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'efirm'.
Namespaced as louis-<category>-<skill> on registration.
-->


# eFirm: Matter Creation Flow

## When to use this

Use this skill when:
- A new client engagement is confirmed and a matter record must be opened.
- An existing client brings a new matter requiring a separate matter file.
- A matter type changes significantly (e.g., advisory becomes litigation) and requires re-classification.
- A matter is transferred from another firm and the full intake needs to be re-run.

This skill is the **central orchestrating workflow** for eFirm. Every other operational skill — billing, deadline tracking, document management, team collaboration — depends on a correctly constituted matter record.

## Why proper matter creation matters

Three systemic risks justify treating this as P0:

1. **Conflict-check failures**: if a matter is opened without a completed conflict check, the firm may represent adverse parties simultaneously — a bar-discipline and malpractice event.
2. **Engagement letter as insurance**: an undocumented engagement is a fee-dispute and malpractice exposure. The engagement letter — and its fee provisions — must exist before billable work begins.
3. **Matter coding**: downstream billing, reporting, and knowledge management all depend on correct matter-type coding at creation. Reclassification after the fact is administratively costly and error-prone.

## Required inputs at matter creation

| # | Field | Notes |
|---|---|---|
| 1 | Client identification | Existing client (lookup) or new (triggers [[efirm-client-intake-form]]) |
| 2 | Matter type | Corporate / Dispute / IP / Employment / Regulatory / Personal / Other |
| 3 | Matter description | Short title (5–10 words) + objective paragraph |
| 4 | Responsible partner | Named partner; must be licensed in relevant jurisdiction |
| 5 | Team assignment | Associates, paralegals, co-counsel if applicable |
| 6 | Fee structure | Hourly / Fixed / Contingency / Hybrid — from [[efirm-fee-quote-builder]] |
| 7 | Conflict check | Automated run + responsible partner sign-off — from [[efirm-conflict-check]] |
| 8 | Engagement letter | Drafted via [[efirm-engagement-letter-draft]]; must be signed before active status |
| 9 | Matter number | Auto-generated per firm numbering scheme |

## Optional / configurable fields

| Field | Default | Notes |
|---|---|---|
| Confidentiality level | Standard | Enhanced (restricted access) / Privileged-only (partner + compliance only) |
| Estimated budget | None | If set, triggers budget-alerting at 80% and 100% |
| Billing cadence | Monthly | Per engagement letter; can override per matter |
| Deadline SLA awareness | On | Triggers [[efirm-deadline-tracker]] population |
| Practice area sub-code | None | For detailed practice reporting |
| Co-counsel | None | External firm with access scoped appropriately |
| Language of matter | English | Relevant for document management and client comms |

## Workflow sequence

### Stage 1: Pre-intake gate

```
Is this a new client?
  YES → Run [[efirm-client-intake-form]] → AML/sanctions screening → UBO check
  NO  → Pull existing client record → confirm data is current → update if needed
```

If AML/sanctions screening returns a flag, **halt** — matter cannot proceed until the flag is resolved by the compliance partner.

### Stage 2: Conflict check gate

```
Run [[efirm-conflict-check]] across all parties.
  CLEAN    → Proceed to Stage 3
  CONCERN  → Route to conflicts partner → decision required before proceeding
  CONFLICT → Cannot proceed [or obtain written waiver per conflict-check skill]
```

Conflict check result is recorded in the matter file with timestamp and outcome before any further steps are taken.

### Stage 3: Fee structure and engagement letter

1. Responsible partner selects or confirms fee structure from [[efirm-fee-quote-builder]].
2. [[efirm-engagement-letter-draft]] auto-generates a firm-branded letter pre-populated from all stage 1–2 data.
3. Partner reviews and approves letter.
4. Letter transmitted to client for e-signature.
5. Matter status: **Pending** (no billable work allowed until letter is signed).

### Stage 4: Matter activation

On receipt of executed engagement letter:

```
Matter status: PENDING → ACTIVE

Auto-actions:
  □ Matter record written to eFirm database
  □ Document management folder created (structure per matter type)
  □ Team access granted (DMS + billing system + matter workspace)
  □ Audit log entry created
  □ Responsible partner notified (push notification)
  □ Billing setup initiated (timekeeper codes; billing cadence; rate card locked)
  □ Default deadlines populated per matter type (via [[efirm-deadline-tracker]])
  □ Client portal access provisioned (if applicable)
```

### Stage 5: Post-opening quality check

Within 5 business days of matter activation, the firm's matter-opening checklist should be reviewed:

- [ ] All parties identified and screened
- [ ] Conflict check complete and clean (or waiver on file)
- [ ] Engagement letter fully executed
- [ ] Fee structure documented and billing system configured
- [ ] Team briefed (initial team call or handoff note per [[efirm-team-handoff-summary]])
- [ ] Initial deadline entries populated
- [ ] Document folder structure created
- [ ] Client communication channel established

## Matter number scheme

The auto-generated matter number should encode:
```
[YY]-[JurisdictionCode]-[SequentialNumber]
```
Example: `25-UAE-0147` (2025, UAE matter, 147th matter opened this year)

For multi-jurisdiction matters, use the primary jurisdiction of the dispute or transaction.

## Special matter types

| Type | Additional fields required |
|---|---|
| Litigation | Court name; case number (when assigned); jurisdiction; limitation date |
| Arbitration | Seat; rules (ICC/DIAC/LCIA/AAA/SIAC); arbitrator appointment deadline |
| Regulatory | Regulating authority; reference number; response deadline |
| M&A / Transaction | Target; acquirer; deal type; estimated close date |
| Real Estate | Property reference; title registry; registration deadline |

## Output to downstream systems

| System | Data passed |
|---|---|
| Billing system | Matter number; client code; fee structure; timekeeper list; rate card |
| DMS | Matter folder structure; access rights |
| Deadline tracker | Matter type → default deadline template pre-populated |
| Client portal | Matter record; team contacts |
| Reporting / analytics | Matter type; practice area; jurisdiction; responsible partner |

## Related skills

- [[efirm-client-intake-form]]
- [[efirm-conflict-check]]
- [[efirm-engagement-letter-draft]]
- [[efirm-fee-quote-builder]]
- [[efirm-deadline-tracker]]
- [[efirm-team-handoff-summary]]
