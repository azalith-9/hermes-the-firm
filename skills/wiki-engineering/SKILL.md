---
name: wiki-engineering
description: Use when discussing engineering culture, process, or technical decisions for a legal-AI product. Covers code review standards, on-call and incident management, post-mortem practice, deployment pipelines, testing strategy, observability, and the architectural choices specific to legal-AI platforms (monolith vs microservices, multi-tenancy, compliance-grade logging). Reach for this skill when the user asks about eng culture, deployment practices, testing, or team engineering standards.
license: MIT
metadata: " id: wiki.engineering category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, engineering-culture, code-review, deployment, observability] related: [wiki-data, wiki-frontend, wiki-dev-design, wiki-haqq-product] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Registered as a flat plugin skill.
-->


# Engineering Culture and Practice for Legal-AI Products

## Scope

This pack covers engineering culture, process standards, and architectural guidance for a legal-AI product team. It is opinionated — these are the practices that reduce risk and improve velocity in small teams building products where correctness and trust matter.

---

## Engineering culture principles

### Correctness over speed (in production)

Legal professionals rely on the product to be accurate and available. A misrouted skill that generates a wrong jurisdiction answer, or a deployment that causes data loss, can destroy user trust. Apply the bias toward correctness to:
- Production deployments (test-first, staged rollout)
- LLM skill outputs (structured review gates before new skills reach users)
- Schema migrations (always reversible; never destructive without a backup)

### Boring technology

Prefer well-understood, battle-tested tools over the newest framework. The product's competitive advantage is in the legal domain and the AI quality, not the infrastructure novelty. Postgres is almost always the right database choice for the first three years. A monolith with well-defined modules beats premature microservices at < 20 engineers.

### Shared ownership

On-call rotation is not just for ops engineers — every engineer who ships a feature owns its production behaviour. Post-mortems are blameless and mandatory for P0/P1 incidents.

---

## Code review standards

### What a review must address

1. **Correctness** — Does the code do what the ticket says? Are edge cases (empty arrays, null values, unauthenticated requests) handled?
2. **Security** — Is user input validated and sanitised? Are access control checks present and correct? Are secrets stored in environment variables, never in code?
3. **Observability** — Are meaningful logs emitted? Are errors reported to the error tracker? Are metrics incremented?
4. **Test coverage** — Is there a test for the happy path and the key failure modes? Does the PR include a test for any bug it fixes?
5. **Design system alignment** — Does new UI use tokens and components from the library? (See [[wiki-dev-design]])

### Review etiquette

- Review within one business day. Blocking a PR for more than 24 hours without comment is a culture debt.
- Mark comments as `blocking:`, `suggestion:`, or `nit:` so authors know what must change vs what is optional.
- Approve with conditions rather than leaving a PR in requested-changes limbo if only nits remain.
- Leave positive comments for good patterns — normalise noticing what works.

---

## Testing strategy

### Layers

| Layer | What it covers | Tooling |
|---|---|---|
| Unit | Pure functions, utilities, business logic | Vitest (frontend/API), pytest (Python) |
| Integration | Database queries, external API clients, skill routing | Vitest + test containers, pytest + test DB |
| E2E | Critical user flows end-to-end | Playwright |
| AI output | Skill quality, hallucination detection | Custom eval harness (see [[wiki-data]] for eval logging) |

### Rules

- New features ship with unit + integration tests. No exceptions.
- E2E tests cover the five most critical paths: signup, first skill invocation, document upload, billing, logout.
- AI skill tests are not deterministic — run them in eval mode, not in CI assertions. Capture baseline pass rates and alert on regression.
- Target: CI green on `main` always. Broken `main` is a P1 incident.

---

## Deployment pipelines

### Environments

```
local dev → feature branch PR preview → staging → production
```

