---
name: eng-tenant-isolation-row-level-security
description: Use when designing, auditing, or debugging the PostgreSQL Row Level Security (RLS) policies that enforce tenant isolation in the multi-tenant legal AI product. Covers the membership-based isolation model, policy patterns for all core tables, common bypass traps, and the mandatory integration test suite that verifies no cross-tenant data leakage.
license: MIT
metadata: " id: eng.tenant-isolation-row-level-security category: eng jurisdictions: [__multi__] priority: P2 intent: [__eng__, rls, multi-tenant, security, supabase, postgresql] related: [eng-supabase-edge-functions-patterns, eng-supabase-index-knowledge-pipeline, eng-pii-redaction-preprocessor, safety-client-confidentiality-cross-tenant] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Tenant Isolation — Row Level Security

## What it does

In a legal AI product handling confidential client documents from multiple law firms and companies, a data leak between tenants is catastrophic — ethically, legally, and commercially. Row Level Security (RLS) is the primary database-level enforcement mechanism that guarantees Tenant A's data can never be read by Tenant B, regardless of application-layer bugs.

This skill defines the RLS model, policy patterns, mandatory test cases, and common pitfalls for the Supabase/PostgreSQL multi-tenant schema.

## Setup / auth

RLS must be enabled on every table that contains tenant-scoped data:

```sql
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE document_chunks ENABLE ROW LEVEL SECURITY;
ALTER TABLE chat_messages ENABLE ROW LEVEL SECURITY;
ALTER TABLE chat_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE pii_audit_log ENABLE ROW LEVEL SECURITY;
ALTER TABLE explainer_videos ENABLE ROW LEVEL SECURITY;
```

The access identity comes from `auth.uid()` (Supabase JWT). The JWT is propagated to Postgres via the `anon` or `authenticated` role set by the PostgREST gateway.

## Capabilities

### Tenancy model

The product uses a **workspace-based multi-tenancy** model:

```
auth.users (one per person)
    ↓
memberships (user ↔ workspace, with role: owner | admin | member | viewer)
    ↓
workspaces (one per law firm / company)
    ↓
all data tables (workspace_id / tenant_id column)
```

The key lookup helper:
```sql
-- Reusable inline function (materialized once per query via security definer)
CREATE FUNCTION current_workspace_ids()
RETURNS UUID[]
LANGUAGE SQL SECURITY DEFINER STABLE AS $$
  SELECT ARRAY(
    SELECT workspace_id FROM memberships
    WHERE user_id = auth.uid() AND status = 'active'
  )
$$;
```

### Canonical RLS policy pattern

```sql
-- Single-workspace tables (user belongs to exactly one workspace for a resource)
CREATE POLICY "tenant read isolation"
  ON documents FOR SELECT
  USING (tenant_id = ANY(current_workspace_ids()));

CREATE POLICY "tenant write isolation"
  ON documents FOR INSERT
  WITH CHECK (tenant_id = ANY(current_workspace_ids()));

CREATE POLICY "tenant update isolation"
  ON documents FOR UPDATE
  USING (tenant_id = ANY(current_workspace_ids()))
  WITH CHECK (tenant_id = ANY(current_workspace_ids()));

CREATE POLICY "tenant delete isolation"
  ON documents FOR DELETE
  USING (tenant_id = ANY(current_workspace_ids()));
```

### Role-based access within a tenant

Some tables need finer control within a workspace (e.g., only `owner` / `admin` can delete documents):

```sql
CREATE POLICY "admin delete documents"
  ON documents FOR DELETE
  USING (
    tenant_id = ANY(current_workspace_ids())
    AND EXISTS (
      SELECT 1 FROM memberships
      WHERE user_id = auth.uid()
        AND workspace_id = documents.tenant_id
        AND role IN ('owner', 'admin')
        AND status = 'active'
    )
  );
```

### System-wide knowledge (no tenant_id)

For tables that hold shared legal knowledge (legislation, public regulatory guidance) accessible to all authenticated users:

```sql
CREATE POLICY "authenticated read system knowledge"
  ON system_chunks FOR SELECT
  USING (auth.role() = 'authenticated');

-- No INSERT/UPDATE/DELETE for non-service-role users
```

### Audit log (append-only)

The `pii_audit_log` table must be append-only for users — no UPDATE or DELETE:

```sql
CREATE POLICY "tenant audit log read"
  ON pii_audit_log FOR SELECT
  USING (tenant_id = ANY(current_workspace_ids()));

CREATE POLICY "tenant audit log insert"
  ON pii_audit_log FOR INSERT
  WITH CHECK (tenant_id = ANY(current_workspace_ids()));

-- No UPDATE or DELETE policies → implicit deny
```

## Integration test suite (mandatory)

Every deploy must pass these tests before reaching production:

```typescript
describe("RLS tenant isolation", () => {
  test("user from tenant A cannot read tenant B documents", async () => {
    const docB = await createDoc(tenantB);
    const { data, error } = await supabaseAs(userA).from("documents").select().eq("id", docB.id);
    expect(data).toHaveLength(0);
  });

  test("user from tenant A cannot read tenant B chunks", async () => {
    const chunkB = await createChunk(tenantB);
    const { data } = await supabaseAs(userA).from("document_chunks").select().eq("id", chunkB.id);
    expect(data).toHaveLength(0);
  });

  test("vector search does not return cross-tenant chunks", async () => {
    const chunks = await retrieveRelevantChunks(testQuery, tenantA.id);
    chunks.forEach(c => expect(c.tenant_id).toBe(tenantA.id));
  });

  test("audit log cannot be deleted by tenant user", async () => {
    const { error } = await supabaseAs(userA).from("pii_audit_log").delete().neq("id", "none");
    expect(error).not.toBeNull(); // RLS blocks delete
  });

  test("service role bypasses RLS (expected)", async () => {
    const { data } = await supabaseServiceRole.from("documents").select();
    expect(data!.length).toBeGreaterThan(1); // sees all tenants
  });
});
```

The last test confirms the expected behavior of service role — document it so engineers don't accidentally use service role in user-facing Edge Functions.

## Common traps

| Trap | Consequence | Fix |
|---|---|---|
| Table created without `ENABLE ROW LEVEL SECURITY` | All rows readable by all users | Add `ALTER TABLE ... ENABLE ROW LEVEL SECURITY` and a permissive/deny policy |
| Using service role key in a user-facing Edge Function | RLS bypassed | Audit all Edge Function deployments for key type |
| `current_workspace_ids()` not SECURITY DEFINER | Can be overridden by malicious Postgres session | Always use `SECURITY DEFINER` for helper functions |
| Forgetting `WITH CHECK` on INSERT/UPDATE | Can insert rows into another tenant's scope | Always pair `USING` with `WITH CHECK` |
| pgvector `match_chunks` RPC bypasses RLS | Cross-tenant vector search results | Embed `WHERE tenant_id = $1` in the SQL function itself |
| Soft-delete (`deleted_at`) without RLS filter | Deleted rows from other tenants still visible | Add `AND deleted_at IS NULL` to USING clause |

## Related skills

- [[eng-supabase-edge-functions-patterns]] — Edge Functions must use anon key (not service role) to benefit from RLS
- [[eng-supabase-index-knowledge-pipeline]] — chunk table RLS is critical for RAG safety
- [[eng-pii-redaction-preprocessor]] — data layer safety complements RLS at the application layer
- [[safety-client-confidentiality-cross-tenant]] — policy that mandates this technical control
