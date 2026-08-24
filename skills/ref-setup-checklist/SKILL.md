---
name: ref-setup-checklist
description: Use as a reference checklist when setting up Louis (or a comparable legal AI platform) for a new law firm or legal department tenant — covering tenant creation, DPA signing, AML compliance overview, conflict-check seed data, firm knowledge base ingestion, branded engagement letter templates, user onboarding for partners and associates, firm preference customization, and integration setup. Consult when onboarding a new firm or auditing an existing deployment's configuration.
license: MIT
metadata: " id: ref.setup-checklist category: ref priority: P1 intent: [__ref__, setup, onboarding, deployment, firm-configuration] related: - ref-mcp-hardening - ref-privilege-layers - ref-skill-authoring - ref-anti-patterns source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'ref'.
Registered as a flat plugin skill.
-->


# Reference — Setup Checklist for New Firm Deployments

## Scope

This checklist covers the steps required to deploy Louis for a new law firm or in-house legal department tenant. Complete each item in the order listed; earlier items are dependencies for later ones.

Use this checklist:
- When a new firm signs up and the implementation team is configuring the deployment
- When auditing an existing deployment to confirm all configuration steps were completed
- When a firm changes ownership, merges, or significantly expands and a re-configuration is required

---

## Phase 1 — Legal and Compliance Prerequisites

These items must be completed before any data is loaded or users are onboarded.

### 1.1 Tenant creation in Supabase / backend

- [ ] Create the tenant namespace in Supabase with a unique tenant ID
- [ ] Confirm data residency: which region should the tenant's data be stored in? (relevant for UAE, KSA, and EU clients with data residency requirements)
- [ ] Set tenant-level configuration: firm name, primary jurisdiction(s), practice areas, preferred language (English / Arabic / bilingual)
- [ ] Configure access control: firm admin designated; admin permissions set

### 1.2 Data Processing Agreement (DPA)

