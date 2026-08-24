---
name: connector-cloudflare
description: Use when a legal-AI platform engineer or operator needs to manage Cloudflare infrastructure — DNS records, Pages deployments, Workers scripts, R2 object storage, and KV namespaces — from within an AI-assisted workflow. Scoped to platform operations for legal-tech products; not a general Cloudflare tutorial. Triggers on requests to deploy, configure, or inspect Cloudflare resources for the legal-AI product stack.
license: MIT
metadata: " id: connector.cloudflare category: connector jurisdictions: [__multi__] priority: P2 intent: [__connector__] related: [connector-posthog, connector-stripe, connector-scheduled-tasks] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Registered as a flat plugin skill.
-->


# Connector — Cloudflare

## What it does

The Cloudflare connector exposes Cloudflare's account and zone APIs to AI-assisted platform operations for legal-AI products. It is an **internal engineering tool** — used by operators and platform engineers, not by end-user lawyers. Its primary purpose is enabling automated or AI-assisted deployment, configuration, and monitoring of the infrastructure that hosts the legal-AI product.

Typical operations:
- Publishing new versions of a legal-AI frontend to Cloudflare Pages.
- Deploying or updating Workers edge functions (e.g., rate-limiting middleware, request routing).
- Managing R2 buckets that store matter documents or OCR outputs.
- Updating KV namespaces used for skill-cache or tenant configuration.
- Rotating DNS records after a domain migration or A/B test.

## Setup / auth

### API token (per-tenant, scoped)

Authentication uses Cloudflare API tokens — not the global API key. Best practice:

1. Create a dedicated token per service/deployment purpose (not one shared token for everything).
2. Scope the token to specific **zones** (domains) and **accounts** as narrow as the job requires.
3. Store the token in the platform's secrets manager (never in code or environment variables committed to VCS).
4. Rotate tokens every 90 days or immediately after any suspected exposure.

### Recommended token permission sets

| Use case | Required permissions |
|---|---|
| Deploy to Pages | `Account:Cloudflare Pages:Edit` |
| Deploy Workers | `Account:Workers Scripts:Edit` |
| Manage DNS | `Zone:DNS:Edit` for the specific zone |
| R2 storage | `Account:Workers R2 Storage:Edit` |
| KV namespaces | `Account:Workers KV Storage:Edit` |
| Read-only monitoring | `Zone:Analytics:Read`, `Account:Account Analytics:Read` |

Never grant `Account:Administrator` to an API token used by automated processes.

## Capabilities

### DNS management
- List, create, update, delete A / AAAA / CNAME / TXT / MX records.
- Manage proxied vs unproxied records (orange-cloud vs grey-cloud).
- Update TTL values.

### Cloudflare Pages
- List projects and deployments.
- Trigger a new deployment from a source branch (Wrangler-based or direct upload).
- Roll back to a previous deployment.
- Manage custom domains and redirect rules.
- Set environment variables per environment (production / preview).

### Workers
- List deployed Workers and their routes.
- Upload new Worker script versions.
- Manage Worker routes and zone bindings.
- View Worker CPU time and error metrics via the analytics API.
- Manage Durable Objects and their namespaces.

### R2 Object Storage
- List buckets and their contents.
- Create and delete buckets.
- Upload, download, and delete objects (files).
- Set bucket CORS and access policies.

In legal-AI contexts, R2 is often used to store:
- Uploaded client documents pending OCR processing.
- Signed PDF versions of generated contracts.
- Scanned court documents awaiting review.

All R2 objects containing client matter content must be tagged with a tenant/matter reference and encrypted at rest (Cloudflare handles encryption; the application must handle correct bucket-per-tenant isolation).

### KV Namespaces
- List namespaces and keys.
- Read and write key-value pairs (with TTL).
- Delete keys.

In legal-AI contexts, KV is used for:
- Skill-cache: caching the compiled skill set per tenant for fast skill routing.
- Tenant config: storing lightweight tenant-level settings (jurisdiction preference, language, persona).
- Rate-limit counters: tracking per-user API call counts.

## Permissions & safety

- **Principle of least privilege.** Every automated workflow uses a narrowly scoped token. Never use a token with broader permissions than the current task requires.
- **Tenant isolation.** Each legal-AI tenant's content in R2 must be stored in a separate bucket (not a prefix within a shared bucket). Cross-tenant reads are a critical failure.
- **No accidental DNS changes.** DNS edits have immediate global effect. Before any DNS change, present the current record and the proposed change to a human operator for confirmation. Never modify DNS autonomously.
- **Worker deployment gates.** Production Worker deployments should require CI/CD pipeline sign-off, not direct AI-driven deployment without human review.
- **Audit log.** All API calls through this connector are logged with timestamp, operation, resource ID, and actor.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| `403 Forbidden` | Token lacks permission for the resource | Check token scopes; never expand automatically — alert operator |
| `10000 Authentication error` | Invalid or expired token | Prompt operator to rotate and update token in secrets manager |
| R2 upload timeout | Object >5GB or slow network | Use multipart upload for large documents; chunk at 100MB |
| Pages deployment stuck | Build hook not triggered | Check Pages build configuration; re-trigger manually |
| KV quota exceeded | Account on free plan with >1 billion reads/month | Alert platform team; upgrade plan or implement local caching |
| DNS propagation lag | Global propagation takes up to 48h for uncached records | Inform engineer; do not retry with a different record while the first is propagating |

## Related skills

- [[connector-posthog]]
- [[connector-stripe]]
- [[connector-scheduled-tasks]]
