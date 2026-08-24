---
name: router-intent-detection
description: Use as the primary intent classifier for every incoming user message. Classifies each message into exactly one primary intent and zero or more secondary intents from a defined label set — drafting, review, research, summarize, translate, compare, calculate, advice, admin, chitchat. Outputs a JSON object with primary intent, secondary intents, and confidence score. Routes low-confidence messages to the clarifying-questions skill rather than guessing.
license: MIT
metadata: " id: router.intent-detection category: router priority: P0 intent: [__router__] related: [router-complexity-grader, router-jurisdiction-detector, router-practice-area-detector, router-persona-selector, router-confidence-scorer] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'router'.
Registered as a flat plugin skill.
-->


# Intent Detection Router

## Purpose

The intent classifier is the first gate in the request pipeline. It determines what the user wants to do — not what topic they are asking about (that is the practice-area detector) or where (that is the jurisdiction detector). Getting intent right at this stage ensures the correct downstream skill is invoked, the correct output format is prepared, and the correct safety checks are applied.

Every incoming user message goes through this classifier. The output is consumed by [[router-complexity-grader]], [[router-practice-area-detector]], and ultimately the skill selector.

## Intent Labels

Exactly one primary intent and zero or more secondary intents are assigned from this set:

### `drafting`
User wants to generate a new document, agreement, clause, notice, letter, or other legal text from scratch or from a brief.

Signals:
- Verb "draft", "write", "create", "generate", "prepare", "make me a…"
- Named document type without an existing document pasted: NDA, MSA, lease, employment agreement, will, SHA, SAFE, MOA
- "Can you write a [document]…"

**Note**: a drafting request that names a known document type is high-confidence drafting even if the user does not say the word "draft". "Can you make me an NDA for my software company?" is unambiguously `drafting`.

### `review`
User wants the AI to read, critique, redline, analyze, or provide comments on an existing document or clause that they have provided.

Signals:
- User pastes or attaches a document with instruction: "review", "check", "look at this", "what do you think of", "red-flag", "is this okay?"
- Verb "review", "analyze", "assess", "evaluate", "critique", "redline"

**Note**: if a user pastes a document without any instruction, the intent is ambiguous. Do not assume review — route to [[conversation-clarifying-questions]] to ask whether they want a review, summary, translation, or something else.

### `research`
User is asking a legal question about a rule of law, statute, regulation, jurisdiction, case, or principle without asking the AI to produce a document or render judgment on a specific situation.

Signals:
- "What is…", "How does…", "Explain…", "What are the rules for…"
- Cites a statute number, regulation, or case and asks what it says
- Asks for a comparative overview: "How do UAE and KSA handle…"

**Distinction from `advice`**: if the question is genuinely about what the law says (not what the user should do), it is `research`. "What is the limitation period under UAE law?" is research. "Has my claim expired?" is advice.

### `summarize`
User wants a shorter version of something — a document, clause, thread, judgment, or regulatory text.

Signals:
- "Summarize", "give me the key points", "TL;DR", "what does this say in plain language", "explain this in simple terms"

### `translate`
User wants a translation of text from one language to another.

Signals:
- Explicit language pair request: "translate this to Arabic", "translate to English"
- Pastes text in one language and asks for it in another
- "What does [foreign phrase] mean in legal context"

**Note**: legal translation from Arabic to English or vice versa may also trigger [[review-translation-quality-ar-en]] as a secondary skill.

### `compare`
User wants an A-vs-B analysis — comparing clauses, jurisdictions, contract versions, or regulatory regimes.

Signals:
- "Compare", "what's the difference between", "how does X differ from Y", "which is better for me"
- Two or more options explicitly stated

### `calculate`
User wants a numerical output — a calculated deadline, end-of-service gratuity, statutory interest, notice period, or other computable result.

Signals:
- "Calculate", "compute", "how much is…", "when does [period] expire", "what is the end-of-service"
- Numbers provided (hire dates, salary, contract value) with a question about a derived quantity

### `advice`
User is asking what they should do, whether they can do something, or what will happen in their specific situation.

Signals:
- "Can I…", "Should I…", "What happens if…", "Is this enforceable against me…", "Do I need to…"
- Describes a specific factual situation and asks for a recommended course of action

**Important**: `advice` is the highest-caution intent. It triggers the no-legal-advice disclaimer check and safety review. See [[safety-compliance-ai-not-privileged-disclaimer-us]] and related skills for handling.

**Distinction from `research`**: "Is this enforceable?" / "What should I do?" = advice. "What does Article 47 say?" = research.

### `admin`
User is asking about billing, settings, account management, plan features, integrations, or the Louis platform itself.

Signals:
- "How do I upgrade…", "What does the Pro plan include…", "My API key…", "Can I connect this to…"

### `chitchat`
User is engaging in small talk, greetings, or off-topic conversation with no legal task.

Signals:
- Greetings: "Hi", "Hello", "How are you"
- Off-topic: "Tell me a joke", "What's the weather like"
- Follow-up affirmations in conversation: "Thanks", "Got it", "Sounds good"

## Logic — Classification Rules

1. Parse the message for the primary action verb and the object of the request
2. Apply the intent label whose definition best matches the action verb + object pair
3. Assign secondary intents for any substantive parallel task (e.g., "draft me an NDA and explain the key clauses" → primary: `drafting`, secondary: `research`)
4. Set confidence based on: (a) clarity of the verb; (b) absence of ambiguity about what the user wants; (c) whether context is required to disambiguate

### Confidence thresholds

- **≥ 0.80**: high confidence; proceed with the classified intent
- **0.60–0.79**: moderate confidence; classify but note uncertainty in any downstream skill calls
- **< 0.60**: low confidence; do not proceed with the classified intent; route to [[conversation-clarifying-questions]] to ask "Do you want me to [option A], [option B], or [option C]?"

### Specific disambiguation rules

- Document pasted with no instruction → `confidence < 0.60`; ask before classifying
- "Is this enforceable?" without context → `advice` at confidence 0.70
- "Can you make me an NDA" → `drafting` at confidence 0.95 even without explicit "draft"
- "What happens if I don't pay?" → `advice` at confidence 0.85

## Output

Return a single JSON object on one line:

```json
{
  "primary": "<label>",
  "secondary": ["<label>", ...],
  "confidence": 0.0-1.0,
  "ambiguity_note": "<if confidence < 0.80, one sentence describing what is unclear>"
}
```

If confidence < 0.60: before returning this JSON (or alongside it, in the same response), invoke [[conversation-clarifying-questions]] to ask the user.

## Related Skills

- [[router-complexity-grader]]
- [[router-jurisdiction-detector]]
- [[router-practice-area-detector]]
- [[router-persona-selector]]
- [[router-confidence-scorer]]
- [[conversation-clarifying-questions]]
