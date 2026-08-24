---
name: connector-figma
description: Use when the legal-AI product design team or a developer needs to read Figma design files, extract Code Connect mappings, or generate UI components from design specs — specifically for building and maintaining the legal-AI product's own front-end. This is an internal engineering/design connector, not a legal-content tool. Triggers on requests to inspect a Figma design, align a React component with a Figma spec, or synchronize Code Connect mappings for the design system.
license: MIT
metadata: " id: connector.figma category: connector jurisdictions: [__multi__] priority: P2 intent: [__connector__] related: [connector-cloudflare, connector-linear, connector-posthog] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'connector'.
Registered as a flat plugin skill.
-->


# Connector — Figma

## What it does

The Figma connector provides read access to Figma design files and Code Connect mappings. Its purpose is to bridge the gap between the product design (what the UI is supposed to look like) and the implemented codebase (what is actually built). In the context of a legal-AI product, this connector is used by:

- **Frontend engineers** generating React/TypeScript components from Figma designs.
- **Designers** verifying that Code Connect mappings correctly link Figma components to their codebase counterparts.
- **Product managers** taking screenshots of Figma frames to attach to Linear issues or feature specs.

This is an **internal team tool** — it operates on the HAQQ/legal-AI product design system, not on clients' legal documents.

## Setup / auth

Authentication uses Figma's OAuth 2.0 flow:

1. An engineer or designer authorizes the connector via "Connect Figma account" in the platform settings.
2. The connector receives a Figma access token scoped to `file_read` and `file_content`.
3. Tokens are stored per-user in the platform's secrets manager.
4. Figma OAuth tokens do not expire by default (they are valid until revoked) but should be rotated annually as a hygiene practice.

For read-only operations (which cover all use cases here), the `file_read` scope is sufficient. Do not request `file_write` unless a write-back feature is explicitly implemented.

## Capabilities

### File reading

- Retrieve the full document structure of a Figma file: frames, components, pages, and layers.
- Extract component properties, layout constraints, and style tokens (colors, typography, spacing).
- Read prototype connections between frames (useful for understanding user flows in the legal-AI UI).

### Design context for code generation

When a developer provides a Figma frame URL or node ID:
- Extract the visual spec: component tree, styles, content.
- Return structured output suitable for generating a React + Tailwind component.
- If Code Connect mappings exist for any component in the frame, return the mapped codebase component identifier instead of generating from scratch.

### Code Connect mappings

Code Connect is Figma's mechanism for linking Figma components to their real codebase implementations. The connector can:
- Read existing Code Connect mappings (`get_code_connect_map`).
- Suggest new mappings where a Figma component exists but no codebase link is present (`get_code_connect_suggestions`).
- Output mappings in the format required by the Figma Code Connect protocol.

### Screenshots

Extract a PNG screenshot of any Figma frame or component for use in:
- Linear issue attachments.
- Documentation.
- Design review sessions in Slack or Notion.

## Usage patterns

### Pattern 1 — New component implementation

```
Developer: "Implement the 'Clause card' component from this Figma frame [URL]"
→ Connector reads the frame's design context
→ Returns component tree, Tailwind classes, and any Code Connect references
→ Developer uses output to implement the React component
→ After implementation, Code Connect mapping is updated to link
```

### Pattern 2 — Design-to-issue workflow

```
Designer: "Capture the mobile intake form spec and attach to Linear DES-42"
→ Connector takes a Figma screenshot of the designated frame
→ Screenshot uploaded to Linear issue DES-42 via [[connector-linear]]
```

### Pattern 3 — Design system audit

Retrieve all Figma components in the design library that lack a Code Connect mapping. Return a list as a Linear project task for the frontend team to address in the next sprint.

## Legal-AI design system considerations

The legal-AI product design system has specific requirements that affect how Figma specs should be read:

- **Bilingual layouts.** Many screens support both LTR (English/French) and RTL (Arabic). Figma frames should be reviewed for RTL mirroring requirements before code generation. If a component is LTR-only in Figma but the product supports Arabic, flag this as a design gap.
- **Accessibility.** Legal documents and forms require high contrast and clear typography. Verify that Figma specs meet WCAG 2.1 AA minimums (4.5:1 contrast ratio for body text).
- **Dense information views.** Legal-AI interfaces often display clause lists, matter timelines, and due-diligence tables. Figma designs for these views tend to be complex; extract with care and verify layer hierarchy before generating code.

## Permissions & safety

- **Read-only.** This connector does not write back to Figma (no creating or modifying frames, components, or styles).
- **Internal use only.** Figma file content belongs to the design team. Do not expose Figma file structures or screenshots to end-user-facing responses.
- **No client document designs.** If a user mistakenly provides a Figma link to a client's document design (e.g., a law firm's branded template), redirect to the appropriate skill and do not retrieve the Figma file without confirming it is a HAQQ internal design file.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| `403 Forbidden` | Figma file is private and token lacks access | Ensure the token belongs to a user with view access to the file |
| Node not found | Node ID in URL is stale (Figma node IDs change on some operations) | Ask user to copy a fresh link from Figma |
| Code Connect suggestion quality poor | Design components have generic names (e.g., "Frame 47") | Prompt design team to name components before mapping |
| Screenshot blank | Frame is off-canvas or hidden | Verify the frame is visible and on the canvas |

## Related skills

- [[connector-cloudflare]]
- [[connector-linear]]
- [[connector-posthog]]
