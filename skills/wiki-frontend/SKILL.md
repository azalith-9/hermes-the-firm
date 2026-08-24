---
name: wiki-frontend
description: Use when making technical decisions about the frontend stack for a legal-AI product, or when debugging or extending the existing Next.js / Tailwind / Shadcn UI / React architecture. Covers the chosen stack rationale, Server Components, RSC streaming, component patterns, RTL support, and performance considerations specific to a document-heavy legal interface. Reach for this skill when the user asks about frontend technology choices, Next.js patterns, React 19 features, or UI component decisions.
license: MIT
metadata: " id: wiki.frontend category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, frontend, nextjs, tailwind, react, server-components] related: [wiki-dev-design, wiki-design, wiki-engineering, wiki-haqq-product] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Frontend Stack: Next.js, Tailwind, Shadcn UI, React 19

## Scope

This pack documents the chosen frontend stack for the legal-AI product, the reasoning behind each choice, and the key patterns and constraints to follow when building and extending the UI. It assumes a Next.js App Router project using Tailwind CSS, Shadcn UI components, React 19, and Server Components with streaming.

---

## Stack overview

| Layer | Technology | Version target |
|---|---|---|
| Framework | Next.js (App Router) | 14 / 15 |
| UI library | React | 19 |
| Styling | Tailwind CSS | 3.x |
| Component base | Shadcn UI | latest (copy-based) |
| Language | TypeScript | 5.x |
| State management | React Server Components + minimal Zustand/Jotai for client state | — |
| Auth | NextAuth.js v5 or Supabase Auth | — |
| Data fetching | Server Actions + `fetch` in Server Components | — |

---

## Why this stack for legal-AI

### Next.js App Router

The App Router (introduced in Next.js 13) enables the React Server Components model, which is the right architectural choice for a document-heavy legal product:
- Server Components render on the server — the bulk of a legal document view (clause display, risk annotations) can be rendered as HTML, reducing JS bundle size and time-to-interactive.
- Streaming allows progressive rendering: the shell (header, navigation) renders immediately; heavy content (document analysis, AI output) streams in as it becomes available. This is critical for LLM-generated responses where latency can be 3–10 seconds.
- Layouts persist across navigation without re-rendering — important for an assistant panel that stays open while the user navigates between matters.

### Tailwind CSS

- Utility-first CSS eliminates the naming problem and style collision risk in large component trees.
- Pairs cleanly with design tokens via `tailwind.config.ts` `theme.extend` (see [[wiki-dev-design]]).
- RTL support: Tailwind v3+ supports logical-property variants (`ms-` for `margin-inline-start`, etc.) which simplify RTL implementation.
- Dark mode: class-based dark mode (`dark:`) is easy to control from a user preference stored in a cookie.

### Shadcn UI

Shadcn UI is not a traditional component library — it is a collection of copy-paste components built on Radix UI primitives and styled with Tailwind. This is the right choice for a legal-AI product because:
- Components are owned by the codebase, not a package. Custom behaviour (jurisdiction pill in a select, risk badge in a card) can be added directly without fighting a library's abstraction.
- Radix UI primitives provide accessibility (keyboard navigation, screen reader support, focus management) for free.
- Consistent with the design token approach (see [[wiki-design]]): override via CSS custom properties, not by forking.

---

## React 19 patterns

### Server Components (RSC)

- Default to Server Components for anything that does not need interactivity or browser APIs.
- Server Components can be `async` — fetch data directly with `await`, no useEffect/useState boilerplate.
- Never import a heavy client library (charting, rich text editor) into a Server Component; it will be bundled but cannot run on the server. Mark the file with `"use client"` or lazy-import.

```tsx
// Good: Server Component fetches document list
export default async function MatterPage({ params }: { params: { matterId: string } }) {
  const docs = await fetchDocuments(params.matterId) // runs on server
  return <DocumentList documents={docs} />
}
```

### Client Components

