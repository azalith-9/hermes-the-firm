---
name: messaging-hard-rule-bible-signoff-required
description: Use when any new marketing claim, product positioning phrase, or outcome statement is proposed for use in customer-facing copy and has not previously appeared in the approved messaging bible. This hard rule requires explicit legal and brand sign-off before any novel claim ships. Triggers automatically within messaging-compliance-checker whenever a new claim is detected. Prevents unauthorized expansion of permitted claims that could create UPL risk, consumer protection liability, or bar advertising violations.
license: MIT
metadata: " id: messaging.hard-rule.bible-signoff-required category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, governance, hard-rule, signoff, claims-management] related: [messaging-compliance-checker, messaging-hard-rule-preapproved-press-quotes-only, messaging-banned-claims-consumer, messaging-banned-claims-lawyer, messaging-bridge-line] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Messaging — Hard Rule: Bible Sign-off Required

## When this applies

This rule triggers whenever any of the following occurs:

1. **A new claim type** appears in a piece of copy that has no exact or substantially equivalent match in the current approved messaging bible
2. **An existing allowed claim** is being used in a materially new context (new channel, new audience, new jurisdiction) where its compliance implications have not been assessed
3. **An outcome-level statement** that is more specific than existing approved outcomes (e.g., a new time-saving metric, a new jurisdiction-specific capability claim)
4. **A third-party endorsement or co-branding claim** referencing a partner, bar association, or institution that has not previously been approved
5. **Any claim about AI capability** that goes beyond the general capability descriptions in the existing bible (e.g., new accuracy benchmarks, new task categories)

This is a **blocking rule**: the asset cannot ship until signoff is obtained and the new claim is added to the bible.

---

## Behavior — The Signoff Process

### Step 1: Identify the Novel Claim

The compliance reviewer (human or automated via [[messaging-compliance-checker]]) identifies the specific phrase or claim that is not in the approved bible. The exact text is flagged in the copy.

### Step 2: Classify the Claim

| Classification | Description | Required reviewers |
|----------------|-------------|-------------------|
| New outcome claim | Any statement about what the product achieves for users or lawyers | Legal + Brand |
| New capability claim | Any new statement about what the product can do | Product + Legal |
| New jurisdiction claim | Coverage or compliance in a jurisdiction not previously covered | Legal (jurisdiction-specific) |
| New comparative claim | Any comparison to a named competitor or to lawyer fees | Legal + CEO/Founder |
| New third-party endorsement | Any quote or reference to a named third party | Legal + Comms |
| New metric / statistic | Any quantitative claim (hours saved, accuracy %, etc.) | Data + Legal |

### Step 3: Draft the Claim for Review

The copywriter or product marketer drafts:
- The exact proposed claim (verbatim)
- The context and surface where it will be used
- The supporting evidence (for metrics and outcomes: the underlying data and methodology)
- The legal analysis (does the claim create UPL risk, consumer protection risk, bar advertising rule violation, or accuracy liability?)

### Step 4: Obtain Sign-off

Submit to the designated reviewers per the classification table above. Sign-off must be:
- Explicit (written approval by each required reviewer)
- Stored in the claims database with date, reviewer name, and supporting evidence
- Added to the bible before the asset publishes

### Step 5: Add to Bible

The approved claim, with its approved exact wording, permitted contexts, and any required disclaimers, is added to the messaging bible. Future uses of the same claim in the same context do not require re-review.

---

## What the Bible Contains

The messaging bible is the canonical registry of:

| Section | Contents |
|---------|----------|
| Allowed consumer claims | Pre-cleared phrases per [[messaging-allowed-claims-consumer]] |
| Allowed lawyer claims | Pre-cleared phrases per [[messaging-allowed-claims-lawyer]] |
| Banned claims | Absolute prohibitions per [[messaging-banned-claims-consumer]] and [[messaging-banned-claims-lawyer]] |
| Approved outcome claims | Specific quantitative claims with supporting evidence citations |
| Approved press quotes | Third-party quotes cleared for re-use per [[messaging-hard-rule-preapproved-press-quotes-only]] |
| Approved comparisons | Competitor comparisons that have passed legal review |
| Surface-specific rules | Channel-level constraints per the surface-rule skills |

---

## Why This Rule Exists

### Legal AI is a high-risk marketing category

Marketing a legal AI product creates regulatory exposure across multiple fronts simultaneously:
- **UPL (unauthorized practice of law)**: a single carelessly worded claim can constitute UPL in multiple jurisdictions
- **Bar advertising rules**: each bar association in each jurisdiction has its own rules about what legal service providers (and by analogy, legal tech products) can claim
- **Consumer protection laws**: false or misleading claims create liability under UAE, KSA, Lebanon, UK, and EU consumer protection frameworks
- **Professional indemnity**: claims about accuracy, reliability, or outcome create insurance exposure

### Organic copy evolution is the primary failure mode

In practice, banned or risky claims rarely enter through deliberate policy decisions. They enter through:
- Copywriters or agencies who don't know the constraints
- AI-generated copy that hasn't been reviewed
- Real-time social posts that bypass the review queue
- Sales team members adapting the deck for a specific prospect
- Influencer ad-libs in sponsored content

This rule exists to catch all of these channels.

---

## Edge Cases

| Situation | Action |
|-----------|--------|
| Urgent campaign launching tomorrow | Launch delay is correct; do not exempt on urgency grounds |
| External agency created copy before briefing on bible | Review before publication; retroactively add approved claims to bible |
| Sales rep added a new claim to a prospect deck | Flag for review; if claim is meritorious, fast-track signoff; remove from deck until cleared |
| The claim is "obviously fine" | All novel claims require the process; "obviously fine" judgments are where errors accumulate |
| Claim was approved at a previous company or product | Does not carry over; re-review in this product's context |

---

## Do not

- Ship novel claims under time pressure without signoff
- Allow informal "I think it's fine" approvals — approvals must be documented
- Add claims to the bible without the supporting evidence (for metrics) or legal analysis (for capability or outcome claims)
- Assume that a claim allowed for one surface is allowed on all surfaces

---

## Related skills

- [[messaging-compliance-checker]]
- [[messaging-hard-rule-preapproved-press-quotes-only]]
- [[messaging-banned-claims-consumer]]
- [[messaging-banned-claims-lawyer]]
- [[messaging-bridge-line]]
- [[messaging-outcome-claims-allowed]]
