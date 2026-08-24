---
name: messaging-surface-rule-waitlist-email
description: Use when drafting or reviewing waitlist confirmation, waitlist-position update, and waitlist-to-launch conversion emails for a legal AI assistant. Waitlist emails are sent to users who have expressed intent but have not yet used the product — making first-impression accuracy and UPL-safe framing especially important. Covers the welcome-to-waitlist email, position-update drip, early-access invitation, and the full-launch conversion email.
license: MIT
metadata: " id: messaging.surface-rule.waitlist-email category: messaging jurisdictions: [__multi__] priority: P2 intent: [messaging, waitlist, email, onboarding, launch, consumer] related: [messaging-compliance-checker, messaging-allowed-claims-consumer, messaging-banned-claims-consumer, messaging-pricing-framing-b2c, messaging-surface-rule-newsletter-mixed-audience, onboarding-b2c-vs-b2b-fork] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'messaging'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Messaging — Surface Rule: Waitlist Email

## When this applies

This skill governs the **waitlist email sequence** — the series of emails sent from the moment a user joins a waitlist through to their conversion to an active user. It includes:

1. **Waitlist confirmation email** — sent immediately on sign-up
2. **Position / momentum update** — optional periodic emails while the user is on the waitlist
3. **Early-access invitation** — for users moving to the front of the queue
4. **Full launch / "you're in" email** — when the product opens to the user

Waitlist emails reach users at a uniquely high-attention moment: they have just self-selected as interested and are forming their understanding of what the product is. Claims made in these emails become the user's baseline expectation. Over-promising at this stage creates a worse product experience and greater UPL risk than over-promising to a user who has already experienced the product.

---

## Behavior — Waitlist Email Standards

### Core rule: set expectations accurately

Waitlist emails must describe what the product *is*, not what it *will* achieve for the user. They may be aspirational in tone but must not make outcome claims that set unrealistic expectations.

### Consumer audience default

Waitlist sign-ups arrive from paid social, organic search, and word of mouth — primarily non-lawyers. Unless the sign-up flow explicitly captures professional status, treat waitlist emails as consumer-audience copy and apply consumer messaging rules throughout.

If the sign-up flow captures professional status (e.g., a "for lawyers" waitlist), apply lawyer messaging rules for that segment.

---

## Email-by-Email Rules

### Email 1: Waitlist Confirmation (sent immediately)

**Purpose:** Confirm the sign-up, set accurate expectations, build anticipation.

| Element | Rule |
|---------|------|
| Subject line | Confirmatory: "You're on the Louis waitlist" — not "You're going to love this!" |
| Opening | Acknowledge the sign-up warmly; no hyperbole |
| Product description | 2–3 sentences; bridge line territory; "legal information and understanding" framing |
| What to expect | What the product will do for the user when they get access — allowed claims only |
| What it is not | Brief "legal information, not legal advice" statement; sets the right expectation before first use |
| CTA (optional) | "Follow us on LinkedIn for updates" / "Tell a friend and move up the list" |
| Disclaimer | "Louis provides legal information, not legal advice." |

**Allowed in confirmation email:**
- "When you get access, Louis will help you understand your contracts, know your rights, and prepare for any legal situation."
- "We've built Louis for MENA — Lebanon, UAE, and KSA from day one."

**Blocked:**
- "When you get access, Louis will handle all your legal work."
- "No lawyer needed — Louis has you covered."

### Email 2: Position / Momentum Update (optional drip)

**Purpose:** Maintain engagement and interest; prevent drop-off from waitlist.

- Share a product teaser, feature preview, or use-case story
- Use case stories: situational ("Here's how a Lebanese SME founder used Louis to understand their vendor contract in 10 minutes") — allowed if factual and sourced; not allowed if it implies outcome guarantees
- Do not create urgency through false scarcity claims

### Email 3: Early-Access Invitation

**Purpose:** Move the user from waitlist to active user with high conversion intent.

| Element | Rule |
|---------|------|
| Subject line | "Your early access to Louis is ready" — specific, clear, no banned claims |
| Body | Reiterate what the product does; reinforce the "legal information" positioning; transition from anticipation to action |
| First-use guidance | Direct to a first-action prompt: "Start by asking Louis about a contract you need to review" |
| CTA | "Start now — free" or "Activate your access" |
| Disclaimer | Retain the standard disclaimer |

### Email 4: Full Launch Conversion

**Purpose:** When the product opens fully, convert remaining waitlist users.

- More urgent tone is appropriate: "Louis is now open to everyone — your spot is ready"
- May reference the pricing model: free tier + paid upgrade — see [[messaging-pricing-framing-b2c]] for framing rules
- Do not use urgency claims that are false ("Only 100 spots left" — if there is no actual limit)

---

## Technical Email Compliance

All waitlist emails must comply with applicable email marketing law (see [[messaging-surface-rule-newsletter-mixed-audience]] for framework details). Key requirements:
- Physical address in footer
- One-click unsubscribe at every email
- Accurate sender identification
- No deceptive subject lines ("You've been selected" — allowed; "Your legal case has been resolved" — deceptive and blocked)

---

## Examples

**Strong waitlist confirmation subject line:**
> "You're on the Louis waitlist — here's what to expect"

**Weak (avoid):**
> "Get ready — no more lawyer bills!"

**Strong product description in confirmation email:**
> "Louis is a legal AI assistant for MENA — covering Lebanon, UAE, and Saudi Arabia. When you get access, you'll be able to upload a contract and get a plain-language breakdown, ask legal questions about your situation, and generate starting-point documents. Louis provides legal information — not legal advice. For complex matters, we'll tell you when to speak to a lawyer."

---

## Related skills

- [[messaging-compliance-checker]]
- [[messaging-allowed-claims-consumer]]
- [[messaging-banned-claims-consumer]]
- [[messaging-pricing-framing-b2c]]
- [[messaging-surface-rule-newsletter-mixed-audience]]
- [[onboarding-b2c-vs-b2b-fork]]
