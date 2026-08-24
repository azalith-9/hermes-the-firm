---
name: site-tools-router
description: Use when rendering or routing to the Louis public tools landing page. Governs the free-tools catalog experience — listing available calculators and tools, enforcing usage limits, surfacing sign-in CTAs for unlimited access, and converting anonymous visitors into registered users. Applies across all jurisdictions and practice areas served by free tools.
license: MIT
metadata: " id: site.tools-router category: site jurisdictions: [__multi__] priority: P3 intent: [__site__] related: [site-use-case-router, tool-date-tool-deadline-calculator, tool-calculator-end-of-service-gratuity, tool-calculator-statutory-interest, tool-calculator-stamp-duty-tax] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'site'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Site — Tools Router

## Purpose

The Tools Router governs the `/tools` landing page and any sub-route under `/tools/:slug`. Its job is threefold:

1. **Catalog** — present all available free tools in a browsable, filterable grid.
2. **Gate** — enforce per-tool usage limits for anonymous / free-tier users and route over-limit requests to sign-in or upgrade flows.
3. **Convert** — turn high-intent tool users into registered accounts through well-placed, non-intrusive CTAs.

## Inputs / signals

| Signal | Source | Used for |
|---|---|---|
| `user.authStatus` | session / cookie | Determine limit tier |
| `user.toolUsageCount[toolSlug]` | usage DB | Enforce free cap |
| `req.params.slug` | URL | Deep-link to specific tool |
| `req.query.intent` | query string | Pre-fill tool with detected intent |
| Practice-area tag | user profile | Personalise catalog sort order |

## Logic

### Catalog rendering

- Pull all tools where `status = "active"` ordered by `priority ASC`, then `category`.
- Group into sections: **Calculators**, **Research**, **Document Tools**, **Court Search**.
- Each card shows: tool name, one-line description, jurisdictions served, and estimated time-to-result.
- Flag tools in beta with a "Preview" badge; hide tools in `status = "disabled"`.

### Usage-limit gate

```
IF user.authStatus == "anonymous":
  allow = toolUsageCount[slug] < ANON_FREE_LIMIT   // e.g. 2 per tool per session
ELIF user.tier == "free":
  allow = toolUsageCount[slug] < FREE_DAILY_LIMIT  // e.g. 10/day across all tools
ELIF user.tier IN ("pro", "firm"):
  allow = true
```

When `allow = false`:
- Display inline paywall overlay (not a hard redirect).
- CTA primary: "Sign up free — 10 uses/day" (anonymous) or "Upgrade to Pro" (free-tier).
- CTA secondary: "Learn more" → `/pricing`.
- Preserve tool state so the user can resume immediately after sign-in.

### Deep-link handling

`/tools/:slug` loads the specific tool page directly. The catalog is collapsed to a sidebar nav. If `slug` is unknown, return a 404 with a suggested similar tool.

### Intent pre-fill

If `?intent=` is present (e.g., from onboarding or a chat referral), auto-populate the tool's primary input field and scroll to the tool form.

## Output

The router emits no JSON — it is a UI routing concern. It should pass to the rendered tool page:

```json
{
  "toolSlug": "string",
  "userTier": "anonymous | free | pro | firm",
  "usageRemaining": "number | unlimited",
  "prefillIntent": "string | null"
}
```

## Conversion best practices

- Show usage remaining as a progress indicator ("7 of 10 free uses today"), not a hard warning — creates urgency without friction.
- After a successful tool run, inject a soft CTA: "Save this result to your matter — sign in free."
- Never gate the tool form itself; let the user reach the result, then gate the export/save action. This maximises perceived value before the ask.
- A/B test CTA copy by user cohort (law student vs solo practitioner vs in-house counsel).

## Why this matters

Free tools are Louis's primary top-of-funnel acquisition channel in the MENA legal market. The EOSG calculator and deadline calculator in particular have direct everyday utility for solo practitioners and in-house teams who may not otherwise trial a full legal AI platform. The tools router must balance discoverability and conversion without creating a hostile experience that drives users away before they see value.

## Related skills

- [[site-use-case-router]]
- [[tool-date-tool-deadline-calculator]]
- [[tool-calculator-end-of-service-gratuity]]
- [[tool-calculator-statutory-interest]]
- [[tool-calculator-stamp-duty-tax]]
