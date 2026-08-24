---
name: wiki-dev-design
description: Use when bridging the gap between design and engineering on a legal-AI product — covering design tokens in code, the Figma-to-code handoff workflow, design reviews with engineers, and maintaining consistency as the product scales. Reach for this skill when the user asks about design token implementation, component handoff, Figma integration, or preventing visual drift between design and production.
license: MIT
metadata: " id: wiki.dev-design category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, design-tokens, figma-to-code, handoff, design-system] related: [wiki-design, wiki-frontend, wiki-engineering, wiki-haqq-product] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Dev-Design Bridge: Tokens, Handoff, and Design Reviews

## Scope

This pack covers the operational process for keeping design and engineering in sync on a legal-AI product: how design tokens flow from Figma into the codebase, the handoff protocol for new components and features, how to run effective design reviews with engineers, and how to catch visual drift before it reaches production.

---

## Why the bridge matters

In legal-tech, visual consistency is a trust signal. A misrendered clause box or a risk badge that changes colour unexpectedly can erode a practitioner's confidence in the tool's accuracy. The design-engineering boundary is where most visual bugs originate. A disciplined bridge process reduces that surface.

---

## Design tokens: the source of truth

Tokens are the contractual interface between design and code. A token changed in Figma should flow into the codebase through a defined process — never by a developer overriding a CSS value manually.

### Token hierarchy

```
Figma Variables (primitives)
        │   export via Style Dictionary / Figma Tokens plugin
        ▼
tokens/primitives.json   (raw values: colors, spacing, radii, etc.)
tokens/semantic.json     (roles: text-primary, surface-danger, etc.)
tokens/components.json   (scoped: button-bg, input-border, etc.)
        │
        ▼
Tailwind config / CSS custom properties
        │
        ▼
Component code (uses Tailwind classes or CSS vars — never hardcoded hex)
```

### Tooling options

| Tool | When to use |
|---|---|
| **Style Dictionary** (Amazon) | Large teams; tokens-as-code with multi-target output (CSS, JS, iOS, Android) |
| **Figma Tokens plugin** (now Tokens Studio) | Smaller teams; Figma-first; exports JSON that feeds Style Dictionary |
| **Tailwind `theme.extend`** | Minimal setup; sufficient for products with < 200 tokens |
| **CSS custom properties** | Framework-agnostic; required if server-side rendering uses non-Tailwind CSS |

For a Next.js / Tailwind product (see [[wiki-frontend]]), the recommended approach is: Tokens Studio in Figma → JSON export → Style Dictionary → `tailwind.config.ts` `theme.extend.colors` / `spacing` / etc.

---

## Figma-to-code handoff protocol

### Step 1: Design complete gate

Before a design enters the handoff queue it must pass:

- [ ] All colours reference Figma variables (no hardcoded hex in frames)
- [ ] All spacing uses the 4 px grid
- [ ] Component instances reference the Figma component library (not one-off frames)
- [ ] RTL/Arabic variant exists if the feature surfaces user-facing text
- [ ] Accessibility contrast check passed
- [ ] Edge cases documented (empty state, error state, loading state, truncated text)

### Step 2: Handoff annotation

Add a "Dev notes" section to the Figma frame before sharing:
- Which existing component(s) to use (or: "new component required")
- Responsive behaviour (stack on mobile / hide on < 768 px / etc.)
- Any animation or transition spec
- Which tokens are used by name (e.g. `--color-surface-warning`)
- Data shape expected (e.g. "risk badge takes `severity: 'high' | 'medium' | 'low'`")

### Step 3: Engineering ticket

The design handoff creates (or links to) a Linear/GitHub issue that includes:
- Link to the Figma frame (with node ID for direct navigation)
- Token list from the annotation
- Acceptance criteria: "Matches Figma frame in light mode, dark mode, and RTL mode"
- Link to the component in the design system if it exists

### Step 4: Implementation

Engineers build against tokens and the component library. No new CSS custom properties or hardcoded values without a corresponding token definition. If a token is missing, create it in `tokens/semantic.json` first — do not hardcode.

### Step 5: Design review in code

Before merging:
1. Open the implemented feature in Storybook (or the dev preview URL)
2. Designer does a side-by-side comparison with the Figma frame
3. Check in light mode, dark mode, and RTL locale
4. Flag issues as "blocking" (must fix before merge) or "polish" (can be a follow-up ticket)

---

## Running effective design reviews

### Format

- Timebox to 30 minutes
- Share screen: Figma frame on the left, running implementation on the right
- Reviewer (designer) calls out discrepancies; engineer notes them
- Decision: fix now vs create a polish ticket vs intentional deviation (document why)

### What to check

| Area | What to look for |
|---|---|
| Spacing | Does padding match the spec? Are gutters consistent? |
| Typography | Font size, weight, line height, letter spacing matching tokens? |
| Colour | Are token values rendering correctly in both themes? |
| Component state | Hover, focus, disabled, loading, error states all present and correct? |
| Responsiveness | Does it stack/hide correctly at 375 px and 768 px breakpoints? |
| RTL | Does the layout mirror correctly? Icons flip? Text alignment right? |
| Accessibility | Focusable? Contrast passes? Screen reader label present? |

---

## Preventing visual drift

Visual drift happens when developers add one-off CSS, when tokens are duplicated under different names, or when Figma diverges from the exported JSON because someone forgot to run the export.

Prevention mechanisms:
- **Automated token sync** — CI job that runs Style Dictionary export and fails if the generated output differs from what is committed (i.e. Figma was updated but the JSON was not exported)
- **Visual regression testing** — Chromatic (or Percy) on Storybook; every component story is baselined and diffs alert on PR
- **Token audit (quarterly)** — grep the codebase for hardcoded hex values (`#[0-9a-fA-F]{3,6}`); any found must be replaced with a token reference before release

---

## Caveats & currency

Design tool ecosystems move quickly. Figma's variable API and the Tokens Studio plugin change with Figma releases; verify export formats after Figma updates. Style Dictionary v3 has a significantly different API from v2; confirm which version your project uses before following tutorials. RTL support in CSS grid and flexbox is now largely handled by logical properties (`margin-inline-start` instead of `margin-left`) — prefer logical properties for all new layout code to avoid RTL-specific overrides.

---

## Related skills

- [[wiki-design]]
- [[wiki-frontend]]
- [[wiki-engineering]]
- [[wiki-haqq-product]]
