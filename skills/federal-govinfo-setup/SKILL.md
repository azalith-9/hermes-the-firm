---
name: federal-govinfo-setup
description: >-
  Wire the govinfo MCP server into Hermes for govinfo. Use when setting up this firm's federal research connectors or when a question needs live federal data the local corpus lacks.
---

<!--
HERMES PORT NOTE
Generated for hermes-the-firm from beshkenadze/us-legal-tools (MIT).
Wiring commands come from that project's own READMEs; verify against
the upstream repo if a package version changes.
-->

# Federal connector: govinfo

govinfo — official primary documents: US Code, Statutes at Large, CFR, Federal Register, congressional material.

Source: [beshkenadze/us-legal-tools](https://github.com/beshkenadze/us-legal-tools)
(MIT), `@us-legal-tools/govinfo-sdk/mcp`.
**Credentials:** required; free key at api.data.gov/signup.

## Wire it into Hermes

`hermes mcp add govinfo` with command `npx` and args `['@us-legal-tools', 'govinfo-sdk', 'mcp']` GOVINFO_API_KEY=<YOUR_API_KEY>

Equivalent Claude-style JSON (for reference):

```json
{
  "mcpServers": {
    "govinfo": {
      "command": "npx",
      "args": [
        "@us-legal-tools/govinfo-sdk/mcp"
      ],
      "env": {
        "GOVINFO_API_KEY": "<YOUR_API_KEY>"
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