- **Feature branch preview**: auto-deployed on PR open via Vercel/Fly.io preview URL. Allows designer and PM review before merge.
- **Staging**: mirrors production config. Database is a copy of production with PII masked. All migrations run on staging first.
- **Production**: deploy after staging green + manual approval (or auto-deploy from `main` after passing all checks, depending on team maturity).

### Deployment checklist

- [ ] All CI checks green (lint, test, type-check, build)
- [ ] Database migration tested on staging with rollback plan documented
- [ ] Feature flags set correctly (new feature behind a flag for staged rollout)
- [ ] Runbook updated if this changes operational behaviour
- [ ] Monitoring alert thresholds reviewed (new endpoints, new error types)

### Database migration safety rules

1. Migrations are forward-only in production. Write a separate rollback migration; do not rely on `DOWN` in the same file.
2. Never add a `NOT NULL` column without a default, or drop a column that code still reads, in the same migration.
3. Large table migrations (> 1 M rows) require `CONCURRENTLY` index builds and offline/online migration strategy.
4. Always take a snapshot before running a migration on production.

---

## On-call and incident management

### Severity tiers

| Tier | Definition | Response time |
|---|---|---|
| P0 | Platform down or data loss | < 15 min response |
| P1 | Core feature unavailable, billing broken | < 1 hr response |
| P2 | Feature degraded, elevated error rate | < 4 hr response |
| P3 | Minor bug, cosmetic issue | Next sprint |

### On-call rotation

- Minimum 2-person rotation to avoid single points of failure
- On-call shifts: 1 week; hand-off meeting includes: open P1/P2 issues, deployment notes, any flaky alerts
- Runbook for every recurring alert type; update after each incident

### Post-mortem practice

Mandatory for P0 and P1; optional but encouraged for P2. Format:

```
## Post-mortem: [Incident title] — [Date]

### Summary (2–3 sentences)
### Timeline
### Root cause
### Impact (users affected, duration, data affected)
### What went well
### What went wrong
### Action items (owner, due date)
```

Post-mortems are blameless. The goal is system improvement, not individual accountability.

---

## Observability

### The three pillars

- **Logs** — structured JSON logs from all services. Key fields: `level`, `service`, `trace_id`, `user_id` (hashed/pseudonymised), `duration_ms`, `status_code`. Ship to a log aggregator (Datadog, Better Stack, Axiom).
- **Metrics** — application-level counters and histograms. Key metrics: request rate, error rate, p50/p95/p99 latency, LLM token usage, skill invocation counts.
- **Traces** — distributed tracing for the AI pipeline is especially important: a single user request may span the router, multiple skill calls, a vector DB query, and an LLM API call. Use OpenTelemetry.

### Alerting rules

- Error rate > 1% for any endpoint → P2 alert
- p95 latency > 5 s for any LLM skill → P3 alert; > 30 s → P2
- Any 5xx on `/api/billing` → P1 alert
- Audit log ingestion rate drops > 50% vs 7-day baseline → P1 alert (may indicate data loss)

---

## Monolith vs microservices

For teams under ~15 engineers building a legal-AI product: **start with a modular monolith**. The AI skill layer naturally decomposes into modules (router, skills, connectors, auth, billing) without needing separate deployments. Premature service extraction adds operational overhead with no benefit at this scale.

When to extract a service:
- Independent scaling requirements (e.g. a document-processing worker that must scale independently of the web tier)
- Independent deployment cadence required by organisational boundaries (e.g. a separate team owns the billing service)
- Hard security boundary required (e.g. PII processing must be isolated and audited separately)

---

## Caveats & currency

Engineering tooling evolves rapidly. Vitest superseded Jest for most new projects but check the current Next.js recommended testing setup. OpenTelemetry instrumentation for the AI SDK tier changes as the SDK matures; check the `@vercel/otel` or `opentelemetry-sdk-node` docs for the current recommended setup.

---

## Related skills

- [[wiki-data]]
- [[wiki-frontend]]
- [[wiki-dev-design]]
- [[wiki-haqq-product]]
