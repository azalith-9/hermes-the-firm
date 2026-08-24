# hermes-the-firm

A complete legal practice for [Hermes Agent](https://github.com/NousResearch/hermes-agent) — **1,147 skills across three layers**, one opt-in entry point, zero session-start cost.

```
DEPARTMENTS      12 practice areas (from anthropics/claude-for-legal)
FIRM ADMIN       how the firm runs AI   (from HAQQ master-claude-for-legal)
LOUIS LIBRARY    982 deep-knowledge skills, MENA-first
                 (from HAQQ mini-claude-for-legal)
```

Ported from three upstreams:

| Source | License | What it contributes |
|---|---|---|
| [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) | Apache-2.0 | 12 practice-area departments + watcher agents + practice-profile system |
| [HAQQ Legal AI / master-claude-for-legal](https://github.com/haqq-ai/master-claude-for-legal) | MIT | AI governance skills, privilege-layer reference docs, firm AI policy / client data explainer / vendor security templates |
| [HAQQ Legal AI / mini-claude-for-legal](https://github.com/haqq-ai/mini-claude-for-legal) | MIT | The Louis library: drafting, review, litigation simulation, education, safety, personas, connectors — Lebanon/KSA/UAE/Egypt/DIFC/ADGM first, FR/UK/US/EU secondary |

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
/hermes-the-firm                       roster: departments + admin + library
/hermes-the-firm litigation            one department's skills
/hermes-the-firm firm-admin            AI governance layer
/hermes-the-firm louis                 Louis categories overview
/hermes-the-firm louis draft           one category (102 drafting skills)

skill_view("hermes-the-firm:nda-review")             direct load
skill_view("hermes-the-firm:draft-agency-agreement") Louis skill
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
- Herminator validation — 1,147/1,147 SKILL.md valid
- Real `PluginManager` load — 1,147 skills + `/hermes-the-firm` command
  registered; namespaced resolution confirmed across all three layers

## Attribution

- Practice departments: Anthropic (claude-for-legal), Apache-2.0
- Firm admin + Louis library: HAQQ Legal AI, MIT
- Port: rJ9, following the hermes-superpowers port conventions.
  See LICENSE and THIRD-PARTY-NOTICES.md.
