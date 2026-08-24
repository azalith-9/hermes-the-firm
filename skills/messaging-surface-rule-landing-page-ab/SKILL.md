---
name: messaging-surface-rule-landing-page-ab
description: Use when creating or reviewing A/B test variants for landing pages of a legal AI assistant — including paid acquisition landing pages, campaign-specific pages, and conversion-optimised pages separate from the main homepage. Defines the compliance requirements that apply to both test variants, what elements may be varied, and the process for adding a winning variant's claims to the messaging bible. Both A and B variants must independently pass messaging compliance before any test launches.
license: MIT
metadata: " id: messaging.surface-rule.landing-page-AB category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, landing-page, A/B-test, CRO, copy-variants, compliance] related: [messaging-compliance-checker, messaging-surface-rule-haqq-ai-homepage, messaging-allowed-claims-consumer, messaging-banned-claims-consumer, messaging-hard-rule-bible-signoff-required] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Registered as a flat plugin skill.
-->


# Messaging — Surface Rule: Landing Page A/B Tests

## When this applies

This skill governs landing pages used in paid acquisition campaigns, organic growth tests, and CRO (conversion rate optimisation) experiments where two or more copy variants are run simultaneously. It applies to:

- Google Ads / Meta Ads campaign landing pages
- Jurisdiction-specific landing pages (e.g., "UAE employment contracts help")
- Persona-specific landing pages (e.g., separate pages for lawyers vs consumers)
- Product-specific landing pages (e.g., NDA generator, contract review)
- Waitlist landing pages (see also [[messaging-surface-rule-waitlist-email]])

Both the **A variant and the B variant** must independently satisfy all messaging compliance requirements before the test runs. A/B testing is not a compliance bypass.

---

## Behavior — The Two-Variant Rule

Every A/B test on a landing page requires:

1. **Two separate compliance reviews** — one per variant — run through [[messaging-compliance-checker]] before the test goes live
2. **Separate documentation** in the marketing review log for each variant
3. **No "exploratory banned" variant** — it is never acceptable to test whether a banned claim converts better; banned claims are banned regardless of conversion performance
4. **Bible alignment for both variants** — if either variant introduces a new claim type, [[messaging-hard-rule-bible-signoff-required]] applies before the test runs

---

## What Can and Cannot Be A/B Tested

### Allowed variables (safe to test without additional review)

| Variable | Example |
|----------|---------|
| Headline formulation | "Understand your contract" vs "Know your rights" |
| Call-to-action text | "Start free" vs "Try Louis free" |
| Hero image / visual | Document visual vs person-with-phone visual |
| Social proof placement | Testimonials above vs below the fold |
| Feature ordering | Lead with drafting vs lead with review |
| Tone register | More formal vs more conversational (within allowed vocabulary) |
| Value anchor phrasing | "Less than a lawyer consultation" vs "For the price of a coffee" |

### Requires additional review before testing

| Variable | Reason |
|----------|--------|
| New outcome metric | Any new time-saving or accuracy number → evidence required |
| New capability claim | Any new jurisdiction or document type claim → product verification required |
| New comparative framing | Any comparison (explicit or implied) to a named competitor or to professional fees → legal review |
| New persona targeting | A page targeting a new audience segment (e.g., first landing page targeting arbitration practitioners) → audience assessment |

### Not permitted as A/B test variables

| Banned test | Reason |
|-------------|--------|
| Banned claim in Variant B | Conversion testing does not justify using banned claims; there is no "let's see if it works" exception |
| "Legal advice" vs "legal information" | Even framing one variant as "legal advice" in a test is a compliance breach |
| No disclaimer vs disclaimer | Disclaimer is not a variable; it is required on all variants |

---

## Landing Page Compliance Checklist

Before any landing page (A or B) launches:

- [ ] Run through [[messaging-compliance-checker]] — all four passes
- [ ] Legal disclaimer present: "Louis provides legal information, not legal advice."
- [ ] All claims sourced and at average level (no outcome guarantees)
- [ ] Testimonials pre-approved per [[messaging-hard-rule-preapproved-press-quotes-only]]
- [ ] CTA does not use banned phrasing ("Get free legal advice" → banned)
- [ ] If new claim: [[messaging-hard-rule-bible-signoff-required]] completed
- [ ] Audience (consumer vs professional) correctly identified and appropriate fork rules applied

---

## After the Test: Adding a Winner to the Bible

If a winning variant introduces copy that was not previously in the messaging bible:
1. Document the winning copy verbatim
2. Submit for bible signoff via [[messaging-hard-rule-bible-signoff-required]]
3. Add to the bible only after sign-off
4. The winning copy is then pre-cleared for use on other surfaces where the same rules apply

Do not simply forward the winning variant to other channels without this process — a claim compliant in a landing page context may need different framing on other surfaces.

---

## Jurisdiction-Specific Landing Pages

Landing pages targeting users in a specific jurisdiction must:
- Reflect the applicable local legal framing (e.g., KSA pages use "Saudi law" context not generic "law")
- Add jurisdiction-specific disclaimers if the product's coverage in that jurisdiction is limited
- Have their claims reviewed against the specific bar advertising rules and consumer protection frameworks of that jurisdiction
- Not make claims about KSA law on a UAE landing page, or vice versa, without clarifying that the coverage spans both

---

## Related skills

- [[messaging-compliance-checker]]
- [[messaging-surface-rule-haqq-ai-homepage]]
- [[messaging-allowed-claims-consumer]]
- [[messaging-banned-claims-consumer]]
- [[messaging-hard-rule-bible-signoff-required]]
- [[messaging-outcome-claims-allowed]]
