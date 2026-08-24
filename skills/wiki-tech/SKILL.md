---
name: wiki-tech
description: Use when a user asks about the technology industry, major tech company dynamics, geopolitics of technology (US-China, EU regulation), AI regulation, or the intersection of technology trends and legal practice. Provides a reference on the tech landscape for legal professionals advising tech companies, drafting tech-sector contracts, or navigating tech regulation in MENA and globally.
license: MIT
metadata: " id: wiki.tech category: wiki jurisdictions: [__multi__, UAE, EU, US] priority: P3 intent: [__wiki__, tech industry, FAANG, geopolitics of tech, AI regulation, EU tech regulation] related: [wiki-startup, wiki-strategy, wiki-space, wiki-vc-startups] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'wiki'.
Registered as a flat plugin skill.
-->


# Technology Industry Reference

## Scope

This pack provides a legal-professional's guide to the technology industry landscape: major companies and their business models, geopolitical tensions shaping tech regulation, key regulatory frameworks (US, EU, MENA), and the legal practice areas most directly implicated by tech industry activity.

---

## Major Technology Company Groups

### FAANG / MAANG (US Mega-Cap Tech)

| Company | Business model | Primary legal exposure |
|---------|---------------|----------------------|
| Meta (Facebook) | Advertising (social media data) | Privacy, content moderation, antitrust |
| Apple | Hardware + App Store + services | Antitrust (App Store), privacy (ATT), IP |
| Amazon | E-commerce + AWS + advertising | Antitrust, labor, data, financial services (payments) |
| Netflix | Subscription streaming | IP (content licensing), content regulation |
| Google / Alphabet | Advertising + cloud + AI | Antitrust, privacy, AI regulation, copyright |
| Microsoft | Enterprise software + cloud (Azure) + AI (OpenAI investment) | Antitrust, enterprise contracts, AI regulation |
| Nvidia | AI chips / semiconductors | Export controls, supply chain, antitrust |
| Tesla / SpaceX | EV + autonomous + launch | Product liability, regulatory, employment |

### Chinese Tech Giants

