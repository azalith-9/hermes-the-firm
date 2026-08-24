---
name: messaging-outcome-claims-banned
description: Use when reviewing marketing copy for a legal AI assistant to identify outcome claims that are prohibited because they guarantee results, make false comparative superiority claims, or imply the product replaces professional legal judgment. Covers bar advertising rules, FTC/ASA standards, and UAE/KSA consumer protection frameworks. Pair with messaging-outcome-claims-allowed to understand what can be said instead.
license: MIT
metadata: " id: messaging.outcome-claims-banned category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, banned, outcome-claims, bar-advertising, FTC, ASA, consumer-protection] related: [messaging-outcome-claims-allowed, messaging-compliance-checker, messaging-banned-claims-consumer, messaging-banned-claims-lawyer, messaging-hard-rule-bible-signoff-required] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Messaging — Outcome Claims Banned

## When this applies

An **outcome claim** is any marketing statement that asserts a specific result achieved by using the product. Some outcome claims are permitted — with proper sourcing and disclaimers — per [[messaging-outcome-claims-allowed]]. The claims in this skill are **categorically banned** regardless of any evidence, disclaimer, or context. They are banned because:

1. They guarantee results that no legal AI product can guarantee (violating consumer protection law)
2. They imply the product performs the role of a licensed lawyer (triggering UPL and bar advertising rules)
3. They make comparative superiority claims without the methodology required to substantiate them legally

---

## Banned Outcome Claims — Verbatim and Category

### Legal Outcome Guarantees

| Banned claim | Why it is banned |
|--------------|-----------------|
| "Will win your case" | Guarantees a judicial or arbitral outcome — impossible for any legal AI to guarantee; violates bar advertising rules in every jurisdiction (KSA, UAE, Lebanon, UK, US) and consumer protection law |
| "Guaranteed outcome" | Any variant of a guaranteed legal result; the uncertainty of law makes this inherently false |
| "Get the result you deserve" | Implied outcome guarantee with subjective framing — equally prohibited |
| "We got them their money back" (used as a general marketing claim rather than a factual case study) | Implies guaranteed replication of a specific outcome |
| "Never lose a case" | Obvious guarantee; also defamatory risk if applied to lawyers using the product |

### Financial Guarantee Claims

| Banned claim | Why it is banned |
|--------------|-----------------|
| "Guaranteed to save money" | Financial outcome guarantee; false advertising under FTC (US), ASA (UK), and UAE/KSA consumer protection frameworks |
| "Save thousands on legal fees" (as a primary undifferentiated claim) | See [[messaging-banned-claims-consumer]]; also a false financial guarantee if unsupported |
| "Zero legal costs" | False; no product eliminates legal costs for all users in all situations |

### Lawyer Replacement Claims

| Banned claim | Why it is banned |
|--------------|-----------------|
| "Replaces your lawyer" | UPL implication; also a false capability claim — no AI product can replicate a licensed lawyer's judgment and fiduciary obligations |
| "Does the legal work for you" | Implies the product performs licensed legal services |
| "No need for a lawyer ever again" | Absolute claim + UPL implication; false for any realistic use case |

### Unsupported Comparative Claims

| Banned claim | Why it is banned |
|--------------|-----------------|
| "The most accurate legal AI" | Comparative superlative without defined, independently verified methodology is false advertising |
| "Better than [named competitor]" | Comparative claim without substantiated side-by-side benchmark; defamation and false advertising risk |
| "More accurate than a human lawyer" | Same; also professionally inflammatory with the buyer audience |

---

## Legal Authority

These prohibitions are grounded in:

| Framework | Jurisdictions | Relevant rule |
|-----------|---------------|---------------|
| Bar advertising rules (outcome claims) | KSA (Saudi Bar), Dubai Bar, Lebanon Bar Association, UK (SRA Code of Conduct), NY/CA Bar (US) | Prohibit outcome guarantees and comparative performance claims in legal services marketing |
| UK ASA / CAP Code | UK | Outcome claims must be substantiated; guarantees must be real and unconditional |
| FTC Act (Section 5) | US | Prohibits unfair or deceptive trade practices; outcome guarantees without substantiation are per se deceptive |
| UAE Consumer Protection Law (Federal Law 15/2020) | UAE | Prohibits misleading statements about product capabilities or results |
| KSA Consumer Protection Regulation | KSA | Prohibits misleading marketing claims and guarantees |

---

## Replace With

| Banned | Allowed replacement |
|--------|---------------------|
| "Will win your case" | "Helps you understand your options and prepare for your legal situation" |
| "Guaranteed to save money" | "Most users report saving time on routine legal tasks" (with source) |
| "Replaces your lawyer" | "Helps you understand the law — and get more from your lawyer meeting" |
| "Most accurate legal AI" | "Accuracy benchmark methodology available on request" (plus specific, sourced metric) |

---

## Enforcement

All customer-facing copy passes through [[messaging-compliance-checker]], which scans for these banned outcomes as Pass 2 of the four-pass review. Any flagged instance is a blocking issue: the asset cannot ship until the banned claim is removed and replaced with a compliant alternative.

---

## Related skills

- [[messaging-outcome-claims-allowed]]
- [[messaging-compliance-checker]]
- [[messaging-banned-claims-consumer]]
- [[messaging-banned-claims-lawyer]]
- [[messaging-hard-rule-bible-signoff-required]]