Mark with `"use client"` only when needed:
- Event handlers (onClick, onChange)
- Browser APIs (localStorage, window, navigator)
- React hooks that depend on client-side state (useState, useEffect, useRef)
- Real-time subscriptions (WebSocket, Supabase Realtime)

**Key pattern**: push `"use client"` as far down the tree as possible. A page can be a Server Component with one small interactive island (`"use client"`) inside it.

### Streaming and Suspense

```tsx
import { Suspense } from 'react'

export default function SkillOutputPage() {
  return (
    <>
      <Header />  {/* renders immediately */}
      <Suspense fallback={<SkillOutputSkeleton />}>
        <SkillOutput />  {/* streams in when LLM response completes */}
      </Suspense>
    </>
  )
}
```

Use skeletons that match the final content layout to avoid layout shift.

### Server Actions

Use Server Actions for form submissions and mutations instead of API routes where possible:
```tsx
async function saveDocument(formData: FormData) {
  'use server'
  // runs on server; validates, writes to DB
}
```

For complex mutations with optimistic UI, combine Server Actions with `useOptimistic`.

---

## RTL and Arabic support

The legal-AI product serves Arabic-speaking users (UAE, KSA, Lebanon, Egypt). RTL support is a first-class requirement, not an afterthought.

### Implementation

1. Set `dir="rtl"` on `<html>` when Arabic locale is active. Next.js i18n middleware can set this per-request based on `Accept-Language` or user preference.
2. Use Tailwind logical-property classes everywhere: `ms-` not `ml-`, `ps-` not `pl-`, `start-` not `left-`.
3. Icons that convey direction (arrows, chevrons, "back" buttons) must flip in RTL. Use a wrapper that applies `transform: scaleX(-1)` in RTL.
4. Shadcn UI components built on Radix are RTL-aware if `dir="rtl"` is set on a parent — verify this for each component used.

### Testing

- Run Playwright tests with `dir="rtl"` in the browser context.
- Include RTL screenshots in visual regression baseline (Chromatic).
- Check: text alignment, spacing mirroring, icon direction, form field layout, modal positioning.

---

## Performance considerations for legal-UI

Legal documents are large; AI outputs can be long. Performance strategies:

- **Virtualize long lists** — a document with 500 clauses should render only the visible ones. Use `@tanstack/react-virtual`.
- **Lazy-load the PDF viewer** — PDF.js is large (~1 MB); load dynamically with `next/dynamic` and a loading placeholder.
- **Split AI output streaming** — stream the AI response token by token rather than waiting for the full completion. Use the AI SDK's `useStreamableValue` or a custom SSE endpoint.
- **Image optimization** — use `next/image` for all images; it handles format conversion and lazy loading.
- **Font subset for Arabic** — the full Noto Sans Arabic font family is large; subset to the Unicode blocks actually used.

---

## File and folder conventions

```
app/
  (auth)/           -- unauthenticated routes
  (dashboard)/      -- authenticated routes; shared layout
    matters/
      [matterId]/
        page.tsx    -- Server Component
        client.tsx  -- "use client" interactive parts
components/
  ui/               -- Shadcn copies (never edit directly; override via tokens)
  legal/            -- legal-specific components (DocumentViewer, RiskBadge, etc.)
  layout/           -- Header, Sidebar, Shell
lib/
  db.ts             -- Supabase / Prisma client
  actions/          -- Server Actions
  ai/               -- AI SDK wrappers, skill invocation
styles/
  globals.css       -- CSS custom properties (tokens)
  rtl.css           -- RTL overrides if any cannot be handled by logical properties
```

---

## Caveats & currency

Next.js releases frequently; the App Router has evolved significantly since its introduction. Check the Next.js changelog before upgrading. React 19 concurrent features are stable but some third-party libraries still have peer-dependency issues with React 18 API; verify before adding new packages. Tailwind v4 (alpha as of early 2026) changes the CSS-first configuration model significantly — do not migrate until a stable release and ecosystem readiness.

---

## Related skills

- [[wiki-dev-design]]
- [[wiki-design]]
- [[wiki-engineering]]
- [[wiki-haqq-product]]