| Company | Business model | Geopolitical-legal significance |
|---------|---------------|-------------------------------|
| Alibaba | E-commerce + Aliyun cloud | Subject to Chinese regulatory crackdown; CFIUS scrutiny for US acquisitions |
| Tencent | Social (WeChat) + gaming + fintech | Data security review (China); investment restrictions in US/EU |
| ByteDance / TikTok | Short-video + AI | National security review (US CFIUS); potential forced divestiture |
| Huawei | Telecom equipment + devices | US export controls; banned from 5G infrastructure in US, UK, Australia |
| Baidu | Search + AI | AI regulation (China's generative AI rules 2023) |

### MENA Tech Ecosystem

Significant regional players:
- **Careem** (UAE, acquired by Uber) — ride-hailing and super-app
- **Noon** (UAE/KSA) — e-commerce
- **Tabby / Tamara** (UAE/KSA) — BNPL fintech
- **Swvl** (Egypt, listed NASDAQ) — mass transit
- **Kitopi** (UAE) — cloud kitchen
- **Anghami** (Lebanon/UAE, listed NASDAQ) — music streaming (first Arab tech company listed on US exchange)
- **talabat** (Kuwait, Delivery Hero subsidiary) — food delivery

---

## Geopolitics of Technology

### US-China Technology Decoupling

The US-China tech rivalry has created a bifurcated global technology supply chain with direct legal implications:

**US export controls on advanced tech to China:**
- Entity List (BIS) — designated Chinese companies barred from receiving US technology without license
- Export Administration Regulations (EAR) — controls on dual-use technology
- CHIPS and Science Act (2022) — restricts semiconductor technology export; US-funded firms cannot expand advanced chip capacity in China
- ITAR — controls on defense-related technology (applies to dual-use space and defense tech)

**CFIUS (Committee on Foreign Investment in the United States):**
- Mandatory review for certain investments in US tech companies by foreign persons
- Chinese investors in AI, semiconductors, quantum computing, biotech face high scrutiny
- Has blocked/unwound several Chinese investments in US tech

**MENA dimension:**
- UAE and Saudi Arabia have signed technology cooperation agreements with both US and China — navigating this requires care
- US government has signaled concern about Chinese tech presence in countries that also receive US security assistance
- Huawei 5G deployments in MENA countries created diplomatic friction with the US

### EU Tech Regulation Wave

The EU has become the dominant global regulator of technology companies:

| Regulation | Year | Subject | Impact |
|------------|------|---------|--------|
| GDPR | 2018 | Data protection | Privacy by design; consent; data subject rights; hefty fines |
| Digital Markets Act (DMA) | 2022 | Gatekeeper platforms | Opens App Stores, requires interoperability, prohibits self-preferencing |
| Digital Services Act (DSA) | 2022 | Online platforms / content | Content moderation obligations; algorithmic transparency; VLOP rules |
| AI Act | 2024 | AI systems | Risk-based framework: prohibited, high-risk, limited-risk, minimal-risk AI |
| Data Act | 2023 | IoT and cloud data | Data sharing obligations; portability; switching rights |
| Cyber Resilience Act | In progress | Product cybersecurity | Security requirements for connected products |
| NIS2 Directive | 2022 | Critical infrastructure cybersecurity | Incident reporting; governance requirements |

### MENA Tech Regulation

MENA is building its own regulatory frameworks:
- **UAE**: Personal Data Protection Law (Federal Decree-Law 45/2021 effective Sept 2023); AI Ethics guidelines; DIFC Data Protection Law 2020; ADGM Data Protection Regulations
- **KSA**: Personal Data Protection Law (PDPL) effective September 2023; AI strategy; National Cybersecurity Authority standards
- **Egypt**: Personal Data Protection Law 2020; Communications Regulatory Authority (NTRA) oversight
- **Lebanon**: Minimal data protection legislation; draft data protection law pending

---

## AI — Technology and Legal Dimensions

### AI Industry Landscape

Key layers of the AI stack:

1. **Foundation model providers**: Anthropic (the agent), OpenAI (GPT-4+), Google (Gemini), Meta (Llama — open source), Mistral, Cohere
2. **Cloud infrastructure**: AWS, Azure, GCP — all offering managed AI inference
3. **Application layer**: thousands of vertical AI applications built on foundation models
4. **Data and tooling**: data annotation, evaluation frameworks, fine-tuning platforms

### Legal Issues in AI

| Issue | Description |
|-------|-------------|
| Copyright in training data | Is using copyrighted content to train AI models infringement? US cases pending; EU AI Act has transparency obligations |
| Copyright in AI output | Can AI-generated content be copyrighted? US Copyright Office: not without human authorship |
| Liability for AI errors | Who is liable when AI gives wrong legal/medical advice? Unsettled; depends on UX framing, disclaimers, jurisdiction |
| Employment impact | AI replacing workers — redundancy law, worker protections; MENA jurisdictions have labor laws requiring consultation |
| Bias and discrimination | AI systems that discriminate in hiring, credit, healthcare; EU AI Act designates these as high-risk |
| Data privacy | Training and inference on personal data; GDPR compliance of AI products |
| Export controls | Advanced AI chips (Nvidia H100/A100) subject to US export controls |

### AI Act (EU) — Risk Categories

| Category | Examples | Requirements |
|----------|---------|--------------|
| Prohibited | Social scoring, real-time biometric surveillance | Banned outright |
| High-risk | CV screening, credit scoring, critical infrastructure, education assessment | Conformity assessment, human oversight, documentation |
| Limited-risk | Chatbots (must disclose AI), deepfakes | Transparency obligations |
| Minimal-risk | Spam filters, AI in video games | Voluntary codes of practice |

---

## Legal Practice Areas Most Impacted by Tech

| Practice area | Tech intersection |
|--------------|-----------------|
| IP / Copyright | Software patents, AI output ownership, open-source licensing |
| Data privacy | GDPR/PDPL compliance for tech products; breach response |
| M&A / corporate | Tech company acquisitions; representations on IP, data, cybersecurity |
| Employment | Non-competes for tech employees; equity plans; AI workforce impact |
| Antitrust | Platform regulation; DMA compliance; merger control for tech deals |
| Finance / FinTech | Crypto regulation; payment services licensing; BNPL |
| Contracts | SaaS MSAs; API terms; cloud service agreements; liability limitations |
| Regulatory | Licensing for AI products; government approval of tech deployments |

---

## How to Use This Pack

Reference when:
- Advising a tech company on regulatory compliance (EU AI Act, GDPR, PDPL)
- Drafting a technology services agreement or SaaS MSA
- Conducting M&A due diligence on a tech target
- Advising on export control compliance for technology transfers to or from MENA
- Providing context to a user question about a specific tech company or AI tool

---

## Caveats & Currency

The tech regulatory landscape is the fastest-moving area of law globally. The EU AI Act, US AI executive orders, and MENA data protection frameworks were all in active implementation as of 2024. Always verify current regulatory status before advising. Company-specific details (revenue, ownership, leadership) change frequently.

## Related Skills

- [[wiki-startup]]
- [[wiki-strategy]]
- [[wiki-space]]
- [[wiki-vc-startups]]
- [[wiki-sales]]