- [ ] The firm has signed and returned the DPA before any personal data is uploaded to the platform
- [ ] DPA filed in the firm's contract record and in the platform's contract management system
- [ ] DPA covers the applicable data protection law(s) for the firm's jurisdiction(s) (GDPR, UAE PDPL, KSA PDPL, DIFC DP Law, etc.)
- [ ] Confirm whether any special-category data (health, financial, children's data) will be processed — if so, confirm the DPA covers this and appropriate safeguards are in place

### 1.3 AML compliance overview

- [ ] The firm has received and acknowledged the platform's AML compliance overview document
- [ ] The firm confirms it has its own AML / KYC obligations as a law firm and that using Louis does not substitute for the firm's independent compliance obligations
- [ ] If the firm uses Louis for AML / KYC screening tools, confirm those tool integrations are configured per the relevant regulatory framework (FATF, UAE AML Law, KSA AML Law)
- [ ] MLRO / compliance contact at the firm identified in the platform configuration

---

## Phase 2 — Firm Knowledge Base

The firm KB is what differentiates the platform from a generic AI — it contains the firm's precedents, templates, and practice-specific knowledge.

### 2.1 Conflict-check seed data

- [ ] Firm provides a list of current and recent clients (name, matter type, counterparty where applicable) for the conflict-check module
- [ ] Conflict-check database is seeded and tested: run 5 test queries to confirm positive and negative results
- [ ] Conflict-check permissions: confirm who can run conflict checks (all fee earners? admin only?) and who can see results

### 2.2 Firm precedents and templates

- [ ] Inventory of firm precedent documents provided (contract templates, court form letters, standard NDAs, engagement letters, etc.)
- [ ] Documents ingested into the firm KB with appropriate metadata (document type, jurisdiction, practice area, date of last review)
- [ ] Knowledge base search tested: confirm that a relevant query returns firm precedents ahead of generic AI-generated templates
- [ ] Document confidentiality: confirm that KB documents are scoped to the tenant and cannot be accessed cross-tenant

### 2.3 Branded engagement letter template

- [ ] Firm provides its standard engagement letter template (or requests Louis to generate one)
- [ ] Template configured with firm name, logo placeholder, partner/associate signature blocks, and firm-specific terms of engagement
- [ ] Tested: generate a sample engagement letter to confirm branding and content are correct

---

## Phase 3 — User Onboarding

### 3.1 Partners and senior fee earners

- [ ] Partner accounts created with appropriate permission level (can configure firm KB, can view all matters, can approve AI-generated outputs for client-facing use)
- [ ] Each partner receives: platform walkthrough (30–45 minutes); overview of AI vs. lawyer roles; anti-patterns briefing (see [[ref-anti-patterns]]); privilege risk briefing (see [[ref-privilege-layers]])
- [ ] Partners acknowledge the firm's AI use policy (a firm policy document that defines permitted and prohibited uses of the platform)

### 3.2 Associates and paralegals

- [ ] Associate / paralegal accounts created with standard permission level (cannot modify firm KB; outputs require partner review before client delivery)
- [ ] Training session: how to use prompt skills effectively; jurisdiction-first approach; when to escalate to a partner
- [ ] Acknowledgment of AI use policy

### 3.3 Admin / IT users

- [ ] Admin account(s) for IT / operations with configuration access but no matter access
- [ ] Admin responsibilities defined: user provisioning / deprovisioning; integration health monitoring; audit log review

---

## Phase 4 — Platform Customization

### 4.1 Firm preferences

- [ ] Default jurisdiction(s) configured (so that queries default to the firm's primary jurisdiction without requiring explicit instruction every time)
- [ ] Preferred language: English / Arabic / bilingual default
- [ ] Output format preferences (e.g., DOCX default, header/footer with firm branding on generated documents)
- [ ] Tone: formal / semi-formal for all AI outputs
- [ ] Disclaimer language: firm-specific non-legal-advice disclaimer configured for all client-facing outputs

### 4.2 Practice area skills activation

- [ ] Enable / disable skills by practice area based on the firm's actual practice areas; disable skills for areas the firm does not practice (reduces router noise)
- [ ] Configure jurisdiction-specific skills to match the firm's jurisdictional footprint

---

## Phase 5 — Integration Setup

### 5.1 Linear (project management / matter tracking)

- [ ] Linear workspace connected with the firm's tenant ID
- [ ] Matter IDs in Linear map to matter IDs in Louis for cross-linking
- [ ] Permissions scoped: Louis can read matter status; cannot write to Linear without approval

### 5.2 HubSpot (CRM / client management)

- [ ] HubSpot connected for conflict-check enrichment (new client intake pulls HubSpot contact data)
- [ ] Scope: read-only CRM access; no write permissions
- [ ] GDPR / DPA: confirm that HubSpot CRM data shared with Louis is covered by the DPA and the firm's client data sharing consent

### 5.3 Stripe / billing (if applicable)

- [ ] If the firm uses Louis's billing integration: Stripe connected; billing entries from Louis time-tracking linked to the firm's billing system
- [ ] Scope: create billing entries for confirmed work; read billing history; no payment execution

### 5.4 Document management (NetDocuments / iManage / SharePoint)

- [ ] If the firm uses a DMS: DMS integration configured with matter-scoped access
- [ ] Test: save a Louis-generated document to the DMS; confirm it appears in the correct matter folder
- [ ] Permissions: Louis can save documents to authorized matters; cannot access documents from other matters

---

## Phase 6 — Go-Live Validation

- [ ] Run an end-to-end test with a fictional matter: conflict check → engagement letter → substantive skill output → document save to DMS
- [ ] Confirm all outputs are watermarked / branded correctly
- [ ] Confirm audit log captures all test actions
- [ ] Confirm tenant isolation: create a second test tenant and confirm it cannot access the first tenant's data
- [ ] Escalation contact confirmed: who at the platform does the firm contact for a security incident or critical bug?

---

## Related skills

- [[ref-mcp-hardening]]
- [[ref-privilege-layers]]
- [[ref-anti-patterns]]
- [[ref-skill-authoring]]
