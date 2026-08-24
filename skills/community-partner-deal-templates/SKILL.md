---
name: community-partner-deal-templates
description: Use when structuring, drafting, or reviewing a HAQQ partnership agreement across five deal types — reseller (commission, territory, exclusivity), tech integration (API access, branding, mutual referral), co-marketing (content and event obligations), strategic (equity, governance, lockup), and academic (discount, research, co-authorship). Produces a term sheet or heads of terms appropriate for the deal type, with MENA-region considerations and references to existing HAQQ partners (Tawqi3i, Mani Group, Oneic, Highworth, Amman Arab University).
license: MIT
metadata: " id: community.partner-deal-templates category: community jurisdictions: [__multi__] priority: P1 intent: [__community__, partnership, deal-terms, bd, templates] related: [academy-partnership-pitch, community-bar-association-co-host-webinar, community-nvidia-inception-co-marketing, academy-vc-program-pitch] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'community'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Partner Deal Templates — HAQQ Partnership Term Structures

## When to use this

Invoke when:
- A BD or partnerships team is negotiating a new partnership and needs a term sheet
- A partner asks for HAQQ's standard commercial terms for their deal type
- A legal review of a proposed partnership structure is needed
- An existing partner agreement needs to be renewed or renegotiated
- A new deal type is being structured and there is no existing precedent

## Deal type taxonomy

HAQQ has five primary partnership deal types. Select the appropriate template based on what the partner does:

| Deal type | What the partner does | Revenue model |
|---|---|---|
| Reseller | Sells Louis subscriptions to their customer base | Commission on referred revenue |
| Tech integration | Connects their product to Louis via API | Mutual referral / revenue share / flat fee |
| Co-marketing | Creates content, events, or campaigns with HAQQ | Cost-sharing or barter |
| Strategic | Deep commercial or equity-linked relationship | Equity / revenue share / governance |
| Academic | Education and research partnership | Discount + research + IP terms |

---

## Template 1: Reseller Agreement

### Key terms

**Commission structure:**
- Standard: 15–25% of net subscription revenue from referred customers
- Volume tiers: commission increases at agreed ARR thresholds (e.g., above USD 100k ARR referred, commission increases to 30%)
- Payment: monthly in arrears; 30-day payment terms

**Territory:**
- Default: non-exclusive in reseller's primary market
- Exclusive territory: available for committed partners with minimum revenue guarantees; negotiated separately
- Territory definition: by country or by customer segment (e.g., "all law firms with 50+ lawyers in Jordan")

**Exclusivity:**
- HAQQ does not grant exclusivity as a default
- Limited exclusivity (e.g., exclusive introductions to a specific named customer) available in exchange for higher commission share or minimum commitment
- Non-compete: reseller may not represent competing legal AI products in the same market during the exclusivity period; this must be defined narrowly

**Customer terms:**
- Reseller sells Louis under HAQQ's standard customer terms (not the reseller's own terms)
- Customer data protection: governed by HAQQ's DPA; reseller may not access customer data
- Customer relationship: HAQQ retains the customer relationship for support and upsell; reseller gets attribution credit only

**Term and termination:**
- Initial term: 12 months; auto-renewable
- Termination for convenience: 60 days' written notice
- Termination for cause (non-payment, brand violation): 14 days' written notice with cure period

---

## Template 2: Tech Integration Agreement

### Key terms

**API access:**
- HAQQ provides API access under a developer agreement
- Rate limits: agreed per use case; subject to fair-use policy
- SLA: uptime guarantee for production API integrations (99.5% monthly uptime target)
- Versioning: HAQQ provides 90 days' notice of breaking API changes

**Branding:**
- "Powered by Louis" badge available for qualifying integrations
- Co-branded marketing assets: HAQQ approval required before publication
- Brand guidelines apply: both parties must comply with each other's brand guidelines

**Mutual referral:**
- Each party refers customers to the other where a natural use case exists
- Referral attribution: UTM-tracked; commission (if any) specified separately
- No obligation to refer a minimum number of customers unless otherwise agreed

