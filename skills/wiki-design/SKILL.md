---
name: wiki-design
description: Use when discussing product design principles, UI/UX decisions, or design system architecture for a legal-AI product. Covers comfort-first design philosophy, glanceable interfaces, progressive disclosure, design tokens, accessibility, and the specific considerations of designing for legal professionals under cognitive load. Reach for this skill when the user asks about design principles, design systems, component libraries, or UI strategy.
license: MIT
metadata: " id: wiki.design category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, product-design, ux, design-system, accessibility] related: [wiki-dev-design, wiki-frontend, wiki-haqq-product, wiki-engineering] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Registered as a flat plugin skill.
-->


# Product Design Principles for Legal-AI

## Scope

This pack covers the design philosophy and practical system for a legal-AI product: comfort-first principles, glanceable UI patterns, progressive disclosure, design tokens, component architecture, accessibility requirements, and the particular UX considerations of serving legal professionals who are often time-pressured, detail-oriented, and using the product in high-stakes contexts.

---

## Core design philosophy

### Comfort-first

Legal professionals use their tools under persistent cognitive load — a partner reviewing a 200-page transaction document is already mentally taxed before they open the AI assistant. The product's job is to reduce friction, not add it.

Comfort-first means:
- **Low visual noise** — neutral palette, generous whitespace, no blinking elements or unsolicited animations
- **Predictable layout** — primary actions always in the same position; no UI shuffling between sessions
- **Calm defaults** — dark mode available by default; font size adjustable; no pop-ups unless critical
- **Forgiving interactions** — destructive actions require confirmation; drafts auto-save; state persists across sessions

### Glanceable UI

The practitioner checks the AI's output with peripheral attention before diving in. Design for scanning:
- Consistent heading hierarchy (H1 → document title, H2 → major section, H3 → sub-clause)
- Colour-coded risk indicators visible without reading the full text (red = flag, amber = review, green = acceptable)
- Summary box at top of every AI output — the practitioner can read the conclusion first and expand detail on demand

### Progressive disclosure

Surface only what is needed for the current task. The assistant should not present 12 options when the user needs one document. Use:
- **Primary action** — one clear CTA per screen state
- **Secondary actions** — collapsed in "More options" or a context menu
- **Advanced settings** — behind a "Settings" or "⚙" toggle, never in the primary flow
- **Jurisdiction / language options** — offered once during onboarding, persisted, surfaceable via a small pill on the output (not a full form every time)

---

## Design system

### Design tokens

Tokens are the single source of truth for visual style. Organize as a three-layer hierarchy:

```
Primitive tokens (raw values)
  → Semantic tokens (named by role)
    → Component tokens (scoped to a component)
```

Example:
```
--color-neutral-900: #111827         (primitive)
--color-text-primary: var(--color-neutral-900)  (semantic)
--input-label-color: var(--color-text-primary)  (component)
```

Primitives live in the design tool (Figma variables); semantic and component tokens live in the codebase (`tokens.css` or a JS/TS token file imported by Tailwind config). See [[wiki-dev-design]] for the Figma → code bridge process.

### Colour

- Primary action: a single brand colour used consistently for buttons, links, active states
- Semantic colours: success (green), warning (amber), danger (red), info (blue) — use sparingly; overuse desensitises
- Neutral scale: at minimum 50/100/200/400/600/800/900
- Dark mode: every semantic colour must have a dark-mode counterpart tested for WCAG AA contrast

### Typography

- One typeface family is almost always right; two at most
- Body: 15–16 px minimum for sustained reading; legal documents at 14 px minimum
- Code / clause display: monospace for extracted contract clauses helps practitioners scan
- RTL support: if the product serves Arabic users (KSA, UAE, LB, EG), the type system must support Arabic script. Use a typeface with verified Arabic glyphs (e.g. IBM Plex Arabic, Noto Sans Arabic). All spacing and layout must mirror horizontally in RTL mode.

### Spacing

Use a 4 px base grid. Common spacing values: 4, 8, 12, 16, 24, 32, 48, 64. Never use arbitrary pixel values — every spacing decision should trace to the grid.

### Component library

Build on top of Shadcn UI (see [[wiki-frontend]]) and override tokens rather than forking components. Key components for a legal-AI product:

| Component | Legal-AI specific notes |
|---|---|
| `DocumentViewer` | Side-by-side original + AI output; clause-level annotations |
| `RiskBadge` | Colour-coded severity indicator; must work in both light/dark and be accessible |
| `JurisdictionPill` | Small pill showing active jurisdiction (e.g. "UAE" or "DIFC"); tappable to change |
| `SkillOutput` | Structured AI response container with summary box + expandable detail |
| `AuditTrail` | Chronological log of AI actions on a matter; append-only display |
| `LanguageToggle` | AR/EN switch; persisted per user; triggers RTL/LTR layout flip |

---

## Accessibility

Minimum standard: **WCAG 2.1 Level AA**. For a product used by professionals in regulated contexts, accessibility is a commercial requirement, not a nice-to-have (procurement teams in large firms check for it).

Key requirements:
- Colour contrast ratio ≥ 4.5:1 for normal text, ≥ 3:1 for large text
- All interactive elements focusable and operable by keyboard
- Screen reader labels on all icons and non-text elements (`aria-label`, `aria-describedby`)
- Focus indicators visible (do not suppress default browser outline without replacement)
- Dynamic content changes announced to screen readers via `aria-live`
- RTL layout fully functional when Arabic locale is active

### Testing checklist

- [ ] axe DevTools or Lighthouse accessibility audit (target 0 critical violations)
- [ ] Keyboard-only navigation walkthrough of core flows
- [ ] Screen reader test (VoiceOver on macOS + NVDA on Windows)
- [ ] Contrast check for all colour combinations in both light and dark mode
- [ ] RTL layout test with Arabic locale set

---

## Design process

### Discovery

- User interviews with practicing lawyers (not just PMs imagining users)
- Shadowing sessions: observe how a practitioner actually uses the current tool in a live matter
- Quantitative: funnel analysis on onboarding, feature adoption (see [[wiki-data]])

### Design reviews

- Hold a structured design review before any feature enters development
- Review criteria: comfort-first checklist, accessibility, consistency with design system, bilingual compatibility
- Record decisions in a shared design decision log (Notion, Linear, or a `design-decisions/` folder in the repo)

### Handoff

See [[wiki-dev-design]] for the full Figma → code handoff process. Key principle: the component should already exist in the library; if it doesn't, build the token and component in the design system first, then use it in the feature.

---

## Caveats & currency

Design systems require ongoing maintenance. Tokens drift when developers add one-off overrides. Schedule a quarterly token audit. Accessibility standards may be updated; verify against the WCAG working group's current recommendation. RTL/Arabic support is particularly prone to regression when new components are added — include RTL in CI visual regression testing.

---

## Related skills

- [[wiki-dev-design]]
- [[wiki-frontend]]
- [[wiki-haqq-product]]
- [[wiki-engineering]]
