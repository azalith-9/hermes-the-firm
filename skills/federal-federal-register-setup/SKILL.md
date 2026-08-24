---
name: federal-federal-register-setup
description: >-
  Wire the federal-register MCP server into Hermes for federal register. Use when setting up this firm's federal research connectors or when a question needs live federal data the local corpus lacks.
---

<!--
HERMES PORT NOTE
Generated for hermes-the-firm from beshkenadze/us-legal-tools (MIT).
Wiring commands come from that project's own READMEs; verify against
the upstream repo if a package version changes.
-->

# Federal connector: federal-register

Federal Register — proposed rules, final rules, notices and presidential documents as they publish.

Source: [beshkenadze/us-legal-tools](https://github.com/beshkenadze/us-legal-tools)
(MIT), `@us-legal-tools/federal-register-sdk/mcp`.
## Wire it into Hermes

`hermes mcp add federal-register` with command `npx` and args `['@us-legal-tools', 'federal-register-sdk', 'mcp']`

Equivalent Claude-style JSON (for reference):

```json
{
  "mcpServers": {
    "federal-register": {
      "command": "npx",
      "args": [
        "@us-legal-tools/federal-register-sdk/mcp"
      ]
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
