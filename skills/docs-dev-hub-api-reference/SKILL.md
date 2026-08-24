---
name: docs-dev-hub-api-reference
description: Use when a developer asks how to integrate with the platform API, authenticate requests, call specific endpoints, handle webhooks, or manage rate limits. This is a platform documentation skill covering the REST and streaming API, SDK installation, authentication, versioning, idempotency, and webhook event structure for the developer hub.
license: MIT
metadata: " id: docs.dev-hub-API-reference category: docs jurisdictions: [__multi__] priority: P2 intent: [__docs__, api, sdk, developer, integration, webhooks, authentication] related: [docs-enterprise-deployment, docs-audit-log-export, docs-case-study-legal-ontology] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Registered as a flat plugin skill.
-->


# Developer Hub — API Reference

## Overview

The platform exposes a REST API for integration with third-party systems, custom legal workflows, and developer-built legal tools. The API enables:

- Invoking legal AI skills programmatically (drafting, review, research).
- Managing matters, documents, and users from external systems.
- Streaming AI-generated legal content into custom interfaces.
- Subscribing to platform events via webhooks (new matter, document generated, user activity).

The developer hub lives at `/developers` in the platform navigation, or at the dedicated developer portal URL provided during onboarding.

## Authentication

All API requests require authentication via a Bearer token:

```
Authorization: Bearer {api_key}
```

API keys are created and scoped in **Settings → Developer → API Keys**. Each key has:
- A **name** (for identification in audit logs).
- A **scope** (read-only, read-write, admin, or custom scopes per resource type).
- An optional **expiry date**.
- An **IP allowlist** (optional; restricts key usage to specified IP ranges).

**Best practices**:
- Create separate API keys per integration (one for your CRM, one for your document management system, one for automated workflows).
- Use the minimum necessary scope for each key.
- Rotate keys on a schedule (quarterly for sensitive integrations; immediately on suspected compromise).
- Never commit API keys to source code repositories.

## Base URL and versioning

```
https://api.{platform-domain}/v2/
```

The API is versioned. The current stable version is **v2**. Breaking changes are never introduced within a version; new versions are released with 90-day notice and a parallel deprecation period for the old version.

Version is specified in the URL path. Requests without a version prefix are rejected. Check `GET /versions` for the current supported version list and deprecation dates.

## REST API — core endpoints

### Skills

```
POST /v2/skills/invoke
{
  "skill_id": "conversation-intake-nda",
  "inputs": {
    "jurisdiction": "DIFC",
    "parties": ["Acme Ltd", "XYZ Corp"],
    "purpose": "technology partnership evaluation",
    "term_years": 2
  },
  "stream": false
}
```

Returns a structured JSON response with the skill output. Set `"stream": true` for Server-Sent Events (SSE) streaming response.

### Documents

```
GET  /v2/documents/{document_id}
POST /v2/documents
PUT  /v2/documents/{document_id}
DEL  /v2/documents/{document_id}
GET  /v2/documents?matter_id={id}&type=NDA&jurisdiction=UAE
```

### Matters

```
GET  /v2/matters
POST /v2/matters
GET  /v2/matters/{matter_id}
PUT  /v2/matters/{matter_id}
```

### Users and workspace

```
GET  /v2/workspace
GET  /v2/users
POST /v2/users                  # Create user (admin scope required)
DEL  /v2/users/{user_id}        # Deactivate user
```

### Audit logs

```
GET /v2/audit-logs?from_date=2025-01-01&to_date=2025-03-31&user_id={id}
```

See [[docs-audit-log-export]] for full filter options.

## Streaming API

For AI-generated content (drafts, analyses, research), use Server-Sent Events (SSE) streaming:

```
POST /v2/skills/invoke
Content-Type: application/json
Accept: text/event-stream
{
  "skill_id": "draft-nda-mutual",
  "stream": true,
  ...
}
```

The server streams token-by-token chunks as `data:` events. Each chunk is a JSON object:
```
data: {"delta": "The parties agree that...", "index": 1, "done": false}
data: {"delta": null, "index": 847, "done": true}
```

Streaming is recommended for any generation task where displaying tokens progressively improves UX.

## Webhooks

Subscribe to platform events to trigger external workflows:

```
POST /v2/webhooks
{
  "url": "https://your-server.com/webhook",
  "events": ["document.created", "matter.closed", "user.invited"],
  "secret": "your_signing_secret"
}
```

Webhook events are signed with HMAC-SHA256 using the secret. Verify signatures before processing:

```
X-Signature: sha256={hex_digest}
```

Standard event types: `document.created`, `document.exported`, `matter.created`, `matter.closed`, `user.invited`, `audit.export.completed`, `skill.invoked`.

Webhook payloads are delivered with a maximum of 3 retries on failure, with exponential backoff.

## Rate limits

| Plan | Requests per minute | Concurrent streams |
|---|---|---|
| Free | 20 | 1 |
| Professional | 100 | 3 |
| Team | 300 | 10 |
| Enterprise | Custom (configured per account) | Custom |

Rate limit status is returned in response headers:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1715789400
```

On limit exhaustion, the API returns HTTP 429. Back off and retry after the `Retry-After` header value (seconds).

## Idempotency

For `POST` requests that create resources, supply an `Idempotency-Key` header to prevent duplicate creation on retry:

```
Idempotency-Key: {uuid-v4}
```

Idempotency keys are valid for 24 hours. Duplicate requests with the same key within the window return the original response.

## SDK installation

```bash
# Node.js / TypeScript
npm install @platform/legal-ai-sdk

# Python
pip install legal-ai-sdk

# Ruby
gem install legal-ai-sdk
```

SDK documentation and code examples are available in the developer portal. The SDK handles authentication, streaming, retry logic, and rate limit backoff automatically.

## Error handling

All errors return a structured JSON body:

```json
{
  "error": {
    "code": "SKILL_NOT_FOUND",
    "message": "No skill with ID 'draft-fake-skill' exists.",
    "request_id": "req_abc123"
  }
}
```

Standard HTTP status codes: `400` (bad request), `401` (unauthorized), `403` (forbidden / insufficient scope), `404` (not found), `422` (validation error), `429` (rate limited), `500` (server error).

Include `request_id` when contacting support.

## Related skills

- [[docs-enterprise-deployment]]
- [[docs-audit-log-export]]
- [[docs-case-study-legal-ontology]]
