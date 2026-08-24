---
name: messaging-surface-rule-influencer-brief
description: Use when preparing an influencer brief for any sponsored or gifted content featuring a legal AI assistant. Defines the exact requirements for script pre-approval, the banned-words list that must be provided verbatim to every influencer, disclosure language requirements by jurisdiction, and the escalation process for influencer ad-libs or deviations from approved script. Applied as part of messaging-compliance-checker before any influencer campaign ships.
license: MIT
metadata: " id: messaging.surface-rule.influencer-brief category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, influencer, sponsored-content, brief, compliance, disclosure] related: [messaging-compliance-checker, messaging-banned-claims-consumer, messaging-hard-rule-preapproved-press-quotes-only, messaging-allowed-claims-consumer, messaging-bridge-line] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Registered as a flat plugin skill.
-->


# Messaging — Surface Rule: Influencer Brief

## When this applies

This skill applies to every piece of **sponsored, gifted, or paid influencer content** that promotes a legal AI assistant — including:

- Instagram posts, Stories, and Reels (paid partnership)
- TikTok videos (sponsored or gifted)
- YouTube integrations (mid-roll, dedicated video, sponsored mention)
- Podcast sponsorships (host-read or producer-read)
- LinkedIn posts by influencers (sponsored content)
- Twitter/X posts (paid or promotional)
- Newsletter sponsorships where the author is acting as an influencer

It applies regardless of follower count, audience size, or whether the influencer is a legal professional or a lifestyle creator. The compliance requirements are identical for all influencer tiers.

---

## Brief Requirements — What Every Brief Must Include

### 1. Approved Script / Key Messages

Every influencer brief must include:
- A pre-approved script (for scripted content) or approved key-message talking points (for ad-lib content)
- The exact phrases from [[messaging-allowed-claims-consumer]] that the influencer is permitted to use
- Clear indication of which claims are mandatory ("must say"), which are optional, and which are absolutely prohibited

**Script approval:** The script or talking points must be reviewed and approved via [[messaging-compliance-checker]] before being sent to the influencer. An unapproved script is not permitted.

### 2. The Banned-Words List

Every influencer brief must include the following banned-words list **verbatim**. Copy-paste this section into every brief:

---

**BANNED WORDS AND PHRASES — DO NOT USE IN YOUR CONTENT:**

The following phrases must **never** appear in your content about Louis:

- "Replaces your lawyer" or "no lawyer needed"
- "Free legal advice"
- "Win your case" or "guaranteed to win"
- "DIY legal" (implying Louis substitutes professional legal services)
- "Skip the lawyer" or "avoid legal fees"
- "Guaranteed outcome" or any promise of a legal result
- "Legal advice" (say "legal information" or "legal understanding" instead)
- Any claim that Louis is a licensed legal professional or provides the services of one

Using any of these phrases may require us to ask you to delete or edit the content. Thank you for keeping our messaging compliant.

---

### 3. Disclosure Requirements

All influencer content must clearly disclose the commercial relationship. Requirements vary by jurisdiction:

| Jurisdiction | Required disclosure |
|---|---|
| UK (ASA/CAP) | "#ad" or "Paid Partnership" — must be in the first two lines of the caption, visible without "see more" |
| US (FTC) | "#ad" or "#sponsored" — prominently placed, not buried; video must include verbal and/or on-screen disclosure |
| UAE (NIMA/TRA rules) | "#ad" or "إعلان#" — per UAE Advertising Standards; influencers registered with NIMA must comply with registration requirements |
| KSA (GCAM rules) | "#إعلان" or "#paid_partnership" — per the General Commission for Audiovisual Media influencer regulations |
| EU (EU DSA, member state implementations) | Clear and conspicuous commercial disclosure; verify member state specifics |
| General | If in doubt, disclose — every platform (Instagram, TikTok, YouTube, LinkedIn) has its own labelling tool; use it |

**The brief must specify which disclosure format to use** for the platform and primary audience jurisdiction. Do not leave disclosure choices to the influencer.

### 4. Review Rights and Revision Process

Every brief must include:
- Pre-publication review right: the brand reviews finished content before it goes live
- Revision request: if content contains banned phrases or incorrect claims, the brand has the right to request specific edits before publication
- Do not post without approval: include this as an explicit contractual obligation in the influencer agreement

---

## Before the Brief Sends — Compliance Check

Before any influencer brief is issued:

1. Run the draft approved script through [[messaging-compliance-checker]] — all four passes
2. Verify the brief contains the banned-words list verbatim (above)
3. Confirm disclosure instructions are jurisdiction-specific and complete
4. Obtain sign-off from legal/brand on any claims that are new per [[messaging-hard-rule-bible-signoff-required]]

---

## Handling Deviations

If an influencer ad-libs or deviates from the approved script and the content is already published:

| Deviation type | Action |
|----------------|--------|
| Contains a banned phrase | Request immediate edit or deletion; document the incident |
| Contains an unapproved outcome claim | Request edit to remove the claim; assess whether re-publication is appropriate |
| Used "legal advice" instead of "legal information" | Request caption edit or re-record; assess urgency based on reach and elapsed time |
| Minor deviation, no compliance breach | Document for future brief improvement; no immediate action required |

Pre-plan this escalation path in the influencer agreement. The influencer should know before posting that they may be asked to edit content.

---

## Examples — Brief Key Message Copy

**Approved talking points for a consumer influencer:**
> "I use Louis to understand what's actually in my contracts before I sign — it explains every clause in plain English. It's not a replacement for a lawyer, but it helps me ask better questions when I need one. Try it free at [link]."

**What an influencer must NOT say:**
> "I haven't needed a lawyer since I started using Louis — it handles everything." *(banned: lawyer replacement + no-lawyer-needed)*

---

## Related skills

- [[messaging-compliance-checker]]
- [[messaging-banned-claims-consumer]]
- [[messaging-hard-rule-preapproved-press-quotes-only]]
- [[messaging-allowed-claims-consumer]]
- [[messaging-bridge-line]]
- [[messaging-outcome-claims-banned]]
