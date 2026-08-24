---
name: justice-intent-developer-api
description: Use when the public-facing assistant detects that a user is a developer asking about API access, SDK integration, webhooks, or building on top of Louis. Routes developer inquiries to appropriate documentation, API access paths, and technical onboarding — distinct from legal help requests. Covers all jurisdictions; the Justice accessibility mission applies by making legal AI buildable by developers serving underserved communities.
license: MIT
metadata: " id: justice.intent.developer-API category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, developer, api, sdk, integration, build-on-top] related: [justice-intent-feature-question, justice-intent-partnership-inquiry, justice-intent-sales, justice-intent-security-compliance] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Justice Intent — Developer API Inquiry

## When to use this

Trigger when the message contains any of the following signals:

- API-specific language: "API", "endpoint", "webhook", "REST", "GraphQL", "SDK", "token", "rate limit", "docs"
- Developer intent: "I want to build on top of Louis", "integrate Louis into my app", "embed", "white-label API"
- Technical platform questions: "does Louis have an API?", "can I call Louis from my code?", "what's the API cost?"
- Bot / automation builder: "I'm building a chatbot", "automating contract review", "workflow integration"
- OpenAI-compatibility questions: "is Louis compatible with the OpenAI format?"

Do **not** trigger on general "how do I use Louis?" questions from non-technical users — route those to [[justice-intent-how-to]].

## Response actions

1. **Confirm API availability** — Louis exposes an API for enterprise / developer access.
2. **Route to developer docs** at `/developer` or `docs.haqq.ai` (whichever is canonical at the time).
3. **Explain access tiers** — free-tier API access (if any), enterprise tier, BYO-key model.
4. **Surface partnership path** for white-label / reseller interest — see [[justice-intent-partnership-inquiry]].
5. **Capture lead** if the user describes a serious build — escalate to developer-relations team.

## API access model

| Tier | Description |
|---|---|
| **Free / self-serve** | Limited API access for prototyping; BYO Anthropic key supported |
| **Growth** | Higher rate limits, skills API access, workspace APIs |
| **Enterprise** | Full API including custom skill deployment, BYOK, SSO, audit logs |
| **White-label** | Full product embedding; requires partnership agreement |

## Key developer capabilities to mention

- **Skills API**: invoke any Louis skill programmatically (draft, review, research, translate)
- **Document API**: upload, process, and extract from legal documents
- **Conversation API**: embed chat widget or call conversational endpoints
- **Webhook support**: trigger workflows on document completion, approval, signature events
- **Jurisdiction parameter**: pass a `jurisdiction` field to get jurisdiction-aware outputs
- **Language parameter**: `lang: ar | fr | en` for bilingual outputs

## Justice / accessibility angle for developers

Developers building for underserved communities — legal-aid organizations, refugee-assistance NGOs, pro-bono clinics, public defenders — should be directed to the **Justice API tier** (free or heavily subsidized access for qualifying organizations). This is the programmatic extension of HAQQ's accessibility mission.

Qualifying signals:
- "NGO", "nonprofit", "pro bono", "legal aid", "public defender", "refugee"
- "low-income", "community clinic", "access to justice"

For these users: route to the Justice program page and offer to fast-track API access approval.

## Tone and response shape

- Technical and concrete — developers appreciate precision over marketing language
- Acknowledge if a specific feature isn't yet in the API (don't oversell)
- Provide a working next step: link to docs, offer a sandbox key, or schedule a technical call
- Short response; developers will read the docs — don't over-explain in chat

## Example exchange

User: *"Does Louis have an API I can use to build a contract review app?"*

> "Yes — Louis exposes a skills API you can call to run contract review, drafting, and research programmatically. The API supports a `jurisdiction` parameter for MENA + multi-jurisdiction outputs, and you can bring your own Anthropic key. Developer docs are at docs.haqq.ai/api. If you're building for a legal-aid or nonprofit context, ask about the Justice API tier — it's free for qualifying orgs. Want me to walk you through the quick-start?"

## Do not

- Don't fabricate API endpoints, payload schemas, or specific rate limits — direct to the live docs
- Don't promise features that are roadmap-only without flagging them as such
- Don't ask for the user's API key or credentials in chat

## Related skills

- [[justice-intent-feature-question]]
- [[justice-intent-partnership-inquiry]]
- [[justice-intent-sales]]
- [[justice-intent-security-compliance]]
