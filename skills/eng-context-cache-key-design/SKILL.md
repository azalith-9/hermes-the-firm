---
name: eng-context-cache-key-design
description: Use when designing the context-caching layer for a legal AI product built on the agent or similar LLMs. Defines how to construct cache keys that maximize prefix-cache hit rates, how to partition context by scope (system prompt, skill, matter, user), how to handle cache invalidation when legal content changes, and how to measure cache efficiency. Engineering skill with significant cost and latency implications for legal AI deployments.
license: MIT
metadata: " id: eng.context-cache-key-design category: eng jurisdictions: [__multi__] priority: P2 intent: [context-cache, prompt-cache, performance, cost-reduction, LLM] related: - eng-cost-per-message-tracker - eng-latency-slo-by-skill - eng-fallback-model-cascade - eng-embedding-model-choice-legal source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Registered as a flat plugin skill.
-->


# Context Cache Key Design

## What it does

Context (prompt) caching allows an LLM provider to reuse the KV-cache for a prefix of the prompt that has been seen before, avoiding recomputation. For Anthropic's the agent, prompt caching is available via the `cache_control` parameter; tokens in cached prefixes are charged at a lower rate and processed faster.

In a legal AI product with large system prompts, extensive skill libraries, and per-matter context documents, caching is a primary lever for:
- **Cost reduction**: cached input tokens are typically priced at ~10% of uncached input token cost.
- **Latency reduction**: cache hits skip the prefill computation for cached tokens.
- **Predictability**: stable prefixes ensure consistent latency SLOs by skill.

## Context layers in a legal AI product

A typical request context in a legal AI platform has four layers, ordered from most-stable (best to cache) to least-stable (cannot cache):

```
Layer 1: System prompt (MOST STABLE)
  — Firm identity, core behavior rules, safety guardrails
  — Changes: at deployment; on firm onboarding
  — Cache lifetime: days to weeks

Layer 2: Skill content (STABLE)
  — Loaded SKILL.md files for the current skill set
  — Changes: on skill version updates
  — Cache lifetime: hours to days

Layer 3: Matter context (SEMI-STABLE)
  — Engagement letter, matter summary, key documents for this matter
  — Changes: as matter progresses
  — Cache lifetime: minutes to hours (within a session)

Layer 4: User turn (EPHEMERAL)
  — The specific user message in this request
  — Changes: every request
  — Cache lifetime: not cached
```

## Cache key construction

A cache key identifies a unique, cacheable prefix. The key must encode all dimensions that affect the prefix content.

### Layer 1 — system prompt key

```
cache_key = SHA256(
  org_id +
  system_prompt_version +
  firm_profile_hash
)
```

The system prompt should be stored as a versioned artifact. Any change to the system prompt (including firm profile data) must increment the version, invalidating the layer-1 cache.

### Layer 2 — skill content key

```
cache_key = SHA256(
  org_id +
  system_prompt_version +           # includes layer 1
  skill_set_hash                    # hash of all loaded skill IDs + versions
)
```

The skill set hash is computed from the sorted list of `{skill_id}:{version}` pairs loaded for this request. If the same skill set is always loaded, this key is stable and the cache hit rate is high. Avoid per-request dynamic skill loading — it destroys layer-2 cache efficiency.

### Layer 3 — matter context key

```
cache_key = SHA256(
  org_id +
  system_prompt_version +
  skill_set_hash +
  matter_id +
  matter_context_version            # increments when matter documents change
)
```

Matter context documents (engagement letter, key filings, current draft under review) change as the matter progresses. The `matter_context_version` is a monotonic counter managed by the eFirm system, incremented each time any matter-context document changes.

### Layer 4 — user turn

Not cached. The user message is always appended fresh.

## Prefix ordering rule

The cache prefix must be assembled in strict layer order (1 → 2 → 3 → 4). The provider's cache only hits if the prefix is an exact byte-for-byte match of a previously seen prefix. Any reordering of tokens, even if semantically equivalent, is a cache miss.

```
Final prompt = [Layer 1: system] + [Layer 2: skills] + [Layer 3: matter] + [Layer 4: user]
```

Always construct in this order. Never interleave layers.

## Cache invalidation triggers

| Event | Layer invalidated | Action |
|---|---|---|
| System prompt update | L1, L2, L3 | Increment system_prompt_version; all caches must be rebuilt |
| Skill version update | L2, L3 | Increment skill version in the skill registry |
| New skill loaded for org | L2, L3 | Recompute skill_set_hash |
| Matter document updated | L3 only | Increment matter_context_version for that matter |
| Firm profile changed | L1, L2, L3 | Treat as system prompt update |

## Measuring cache efficiency

Track per-request:

| Metric | Description | Target |
|---|---|---|
| `cache_hit_rate_l1` | % of requests where Layer 1 was a cache hit | >95% |
| `cache_hit_rate_l2` | % of requests where Layer 2 was a cache hit | >80% |
| `cache_hit_rate_l3` | % of requests where Layer 3 was a cache hit | >40% (varies by matter activity level) |
| `input_tokens_billed_uncached` | Tokens billed at full price | Minimize |
| `input_tokens_billed_cached` | Tokens billed at reduced price | Maximize |
| `cache_miss_cost_spike` | Request where all three layers are misses | Alert if > [threshold] in an hour |

These metrics feed into [[eng-cost-per-message-tracker]].

## Legal product specifics

- **Privilege isolation**: matter context (Layer 3) is per-matter and per-client. Never share a Layer-3 cache prefix across different clients. Enforce tenant isolation at the cache key level — `org_id` must be in every key.
- **Confidentiality on cache servers**: if using Anthropic's prompt caching, review the data-processing terms. For highly sensitive matters, consider whether to opt into caching at all (accept the cost/latency trade-off for maximum data isolation).
- **Skill library size**: legal AI products load many skills. If the total skill content exceeds the provider's max cacheable prefix (e.g., ~200K tokens for the agent), prioritize which skills are in the "always loaded" set vs. loaded on demand. Always-loaded skills benefit from the Layer-2 cache; on-demand skills are always cache misses at Layer 2.

## Related skills

- [[eng-cost-per-message-tracker]]
- [[eng-latency-slo-by-skill]]
- [[eng-fallback-model-cascade]]
- [[eng-embedding-model-choice-legal]]
