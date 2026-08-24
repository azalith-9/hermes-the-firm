---
name: wiki-testing
description: Use when a user asks about software testing methodologies, quality assurance for legal-tech products, AI evaluation frameworks, hallucination detection, or how to test legal AI outputs. Provides a reference on the full spectrum of software testing — unit through chaos — with specific coverage of AI-specific evaluation techniques including eval suites, hallucination tests, and output drift detection applicable to legal AI systems.
license: MIT
metadata: " id: wiki.testing category: wiki jurisdictions: [__multi__] priority: P3 intent: [__wiki__, software testing, AI evaluation, hallucination testing, legal AI quality, eval suites] related: [wiki-tech, wiki-skill, wiki-research] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Registered as a flat plugin skill.
-->


# Software Testing & AI Evaluation Reference

## Scope

This pack covers software testing methodologies from unit testing through chaos engineering, and then focuses specifically on AI evaluation techniques. The second half addresses the unique quality challenges of legal AI systems: hallucination risk, jurisdictional accuracy, output consistency, and regression testing when models are updated.

---

## Software Testing Taxonomy

### By Scope

| Type | What it tests | Who writes it | Tools |
|------|-------------|--------------|-------|
| Unit | Individual function or module in isolation | Developer | Jest, pytest, JUnit, Go testing |
| Integration | Interaction between modules or services | Developer / QA | Postman, pytest, Supertest |
| End-to-End (E2E) | Full user workflow from UI to backend | QA / dev | Playwright, Cypress, Selenium |
| Contract | API contracts between services (consumer/provider) | Dev / platform | Pact, Spring Cloud Contract |
| Performance / load | System behavior under load; latency; throughput | QA / SRE | k6, Gatling, Artillery, Locust |
| Security | Vulnerabilities, input sanitization, auth | Security / QA | OWASP ZAP, Burp Suite, Snyk |
| Chaos | System resilience when components fail | SRE | Chaos Monkey, Gremlin, LitmusChaos |
| Smoke | Basic functionality after deployment | QA / CI | Part of E2E suite |
| Regression | Previously-fixed bugs have not returned | QA / CI | Full test suite run on every PR |

### By Layer (Legal-Tech Stack)

For a legal AI product:

| Layer | Testing focus |
|-------|-------------|
| UI / chat interface | E2E user workflows; input sanitization; response rendering |
| API gateway | Rate limiting; auth; input validation; error responses |
| Skill router | Correct skill selected for each intent category; edge cases |
| LLM inference | Prompt consistency; token limits; latency; fallback behavior |
| Document generation | Output against golden templates; clause inclusion; variable substitution |
| Data integrations | Data pipeline reliability; schema validation; data freshness |
| Auth / IAM | Permission boundaries; role-based access; token expiry |

---

## Test Quality Principles

### Test Pyramid

The test pyramid (Mike Cohn) recommends:
- **Many unit tests** (fast, cheap, precise)
- **Fewer integration tests** (slower, more realistic)
- **Fewest E2E tests** (slowest, most brittle, highest maintenance)

Anti-pattern: "ice cream cone" — many E2E tests, few unit tests. Common in projects without strong QA discipline; results in slow CI and high flakiness.

### Test Characteristics (FIRST)

| Attribute | Meaning |
|-----------|---------|
| Fast | Tests run quickly (unit tests <100ms) |
| Independent | Tests do not depend on each other or on execution order |
| Repeatable | Same result regardless of environment |
| Self-validating | Clear pass/fail — no manual inspection required |
| Timely | Written before or alongside the code (TDD/BDD) |

### Coverage Targets

- Unit test coverage: 80%+ line coverage is a common target; diminishing returns above 90% for application code
- Critical paths (auth, payment, legal output) should have 100% unit + integration coverage
- Coverage is a lagging indicator — it tells you what is tested, not whether the tests are meaningful

---

## AI-Specific Evaluation

Legal AI introduces testing challenges that conventional software testing does not address: outputs are probabilistic, not deterministic; correctness is often judgment-dependent; and errors can be legally consequential.

### Eval Suites for Legal AI

An eval suite is a curated set of test cases with ground-truth answers used to measure model or system quality.

**Components of a legal AI eval suite:**

| Component | Description | Example |
|-----------|-------------|---------|
| Golden Q&A set | Questions with verified correct answers | "Under UAE Labour Law, what is the minimum notice period for indefinite contracts?" → "30 days" |
| Document extraction tests | Extract specific clauses from contract samples | "What is the governing law clause in this MSA?" |
| Drafting quality tests | Generate a document; check against template or rubric | Generate an NDA; score for required clauses, jurisdiction accuracy, clarity |
| Jurisdiction accuracy | Does the model correctly apply the stated jurisdiction's law? | "Under LB law" vs "under UAE law" — different answers for same question |
| Edge case set | Adversarial and unusual inputs | Conflicting jurisdiction signals; ambiguous instructions; mixed-language inputs |
| Refusal accuracy | Does the model correctly refuse out-of-scope requests? | "Generate a prescription" → should decline |

