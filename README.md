# hermes-the-firm

A complete legal practice for [Hermes Agent](https://github.com/NousResearch/hermes-agent) — **1,155 skills across five layers**, one opt-in entry point, zero session-start cost.

```
DEPARTMENTS      12 practice areas        anthropics/claude-for-legal
FEDERAL RESEARCH live MCP connectors      beshkenadze/us-legal-tools
CORPUS           US primary law on disk   Vaquill/open-us-law
FIRM ADMIN       how the firm runs AI     HAQQ master-claude-for-legal
LOUIS LIBRARY    982 deep-knowledge skills, MENA-first
                                          HAQQ mini-claude-for-legal
```

Ported from four upstreams:

| Source | License | What it contributes |
|---|---|---|
| [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | Apache-2.0 | 12 practice-area departments + watcher agents + practice-profile system |
| [beshkenadze/us-legal-tools](https://github.com/beshkenadze/us-legal-tools) | MIT | Federal MCP layer: eCFR, Federal Register, CourtListener (case law), govinfo — wiring skills + catalog |
| [Vaquill/open-us-law](https://github.com/vaquill/open-us-law) | CC BY 4.0 (data) | The corpus: ~3M sections of US statutes/constitutions/court rules; coverage manifest drives the skills' honesty about what's verified |
| [HAQQ Legal AI / master-claude-for-legal](https://github.com/haqq-ai/master-claude-for-legal) | MIT | AI governance skills, privilege-layer reference docs, firm AI policy / client data explainer / vendor security templates |
| [HAQQ Legal AI / mini-claude-for-legal](https://github.com/haqq-ai/mini-claude-for-legal) | MIT | The Louis library: drafting, review, litigation simulation, education, safety, personas, connectors — Lebanon/KSA/UAE/Egypt/DIFC/ADGM first, FR/UK/US/EU secondary |

## How the layers work together

A Michigan workers'-comp question routes like this: the department skills
frame it against the firm's playbook, `us-statute-lookup` pulls MCL 418's
actual text from the local corpus (Michigan ships complete and human-
verified), `federal-courtlistener-setup` adds case law when wired,
`us-citation-verify` round-trips every cite before anything is filed.
Primary law on disk, live federal data on tap, case law via connector.

## The name

"for-legal" names a tool; a firm is an institution — departments,
administration, a library, and an associate who never sleeps. Also:
who's alive to say Hermes wasn't firm? *Hermes: The Firm* (a la Spaceballs:
The Movie). It scans like Kermit The Frog. And there was that TV show.

## Design

- **Opt-in, not always-on.** Plugin skills are explicit loads: nothing
  enters context until `skill_view("hermes-the-firm:<skill>")` is called.
  No hooks, no bootstrap injection at session start.
- **One flat namespace, honest ownership.** All 1,147 skills register as
  `hermes-the-firm:<name>`. Cross-source name collisions are prefixed
  (`firm-admin-tabular-review`); which skill belongs to what is recorded
  at port time in `references/owner-map.json`, never guessed at runtime.
- **Practice profiles are the product.** Each department has a cold-start
  interview that writes `~/.hermes/plugins/config/hermes-the-firm/<area>/PRACTICE.md`.
  Until populated, department skills refuse to give generic answers on
  purpose. Louis and firm-admin skills are self-contained.

## Install

```bash
git clone <this-repo> ~/projects/hermes-the-firm    # or cp -r
mkdir -p ~/.hermes/plugins
ln -s ~/projects/hermes-the-firm ~/.hermes/plugins/hermes-the-firm
hermes plugins list
hermes plugins enable hermes-the-firm
# answer N to "replace built-in tools?" — this plugin registers one
# command and read-only skills only
```

Restart your session (or `hermes gateway restart`).

## Usage

```text
/hermes-the-firm                       roster: departments + connectors + corpus + library
/hermes-the-firm litigation            one department's skills
/hermes-the-firm federal-mcp           federal research connector wiring
/hermes-the-firm firm-admin            AI governance layer
/hermes-the-firm primary-law           US statute lookup / citation verify
/hermes-the-firm louis                 Louis categories overview
/hermes-the-firm louis draft           one category (102 drafting skills)

skill_view("hermes-the-firm:nda-review")             direct load
skill_view("hermes-the-firm:us-statute-lookup")      corpus search
```

First run in a department: load its `<prefix>-cold-start-interview`.

## Regenerating from upstream

```bash
# regeneration from the upstream checkouts is done with our
# internal port toolchain (not part of this distribution);
# verification:
python3 -m pytest tests/ -q
```

Regeneration is idempotent and rebuilds `skills/`, `templates/`, and
generated files under `references/` wholesale. Don't hand-edit those
trees; changes belong in the upstream sources.

Notable converter fixes applied on port:
- 70 Louis skills shipped broken YAML frontmatter upstream (unquoted
  `:` scalars) — quoted automatically, verified parseable.
- `tabular-review` existed in both corporate-legal and the master pack;
  both preserved, master's renamed `firm-admin-tabular-review`.

## Verification status

- `pytest tests/` — 12 leak/structure/source tests green
- Herminator validation — 1,155/1,155 SKILL.md valid
- Real `PluginManager` load — 1,155 skills + `/hermes-the-firm` command
  registered; namespaced resolution confirmed across all five layers

## Attribution

- Practice departments: Anthropic (claude-for-legal), Apache-2.0
- Federal MCP wiring: beshkenadze (us-legal-tools), MIT
- US law corpus data: Vaquill (open-us-law), CC BY 4.0
- Firm admin + Louis library: HAQQ Legal AI, MIT
- Port: rJ9, following the hermes-superpowers port conventions.
  See LICENSE and THIRD-PARTY-NOTICES.md.
