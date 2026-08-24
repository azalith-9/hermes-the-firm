---
name: docs-sso-saml-setup
description: Use when an enterprise customer's IT administrator needs to configure Single Sign-On (SSO) for Louis using SAML 2.0 with their identity provider (Okta, Azure AD / Entra ID, Google Workspace, or Auth0). Covers the end-to-end setup flow, attribute mapping, tenant and group provisioning, testing, and rollout. Applicable across all jurisdictions for any Enterprise-tier deployment.
license: MIT
metadata: " id: docs.SSO-SAML-setup category: docs jurisdictions: [__multi__] priority: P2 intent: [SSO, SAML, identity provider, enterprise auth, Okta, Azure AD] related: [docs-security-overview, docs-team-roles-permissions, docs-tenant-isolation-explainer] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Registered as a flat plugin skill.
-->


# SSO / SAML 2.0 Setup Guide

## Prerequisites

- Louis Enterprise tier (SSO is an Enterprise feature; contact sales if on a lower plan).
- Administrative access to your Identity Provider (IdP).
- A domain verified in your Louis organization settings.
- (Optional) Security groups or AD groups that map to Louis roles.

## Overview of the flow

```
User browser → Louis login page
  → Redirect to IdP (with SAML AuthnRequest)
  → IdP authenticates user
  → IdP posts SAML Response (assertion) back to Louis ACS URL
  → Louis validates signature, maps attributes, creates/updates session
  → User lands in Louis
```

## Step 1 — Retrieve Louis service provider (SP) metadata

1. In Louis, go to **Settings → Organization → Security → SSO**.
2. Click **Configure SSO**.
3. Download or copy:
   - **SP Entity ID** (also called Audience URI): `https://app.haqq.ai/saml/metadata`
   - **ACS (Assertion Consumer Service) URL**: `https://app.haqq.ai/saml/acs`
   - **SP Metadata XML** (download and upload directly to your IdP if supported).

## Step 2 — Configure your Identity Provider

### Okta

1. In Okta Admin Console: **Applications → Create App Integration → SAML 2.0**.
2. Set **Single sign-on URL** to the ACS URL above.
3. Set **Audience URI (SP Entity ID)** to the SP Entity ID above.
4. Under **Attribute Statements**, add:
   - `email` → `user.email`
   - `firstName` → `user.firstName`
   - `lastName` → `user.lastName`
   - `groups` → `user.groups` (for role mapping — see Step 4)
5. Download the IdP metadata XML.
6. Assign the application to the relevant Okta groups.

### Azure AD / Microsoft Entra ID

1. In Azure Portal: **Enterprise Applications → New Application → Create your own → Integrate any other application**.
2. Go to **Single sign-on → SAML**.
3. Set **Identifier (Entity ID)** to SP Entity ID; **Reply URL (ACS URL)** to ACS URL.
4. Under **Attributes & Claims**, map:
   - `emailaddress` → `user.mail`
   - `givenname` → `user.givenname`
   - `surname` → `user.surname`
   - `groups` → Group ObjectIDs (or display names if configured)
5. Download **Federation Metadata XML**.
6. Assign users or groups to the application.

### Google Workspace

1. In Google Admin Console: **Apps → Web and mobile apps → Add app → Add custom SAML app**.
2. Download the IdP metadata at step 1 of Google's wizard.
3. Set **ACS URL** and **Entity ID** as above.
4. Under **Attribute mapping**:
   - `email` → Primary email
   - `firstName` → First name
   - `lastName` → Last name
5. Enable the app for the relevant OUs.

### Auth0

1. In Auth0 Dashboard: **Applications → Create Application → Regular Web Application**.
2. Go to **Addons → SAML2 Web App**.
3. Set **Application Callback URL** to ACS URL.
4. In **Settings (JSON)**, set `audience` to SP Entity ID.
5. Map attributes in the settings block:
   ```json
   {
     "mappings": {
       "email": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress",
       "given_name": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname",
       "family_name": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname"
     }
   }
   ```
6. Download IdP metadata or note the IdP SSO URL and certificate.

## Step 3 — Upload IdP metadata to Louis

1. Back in Louis **Settings → SSO**, click **Upload IdP Metadata** and upload the XML file (or paste the metadata URL / individual fields).
2. Fields required if not using metadata XML:
   - IdP Entity ID
   - IdP SSO URL (redirect binding)
   - IdP certificate (PEM format, X.509)

## Step 4 — Map groups to Louis roles

Louis supports automatic role assignment based on SAML group attributes:

| SAML group name (example) | Louis role |
|---|---|
| `louis-admins` | Admin |
| `louis-lawyers` | Lawyer |
| `louis-paralegals` | Paralegal |
| `louis-viewers` | Viewer |
| `louis-billing` | Billing Admin |

Configure the mapping in **Settings → SSO → Role Mapping**. If a user belongs to multiple groups, the highest-privilege role wins. Users with no matched group receive the default role (configurable; default: Viewer).

## Step 5 — Test before rollout

1. Click **Test SSO** in Louis settings — this opens a new browser tab and initiates a SAML flow using a test user account.
2. Verify:
   - Login completes without error.
   - User's name and email are populated correctly.
   - Role is assigned as expected.
3. Check the SAML assertion in the test panel to diagnose attribute-mapping issues.

Common errors:
- `InvalidAudience`: SP Entity ID mismatch — verify copy-paste accuracy, no trailing slash.
- `Signature validation failed`: Certificate expired or wrong cert uploaded.
- `User not provisioned`: User exists in IdP but not assigned to the application.

## Step 6 — Roll out

1. Enable **SSO Enforcement** (optional): forces all users with your domain to authenticate via SSO; password login disabled for those users.
2. Communicate the change to users — they will be redirected to your IdP on next login.
3. Set a **grace period** (recommended 48 hours) during which both SSO and password login are accepted.
4. After grace period, enable enforcement.

## JIT (Just-In-Time) provisioning

Louis supports JIT provisioning: the first time a user authenticates via SSO, an account is automatically created using the SAML attributes. No manual user invitation needed. If SCIM provisioning is required (automated de-provisioning), contact support for SCIM configuration.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Redirect loop | ACS URL misconfigured in IdP | Verify ACS URL exactly |
| Wrong role assigned | Group attribute missing from assertion | Add group attribute in IdP app config |
| Clock skew error | Server time drift > 5 min | Sync NTP on IdP server |
| Certificate error | Expired IdP cert | Re-download and upload fresh cert |

## Related skills

- [[docs-security-overview]]
- [[docs-team-roles-permissions]]
- [[docs-tenant-isolation-explainer]]
