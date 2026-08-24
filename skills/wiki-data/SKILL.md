---
name: wiki-data
description: Use when designing, debugging, or discussing the data infrastructure for a legal-AI product. Covers ingestion pipelines, data warehousing (dbt, Snowflake, BigQuery, Postgres), analytical modeling, and the specific requirements of legal-AI data stores — audit logs, prompt-completion records, user analytics, and privacy-preserving design. Reach for this skill when the user asks about data modeling, pipeline architecture, analytics, or compliance-grade logging for a legal platform.
license: MIT
metadata: " id: wiki.data category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, data-pipeline, warehouse, analytics, audit-logs] related: [wiki-engineering, wiki-memory, wiki-frontend, wiki-haqq-product] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Data Infrastructure for Legal-AI Products

## Scope

This pack covers data pipeline design, warehouse choices, analytical modeling, and the special-purpose stores a legal-AI product requires: audit logs, prompt-completion archives, user analytics, and entity extraction stores. It applies to both the internal analytics layer (understanding how the product is used) and the operational data layer (state that the AI system reads and writes at runtime).

---

## Architecture overview

A legal-AI data stack has three conceptually distinct tiers:

```
Operational DB (Postgres / Supabase)
        │
        ▼
Streaming / CDC layer (Kafka, Debezium, or pg_logical)
        │
        ▼
Raw storage / lake (S3, GCS)
        │
        ▼
Warehouse (Snowflake / BigQuery / dbt-modelled Postgres)
        │
        ▼
BI layer (Metabase, Superset, or direct SQL notebooks)
```

For early-stage products (< 10 k MAU), a single Postgres instance with dbt models running against it is often sufficient. Graduate to Snowflake or BigQuery when query times on the operational database begin affecting product latency or when CDC fan-out is needed.

---

## Data stores and their purposes

### 1. Operational database (Postgres)

The primary source of truth for application state:

- **Users and workspaces** — accounts, billing state, permissions, plan tiers
- **Matters / projects** — legal work items, associated documents, status
- **Documents** — metadata records (content stored in object storage or vector store)
- **Skills / routing** — active skill configurations, feature flags per workspace
- **Conversations** — session-level chat records (foreign key to user + matter)

Schema design notes for legal-AI:
- Always include `created_at`, `updated_at`, and a `deleted_at` soft-delete field — legal records must not be hard-deleted.
- Row-level security (RLS) in Postgres/Supabase is the right default for multi-tenant legal data; do not rely solely on application-layer access control.
- Every table that holds client data should carry a `jurisdiction` column — enables data residency filtering and compliance reporting.

### 2. Prompt-completion store

All LLM interactions must be logged for:
- **Audit / accountability** — legal professionals may need to show which AI responses informed a work product
- **Quality monitoring** — flagging hallucinations, tracking skill hit rates
- **Billing** — token-based cost attribution per workspace or matter

Minimum schema:

```sql
prompt_completions (
  id          uuid PRIMARY KEY,
  workspace_id uuid NOT NULL,
  matter_id   uuid,
  user_id     uuid NOT NULL,
  skill_id    text,               -- which skill routed this
  model       text,               -- e.g. claude-sonnet-4-5
  prompt_tokens  int,
  completion_tokens int,
  latency_ms  int,
  created_at  timestamptz NOT NULL DEFAULT now(),
  jurisdiction text,
  -- do NOT store raw prompt/completion in main table; link to encrypted blob
  blob_ref    text                -- S3/GCS key of encrypted content
)
```

**Privacy design:** Never store raw prompt text in the operational database unencrypted. Store a reference to an encrypted blob in object storage. Apply retention policies per workspace (configurable, minimum 90 days for legal-grade accounts, deletion on request).

### 3. Audit log store

Immutable event stream of all actions taken on the platform:

- Document uploads, downloads, deletions
- Skill invocations with outcome (success / flagged / escalated)
- Permission changes, user additions, billing events
- Data exports

Use an append-only table or a dedicated audit service (e.g. write to a separate Postgres schema with no `DELETE` or `UPDATE` grants to the application role). For compliance-grade deployments in UAE PDPL or KSA PDPL contexts, the audit log may itself need to be retained for a regulatory minimum period.

### 4. Vector / embedding store

Used for retrieval-augmented generation (RAG) over firm documents:

- Pinecone, pgvector, or Weaviate depending on scale
- Each embedding record should carry: `document_id`, `chunk_index`, `jurisdiction`, `matter_id`, `workspace_id`, `model_version` (for re-embedding when model changes)
- Access control at query time: filters must enforce `workspace_id` isolation — cross-workspace retrieval is a critical security failure mode in multi-tenant legal products

### 5. Analytics warehouse

Feed from the operational DB via CDC or nightly export:

- **dbt models** transform raw event tables into fact/dimension schema
- Key marts: `fct_sessions`, `fct_skill_invocations`, `dim_users`, `dim_workspaces`, `fct_documents_processed`
- Run on BigQuery (large scale) or a dbt-core local project against Postgres (early stage)

---

## dbt conventions for legal-AI analytics

```
models/
  staging/       -- 1:1 with source tables, light cleaning only
  intermediate/  -- joins, window functions, business logic
  marts/
    growth/      -- activation, retention, expansion metrics
    product/     -- feature usage, skill hit rates, latency
    finance/     -- MRR, ARR, billing events (see [[wiki-finance]])
```

Key metrics to model:
- **Skill utilisation rate** — `skill_invocations / active_sessions` by skill_id
- **Matter completion rate** — sessions that produce a document or explicit user-confirmed output
- **Escalation rate** — skill-level flag rate (AI declines, routes to lawyer)
- **Time-to-first-value** — minutes from signup to first completed skill invocation

---

## Privacy and data residency

MENA jurisdictions impose data residency requirements that affect warehouse choices:

| Jurisdiction | Applicable framework | Key requirement |
|---|---|---|
| UAE | UAE PDPL (Federal Decree-Law No. 45/2021) | Consent for cross-border transfer; government data must stay onshore |
| KSA | KSA PDPL (Royal Decree M/19) | Transfer requires NCA approval or adequate-protection finding |
| DIFC | DIFC Data Protection Law 2020 | Modelled on GDPR; adequacy decisions or SCCs required |
| ADGM | ADGM Data Protection Regulations 2021 | Similar to GDPR; independent regulator |
| Lebanon | No comprehensive PDPL yet | Sector-specific rules apply; watch draft law |
| Egypt | Egypt PDPL (Law 151/2020) | Sensitive data; explicit consent required |

For multi-region deployments: use Supabase projects or cloud regions per jurisdiction boundary; never co-mingle data from jurisdictions with conflicting residency rules in a single warehouse without proper anonymisation.

---

## Observability and alerting

- Pipeline failures should alert within 5 minutes via PagerDuty or equivalent.
- Row count anomaly detection on key tables (prompt_completions, audit_log) — a sudden drop signals ingestion failure, not reduced usage.
- Data freshness SLAs: operational metrics < 5 min lag; warehouse models < 2 hr lag during business hours.

---

## Caveats & currency

Data privacy laws in MENA are evolving rapidly. The frameworks cited above were current as of early 2026; check the relevant authority's official website (UAE TDRA, Saudi NCA, DIFC Commissioner of Data Protection) before implementing cross-border data flows. dbt and warehouse tool version requirements change frequently; pin versions in your `packages.yml` and test upgrades in a staging environment.

---

## Related skills

- [[wiki-engineering]]
- [[wiki-memory]]
- [[wiki-frontend]]
- [[wiki-haqq-product]]
- [[wiki-finance]]
