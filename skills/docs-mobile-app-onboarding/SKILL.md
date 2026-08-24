---
name: docs-mobile-app-onboarding
description: Use when a user asks how to install, set up, or use the mobile app — iOS or Android. This is a platform documentation skill covering the mobile app installation flow, sign-in, first task, push notification configuration, biometric unlock, WhatsApp document sharing, and the differences between mobile and web feature availability.
license: MIT
metadata: " id: docs.mobile-app-onboarding category: docs jurisdictions: [__multi__] priority: P2 intent: [__docs__, mobile app, ios, android, onboarding, whatsapp, biometric] related: [docs-legal-ai-workspace-guide, docs-faq-pack, docs-enterprise-deployment] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'docs'.
Registered as a flat plugin skill.
-->


# Mobile App Onboarding

## What the mobile app does

The mobile app brings core legal AI workspace capabilities to iOS and Android devices. It is optimized for:

- **On-the-go drafting and review**: start an NDA, review a contract, or run a quick legal research query from a phone or tablet.
- **Matter access**: check matter status, review documents, and respond to colleague comments.
- **Push notifications**: be notified when a document is shared with you, a deadline approaches, or a colleague tags you in a matter.
- **WhatsApp sharing**: the most common document distribution channel in MENA practice — send a drafted document directly from the app via WhatsApp, with a secure link or as a PDF attachment.
- **Biometric authentication**: Face ID (iOS) or fingerprint (Android) for fast, secure re-entry.

## Installation

### iOS (iPhone / iPad)

1. Open the **App Store**.
2. Search for **[Platform name]** or follow the universal link from the web app: **Settings → Mobile → Get the App → iOS**.
3. Tap **Get** → **Install**. Face ID or Touch ID required for App Store purchase authorization.
4. After installation, tap **Open** or find the app icon on the home screen.

Minimum iOS version: iOS 16. Optimized for iOS 17+. Compatible with iPhone 12 and later; iPad (all models, iPadOS 16+).

### Android

1. Open **Google Play Store**.
2. Search for **[Platform name]** or follow the universal link from the web app: **Settings → Mobile → Get the App → Android**.
3. Tap **Install**.

Minimum Android version: Android 12. Compatible with most Android devices released in 2021 or later.

## First-time sign-in

1. Open the app. Tap **Sign In**.
2. Enter your email address and tap **Continue**.
3. If SSO is enabled on your workspace: tap **Continue with SSO** and authenticate via your organization's IdP (Okta, Azure AD, Google Workspace, etc.).
4. If password sign-in: enter password, complete MFA if enabled.
5. On first sign-in, you will be prompted to enable **Biometric Unlock** (recommended) and **Push Notifications** (recommended for deadline and collaboration alerts).

If your workspace requires SSO and you do not see the SSO button: contact your workspace administrator — your email domain must be configured for SSO in the workspace settings before it appears in the mobile app.

## First task

The onboarding tutorial prompts you to complete your first task:

1. **Try the AI assistant**: tap the chat icon and type a legal question or a drafting request.
2. **Open a matter**: tap **Matters** to see existing matters (if any) or create a new one.
3. **Review a document**: tap **Documents → Upload** to upload a PDF and invoke the risk review skill.

The onboarding checklist tracks completion and unlocks a usage credit bonus on first completion (verify current offer in the app).

## Push notifications

Enable push notifications to receive:

- **Deadline reminders**: configurable lead time (7, 14, 30 days before deadline).
- **Document shared**: when a colleague shares a document with you or sends you a draft for review.
- **Matter updates**: when a new document, comment, or status change is recorded on a matter you own or follow.
- **Billing alerts**: credit balance low, subscription renewal approaching.
- **Security alerts**: new device login detected, suspicious activity flag.

Configure push notification preferences at **App Settings → Notifications** or in **Settings → Notifications** on the web app (synced to mobile).

## Biometric unlock

After the initial SSO or password sign-in, enable biometric unlock for subsequent app openings:

- **iOS**: Face ID or Touch ID.
- **Android**: fingerprint or face unlock (Android 12+ secure biometric).

Biometric unlock re-authenticates the existing session. It does not replace SSO — if the session expires (default: 8 hours), full authentication is required.

Enterprise workspaces can require biometric unlock via the MDM (Mobile Device Management) policy.

## WhatsApp sharing

WhatsApp is the dominant professional messaging platform in MENA markets. The mobile app integrates with WhatsApp for document distribution:

1. Open a drafted or reviewed document.
2. Tap **Share → WhatsApp**.
3. Choose: **Secure Link** (recipient opens in the platform via a time-limited authenticated link) or **PDF Attachment** (sends the PDF directly in the WhatsApp message).
4. Recipient opens and signs in if required (for Secure Link) or downloads the PDF (for attachment).

Note: PDF attachment sharing sends the document outside the platform's security perimeter. Use Secure Link where client data sensitivity requires access control. The workspace administrator can restrict PDF attachment sharing via **Settings → Sharing Policy**.

## Universal links

Universal links allow navigation directly from the web app to the mobile app on the same device:

- Clicking a matter link or document link on mobile web opens the native app automatically (if installed).
- Deep links from email notifications or WhatsApp messages open the specific matter or document directly in the app.

Configure universal link handling in iOS **Settings → [Platform name] → Default Browser Behavior** or Android app link settings.

## Mobile vs web feature availability

| Feature | Mobile | Web |
|---|---|---|
| Chat / AI assistant | Full | Full |
| Document drafting | Full | Full |
| Document review (upload) | Upload only; review starts on mobile, results in full editor on web | Full |
| Multi-document compare | View only; initiate on web | Full |
| Matter management | Full | Full |
| Flows / workflow automation | View/approve steps | Full configuration |
| Developer API configuration | View only | Full |
| Audit log export | View only | Full |
| Billing / subscription management | View only | Full |
| Biometric unlock | Yes | N/A |
| WhatsApp sharing | Yes | No (web uses native share) |

## Related skills

- [[docs-legal-ai-workspace-guide]]
- [[docs-faq-pack]]
- [[docs-enterprise-deployment]]