### Hallucination Testing

Hallucination in legal AI — generating plausible but false legal information — is a high-stakes failure mode.

**Types of legal hallucination:**
1. **Fabricated statute numbers** — citing "Article 47 of UAE Companies Law" when no such article exists or it says something different
2. **Fabricated case citations** — inventing case names that do not exist or misquoting real cases
3. **Outdated law** — citing repealed or amended provisions as current
4. **Jurisdiction bleed** — applying US/UK law to a MENA question, often confidently
5. **Precision overconfidence** — stating exact thresholds, percentages, or amounts without hedging when the underlying law is ambiguous

**Hallucination detection methods:**

| Method | How it works | Strengths | Weaknesses |
|--------|-------------|----------|------------|
| Ground-truth comparison | Compare output to verified database of legal provisions | High precision | Requires comprehensive verified DB |
| Citation verification | Parse all citations; verify against official sources | Catches fabricated citations directly | Misses errors in paraphrased content |
| Expert review | Legal experts review AI outputs | High accuracy | Slow, expensive, unscalable |
| LLM-as-judge | Second LLM model evaluates first model's output | Scalable | Risk of correlated errors |
| Consistency testing | Ask the same question multiple times; flag inconsistencies | Catches high-variance outputs | Does not catch consistently-wrong answers |
| Red-teaming | Adversarial prompts designed to elicit hallucinations | Finds new failure modes | Coverage depends on creativity of testers |

### Drift Detection

Model drift occurs when model behavior changes over time — either because the underlying model was updated or because the inputs have shifted.

For legal AI:
- **Model updates**: when the underlying LLM (the agent, GPT-4, etc.) is updated, legal outputs may change; run the full eval suite against the new model before deploying
- **Prompt drift**: accumulated changes to prompts and skill files can gradually shift output quality; version-control all skill files
- **Distribution drift**: if user input patterns shift (e.g., more Arabic queries, more complex contracts), performance on the original eval suite may not reflect real-world quality

**Drift monitoring approaches:**
- Shadow evaluation: run the new model version in shadow mode (same inputs, outputs not shown to users) and compare outputs against the current version
- A/B evaluation: randomly route a small percentage of traffic to the new version; measure downstream quality signals
- Continuous eval: run a subset of the golden eval suite against every production deployment; alert on regressions

---

## Testing in Legal AI — Specific Protocols

### Regression Testing on Skill Updates

When a skill file is updated:
1. Run the full golden Q&A set for that skill's practice area and jurisdiction
2. Verify that jurisdiction-specific answers have not changed without intent
3. Check clause inclusion in any drafting outputs against the template
4. Review output format compliance (does the output still match the expected schema?)

### Jurisdiction Coverage Testing

A legal AI serving MENA must be tested separately for each jurisdiction it claims to support:
- LB, KSA, UAE (onshore), DIFC, ADGM, EG — minimum coverage
- Each has different labor law defaults, contract formalities, IP regimes
- A test passing for DIFC does not validate UAE-mainland behavior

### Output Format Testing

Legal AI outputs often need to conform to specific formats (JSON for API consumers, structured memo for lawyers, track-change document for contract review):
- Test format compliance separately from content accuracy
- JSON schema validation for structured outputs
- Template adherence scoring for document drafts
- Markdown validity for chat outputs

---

## Quality Metrics for Legal AI

| Metric | Definition | Target |
|--------|-----------|--------|
| Hallucination rate | % of outputs with factual legal errors | <2% on golden set |
| Jurisdiction accuracy | % of jurisdiction-specific answers correct | >95% |
| Clause inclusion rate | % of required clauses present in drafting output | >98% |
| Response latency (P50) | Median time to first token or full response | <3s first token; <30s full response |
| Refusal precision | % of correct refusals (refusing only what should be refused) | >98% |
| Refusal recall | % of out-of-scope requests correctly refused | >95% |
| User satisfaction score | Lawyer rating of output quality | >4.2/5 |

---

## How to Use This Pack

Reference when:
- Designing a QA process for a legal AI product
- Setting up an eval suite for a new jurisdiction or practice area
- Debugging a hallucination reported by a user
- Planning a model upgrade and assessing regression risk
- Writing a vendor assessment for a legal AI tool's quality claims

---

## Caveats & Currency

AI evaluation methods are evolving rapidly. LLM-as-judge approaches, standardized legal benchmarks, and hallucination detection frameworks were all active research areas as of 2024. Verify current best practices in AI evaluation literature before finalizing a QA program.

## Related Skills

- [[wiki-tech]]
- [[wiki-skill]]
- [[wiki-research]]
- [[eval-hallucination-detector]]
- [[heuristic-always-state-jurisdiction-first]]
