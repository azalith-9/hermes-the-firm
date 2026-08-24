---
name: justice-intent-book-call
description: Use when a user signals intent to speak with a human sales representative, customer success manager, or legal consultant — phrases like 'talk to someone', 'book a demo', 'schedule a meeting', or 'discuss for our firm'. Detects the booking intent, captures pre-call context (use case, firm size, urgency), routes to the appropriate booking channel (Calendly or embedded widget), and generates a pre-meeting brief for the sales rep. Distinct from emergency handoff — this is a commercial conversion flow, not a safety escalation.
license: MIT
metadata: " id: justice.intent.book-call category: justice jurisdictions: [__multi__] priority: P1 intent: [__justice__, book-call, sales, demo, scheduling, commercial-conversion, CRM-handoff] related: [justice-human-handoff, justice-intent-career-application, justice-intent-changelog-status] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'justice'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Justice Intent — Book a Call

## When this applies

This intent fires when a user expresses a desire to connect with a human at HAQQ/Louis — sales, customer success, legal partnerships, or enterprise evaluation. It is a **commercial conversion flow**, entirely distinct from emergency or safety handoffs (see [[justice-human-handoff]]).

---

## Detection patterns

### Strong signals (direct booking intent)
- "talk to someone", "speak with sales", "book a call", "book a demo"
- "schedule a meeting", "set up a meeting", "arrange a call"
- "I want to discuss this for our firm", "can we get on a call?"
- "who can I speak to about pricing / enterprise / partnership"
- "have a conversation about Louis for [firm name]"
- "get a walkthrough", "see a live demo"

### Moderate signals (possible booking intent — confirm first)
- "how do I get started for a law firm?" — might be self-service
- "what are the enterprise features?" — might just need information
- "can Louis handle our whole team?" — might self-serve or need sales

### Negative — do not trigger booking flow
- User asking a factual question that can be answered immediately
- User clearly on a self-service path (has credit card, is signing up)
- User who just wants pricing information (answer with pricing page link first)

---

## Behavior

### Step 1: Confirm intent
For strong signals: proceed directly to booking.
For moderate signals: ask one clarifying question — "Would you like to discuss this with our team, or can I answer your question directly?"

### Step 2: Capture pre-call context
Before handing off to booking, gather from the conversation (or ask 2–3 questions if not already available):

| Context field | Why it matters | How to capture |
|---|---|---|
| Use case | What is the user trying to achieve? | Often stated in conversation; ask if unclear |
| Firm size + role | Determines sales rep + package | "How many lawyers are at your firm?" / "What is your role?" |
| Timeline / urgency | Priority of the opportunity | "When are you looking to get started?" |
| Specific questions | What to prepare for the call | "What's the main thing you'd want to cover on the call?" |
| Current tools | Competitive context | "What tools does your firm currently use for legal drafting/research?" (optional) |

Do not ask more than 3 questions — minimize friction.

### Step 3: Generate pre-meeting brief
Summarize the gathered context in 3–5 bullet points:
```
Pre-call brief for [Firm Name]:
- Use case: [e.g., "contract review + drafting for UAE corporate practice"]
- Firm: [size, type, geography]
- Urgency: [e.g., "evaluating tools for Q2 deployment"]
- Key questions: [e.g., "Arabic language quality, DIFC-specific knowledge, pricing for 15 lawyers"]
- Current tools: [e.g., "currently using Harvey + Word"]
```

This brief is surfaced to the sales rep before the call (via CRM integration or email).

### Step 4: Route to booking
Primary channel:
- **Calendly** (or equivalent): direct link to HAQQ sales calendar (e.g., `calendly.com/haqq-sales` or similar)
- Present 3 available time slots from the next business day if Calendly integration is live
- Fallback: "Here's a link to book a time directly: [link]"

Secondary channel:
- Embedded booking widget in chat (if platform supports it)
- Email-based: "Email us at [sales@haqq.ai] with your preferred times and we'll confirm within 4 hours"

### Step 5: Handoff acknowledgment
Confirm to the user:
- When to expect confirmation
- What the call will cover
- That their context has been captured so the call can start productively
- "While you wait, I'm happy to answer any specific questions about Louis's capabilities."

---

## Skip booking flow if

| Condition | Route instead |
|---|---|
| Question can be answered immediately | Answer directly; offer booking as optional follow-up |
| User clearly wants self-service (has pricing; is signing up) | Route to signup or pricing page |
| Question is an emergency / legal crisis | Route to [[justice-human-handoff]] immediately; do not divert to sales |
| User is a job applicant | Route to [[justice-intent-career-application]] |

---

## Output format

```json
{
  "intent": "book_call",
  "confidence": "high | medium",
  "pre_call_brief": {
    "firm": "...",
    "use_case": "...",
    "firm_size_role": "...",
    "urgency": "...",
    "key_questions": ["...", "..."],
    "current_tools": "..."
  },
  "booking_channel": "calendly | widget | email",
  "booking_url": "https://calendly.com/haqq-sales",
  "message_to_user": "..."
}
```

---

## Edge cases

| Scenario | Handling |
|---|---|
| User wants a call but is in a time zone where HAQQ team is unavailable | Offer asynchronous: "We'll reach out within X hours to confirm a time that works" |
| User is a competitor or journalist | Normal booking flow; do not pre-screen beyond use case |
| User wants a reference call with an existing customer | Route to customer success: "Our customer success team can arrange that — here's the contact" |
| User booked previously and wants to reschedule | Provide reschedule link directly |

---

## Related skills

- [[justice-human-handoff]]
- [[justice-intent-career-application]]
- [[justice-intent-changelog-status]]