**Revenue share (where applicable):**
- For integrations where HAQQ's API is embedded in the partner's paid product: negotiated revenue share (typically 10–20% of net incremental revenue attributable to the integration)

**IP:**
- Each party retains all IP in its own product
- Integration-specific customizations: owned by the party that created them; licensed to the other for integration purposes only
- No assignment of underlying IP without express written agreement

---

## Template 3: Co-Marketing Agreement

### Key terms

**Content obligations:**
- Each party specifies the content deliverables it will contribute (blog posts, webinars, social posts, case studies)
- Content calendar: agreed in advance; minimum 2-week lead time for review
- Approval rights: each party approves content that references them before publication

**Event obligations:**
- Co-hosted events: cost-sharing model (split agreed per event)
- Speaking: each party provides a speaker for joint events; travel costs borne by each party
- Branding: co-branded event materials; both logos; prominence negotiated

**Lead sharing:**
- Leads generated at co-branded events: split by attribution (who brought the lead)
- Neither party may use the other's leads for outbound campaigns without express consent

**Term:**
- Campaign-specific or annual rolling; no long-term commitment required for co-marketing unless tied to a larger strategic deal

---

## Template 4: Strategic Partnership Agreement

Strategic deals involve deeper commercial commitment — potentially equity, governance rights, or long-term revenue sharing. These terms are negotiated case-by-case and should involve qualified legal counsel for both parties.

**Key structural elements:**
- **Equity component** (if any): HAQQ equity (common or preferred shares, options, or warrants) in exchange for strategic value contribution (distribution access, technology, capital)
- **Governance**: board observer rights (common at certain equity thresholds); information rights; anti-dilution provisions
- **Revenue sharing**: long-term revenue share on a defined customer segment or geography; capped or uncapped
- **Lockup**: equity holder lockup on HAQQ shares for agreed period; transfer restrictions
- **Exclusivity**: strategic partners may negotiate exclusive rights in a market segment for the duration; requires significant commercial commitment in exchange

**Process:** strategic deals must be reviewed and approved by HAQQ's board or designated officer. No binding terms should be discussed with a potential strategic partner without board-level authorization.

---

## Template 5: Academic Partnership Agreement

### Key terms

**Discount:**
- Verified students: free Justinian access (see [[academy-students-program]])
- Faculty and researchers: discounted professional-tier access (typically 70–80% off commercial rate)
- Institutional license: flat-fee annual license covering all enrolled law students + faculty at the institution

**Research:**
- Joint research projects: each party contributes resources under a jointly agreed research protocol
- HAQQ access obligations: HAQQ may provide anonymized usage data for research purposes under a data license agreement
- Publication rights: each party may publish research it authors; joint publications require both parties' approval before submission

**Co-authorship:**
- Where a HAQQ team member substantively contributes to a research paper: co-authorship acknowledgment required
- Where HAQQ provides data only: acknowledgment in the methodology section sufficient

**IP from research:**
- Background IP: retained by each party
- Foreground IP (developed during the partnership): jointly owned unless otherwise agreed; neither party may commercialize jointly-owned IP without the other's consent

---

## Existing HAQQ partners — deal-type reference

| Partner | Deal type | Notes |
|---|---|---|
| Tawqi3i | Tech integration | Lebanese e-notarization; API integration for draft-to-sign workflow |
| Mani Group | Reseller / distribution | MENA professional services distribution |
| Oneic | Tech integration / strategic | Technology ecosystem partner |
| Highworth | Reseller / strategic | Gulf region professional services |
| Amman Arab University | Academic | Jordan; student and faculty program |

---

## Governing law and dispute resolution for partnership agreements

- Preferred governing law for MENA partnerships: UAE law (onshore) or DIFC law (for English common-law flexibility)
- Dispute resolution: negotiation → mediation → arbitration (DIAC or ICC; seat in Dubai or DIFC)
- For academic partnerships with Lebanese institutions: Lebanese law and LBBA-affiliated arbitration is an acceptable alternative

## Related skills

- [[academy-partnership-pitch]]
- [[community-bar-association-co-host-webinar]]
- [[community-nvidia-inception-co-marketing]]
- [[academy-vc-program-pitch]]
