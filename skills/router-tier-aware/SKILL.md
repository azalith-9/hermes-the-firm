---
name: router-tier-aware
description: Use to respect user plan tier and credit balance before executing any tool call or premium feature. Maps five subscription tiers (free, starter, pro, business, enterprise) to available feature sets, enforces graceful degradation for blocked features, and surfaces upgrade CTAs when a user hits a tier wall. Never silently degrades output quality or refuses without a path forward.
license: MIT
metadata: " id: router.tier-aware category: router priority: P0 intent: [__router__] related: [router-tool-selector, router-complexity-grader, router-persona-selector, router-intent-detection] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'router'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Tier-Aware Gating

## Purpose

Louis operates across multiple subscription tiers. Premium features — deep-research, RAG over private corpora, web search, agentic workflows, exports — are available only on paid tiers. The tier-aware gate enforces these boundaries while maintaining a good user experience: explaining clearly what the user is missing, surfacing the upgrade path, and always offering the best possible answer within the current tier's constraints.

The rule is: **degrade gracefully, never silently**. A user who hits a tier wall should understand exactly what they are missing and how to get it.

## Tier Definitions

### `free`

**What is included**:
- Model inference for short-answer and medium-complexity requests
- Generic legal knowledge questions answered from model training
- Boilerplate drafting (NDA template, standard clause generation) without firm-specific context
- Basic document review without private KB access

**What is blocked**:
- RAG over private corpus (firm KB or personal document store)
- Deep-research mode (RAG over public legal corpus + web search)
- All calculator tools
- Agentic workflows
- Document exports (PDF/DOCX download)
- Priority response queue

**Credit model**: limited credits per period (number defined in billing configuration)

### `starter`

**What is added over free**:
- RAG over personal document store (uploaded documents)
- Light deep-research (RAG over public legal corpus; no web search)
- Basic calculator tools (EOSG, notice period)
- Document export (limited formats)

### `pro`

**What is added over starter**:
- Full RAG (firm KB + public legal corpus + personal)
- Full deep-research (RAG + web search)
- All calculator tools (interest, stamp duty, statutory deadlines)
- Document export (all formats)
- Multi-turn conversation memory
- Priority response queue

### `business`

**What is added over pro**:
- eFirm features: matter management, billing integration, team collaboration
- Shared firm knowledge base (shared across all team users)
- Connector integrations (Linear, HubSpot, Stripe)
- Team-level usage analytics
- Matter-scoped conversations

### `enterprise`

**What is added over business**:
- SSO (Single Sign-On) integration
- Full audit log (who asked what, when)
- On-premises or private-cloud deployment option
- Dedicated support SLA
- Custom knowledge base onboarding
- API access with SLA-backed response times

## Behavior Rules

### Rule 1 — Never Silently Refuse

If a user on a lower tier requests a feature that is not available:
- Do NOT silently return a lower-quality answer (e.g., answer a deep-research question with a generic model answer without telling the user they are not getting the full depth)
- DO explain what is happening and why

### Rule 2 — Inline Upgrade CTA (Contextual)

When a tier wall is hit, surface a one-line upgrade call-to-action at the end of the response. Keep it contextual — tell the user what they would get if they upgraded.

Example: "To access our public legal corpus with 6.3M laws across 50+ jurisdictions for this research, upgrade to Pro. [Upgrade now →]"

Do not repeat the CTA in subsequent turns of the same conversation unless the user explicitly asks about pricing or features.

### Rule 3 — Credit Warnings

- At < 20% of remaining credits: append a one-line warning at the end of each response: "You have [X]% of your monthly credits remaining. [Manage credits →]"
- At 0 credits: hard refusal with a single CTA. Do not generate any substantive output — the credit system must be respected.
- At 0 credits, do NOT degrade silently to a free-tier answer — the user has used their allocation; they should top up or wait for renewal.

### Rule 4 — Features Available Within Tier

Before executing any tool call, check whether the tool is available at the current tier:

```
free: [model-inference]
starter: [model-inference, rag-personal, calc-basic]
pro: [model-inference, rag-personal, rag-firm, rag-public, web-search, calc-all, export]
business: [all-pro, efirm-matter, efirm-billing, connectors]
enterprise: [all-business, sso, audit-log, on-prem-option, api-sla]
```

### Rule 5 — No Partial Tool Execution

Do not execute a tool call that will return a billing error mid-stream. Check tier + credits before invoking any tool; if blocked, surface the message before starting.

## Output to Downstream

```json
{
  "tier": "free|starter|pro|business|enterprise",
  "credits_remaining": <integer or null if unlimited>,
  "credits_warning": true/false,
  "features_available": ["<tool-id>", ...],
  "features_blocked": ["<tool-id>", ...],
  "upgrade_cta": "<null or one-line upgrade message>"
}
```

## Related Skills

- [[router-tool-selector]]
- [[router-complexity-grader]]
- [[router-persona-selector]]
- [[router-intent-detection]]
