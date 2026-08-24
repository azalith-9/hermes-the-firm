---
name: federal-courtlistener-setup
description: >-
  Wire the courtlistener MCP server into Hermes for courtlistener. Use when setting up this firm's federal research connectors or when a question needs live federal data the local corpus lacks.
---

<!--
HERMES PORT NOTE
Generated for hermes-the-firm from beshkenadze/us-legal-tools (MIT).
Wiring commands come from that project's own READMEs; verify against
the upstream repo if a package version changes.
-->

# Federal connector: courtlistener

CourtListener — US case law, dockets, and citations (the case-law layer the local corpus does NOT carry).

Source: [beshkenadze/us-legal-tools](https://github.com/beshkenadze/us-legal-tools)
(MIT), `@us-legal-tools/courtlistener-sdk/mcp`.
**Credentials:** free token at courtlistener.com → account → API; optional but rate-limited without it.

## Wire it into Hermes

`hermes mcp add courtlistener` with command `npx` and args `['@us-legal-tools', 'courtlistener-sdk', 'mcp']` COURTLISTENER_API_TOKEN=<your-token>

Equivalent Claude-style JSON (for reference):

```json
{
  "mcpServers": {
    "courtlistener": {
      "command": "npx",
      "args": [
        "@us-legal-tools/courtlistener-sdk/mcp"
      ],
      "env": {
        "COURTLISTENER_API_TOKEN": "<your-token>"
      }
    }
  }
}
```


After adding, restart the session or run `hermes gateway restart`, then
confirm with `hermes mcp list`. Probe one real call before trusting the
connector — configured is not connected.

## What this buys the firm

Live federal data on top of the local open-us-law corpus: eCFR covers the
regulations layer the corpus is thin on, CourtListener covers case law
(which the corpus does not carry at all), Federal Register covers
rulemaking as it happens, govinfo covers official document sets.
