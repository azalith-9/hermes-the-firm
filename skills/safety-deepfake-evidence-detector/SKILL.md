---
name: safety-deepfake-evidence-detector
description: Use when a user submits images, audio, or video as litigation evidence and asks whether it is authentic, or when a legal team needs to assess the integrity of digital media before relying on it in proceedings. Flags media for forensic review using metadata analysis, visual/audio anomaly heuristics, and reverse-image techniques — but never asserts authenticity or inauthenticity definitively. Maps court admissibility frameworks (US FRE 901/Daubert, UK Civil Evidence Act, DIFC/ADGM, MENA civil-law expert appointment) and routes to certified digital forensic examiners.
license: MIT
metadata: " id: safety.deepfake-evidence-detector category: safety jurisdictions: [US, UK, DIFC, ADGM, LB, KSA, UAE, GCC, EU] priority: P0 intent: [safety, evidence, deepfake, digital-forensics, admissibility] related: - safety-synthetic-witness-flagger - safety-ai-disclosure-required-tribunals - safety-bar-rule-1-1-competence-ai - review-evidence-integrity source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'safety'.
Registered as a flat plugin skill.
-->


# Deepfake / Synthetic Evidence Detector

## When to use this

Trigger this skill when:
- A user presents image, audio, or video files as exhibits or evidence in a legal matter.
- A user asks "is this video real?" or "could this have been manipulated?" in a legal context.
- A lawyer is evaluating whether opposing-party media evidence is authentic before trial.
- A client claims that media evidence used against them is fabricated.
- A regulatory submission involves digital media whose provenance is uncertain.

## Hard limit — what this skill does and does not do

**Does**: flag anomalies, identify areas of concern, recommend expert referral, map admissibility frameworks.

**Does not**: definitively declare media authentic or inauthentic. That determination requires a qualified digital forensic examiner with access to the original file, chain-of-custody documentation, and validated forensic tools. AI-based assessment is a triage tool, not a substitute for expert testimony.

Standard output line:
> This media should be reviewed by a qualified digital forensic examiner before being relied upon in proceedings. The following anomalies warrant professional analysis:

## Triage methodology

### Step 1 — Metadata analysis
- **EXIF data** (images/photos): check for creation date, GPS coordinates, device model, software used. Inconsistencies (future dates, mismatched device for claimed provenance, absent metadata on supposedly original files) are flags.
- **Container / codec forensics** (video/audio): check for re-encoding artifacts, codec inconsistencies, anomalous file structure. Generative tools often leave characteristic codec signatures.
- **Generation tool fingerprints**: some AI image and video generators leave statistical patterns (GAN artifacts, diffusion model signatures) detectable through frequency-domain analysis.

### Step 2 — Visual anomaly heuristics (images/video)
- **Facial geometry**: unnatural eye reflections, asymmetric blinking, teeth/gum anomalies at high resolution.
- **Lighting consistency**: light direction inconsistent with background; reflections on glossy surfaces that don't match the light source.
- **Temporal coherence** (video): frame-to-frame inconsistencies in hair, fabric texture, background elements — generative models often struggle with temporal consistency.
- **Lip sync** (video with speech): phoneme-to-lip-movement sync errors; unnatural mouth shape transitions.
- **Compression artifacts**: deepfake generation and re-encoding often produces characteristic block artifact patterns.
- **Background warping**: subtle background distortions around moving faces are a common deepfake artifact.

### Step 3 — Audio analysis
- **Spectrogram review**: AI voice cloning leaves characteristic spectral patterns — look for unusual smoothness, absence of natural breath/swallow sounds, pitch stability anomalies.
- **Prosody**: synthesized speech often has unnatural prosody — uniform stress, unusual pause patterns.
- **Background noise consistency**: sudden changes in background noise profile suggest editing.

### Step 4 — Reverse image / video search
- Run key frames against reverse image search to identify prior appearances of the same media online.
- A media file that appears to have been created for this litigation but shows prior unrelated appearances is a strong provenance flag.
- Date discrepancies between claimed creation date and earliest online appearance are significant.

### Step 5 — Inconsistency with case record
- Does the media content contradict established facts, timelines, or other documentary evidence?
- Are claimed timestamps consistent with known movements or locations of the parties?
- Does the claimed recording match the device, location, or technical setup the party claims?

## Output format

```
## Media Authenticity Assessment — Preliminary (Triage Only)

File: [filename / description]
Assessed by: AI preliminary triage — NOT a forensic determination

### Flags identified:
1. [Flag category]: [Description of anomaly observed]
2. [Flag category]: [Description of anomaly observed]
...

### Recommendation:
Instruct a certified digital forensic examiner to conduct a full analysis of the original file before relying on this media in proceedings or disclosing it to opposing counsel. See admissibility notes below.

### Chain of custody note:
Preserve the original digital file in its original format immediately. Any conversion, compression, or re-encoding may destroy forensic evidence. Maintain a hash (SHA-256) of the original file for verification.
```

## Court admissibility frameworks

### United States — FRE 901 + Daubert
- Authentication (FRE 901): proponent must produce sufficient evidence to support a finding that the item is what the proponent claims.
- For digital media: chain of custody, hash verification, and testimony about how the media was obtained are typically required.
- Expert testimony on deepfake analysis: subject to *Daubert* standard (reliable methodology, peer review, known error rate, general scientific acceptance).
- Post-*Mata* sensitivity: courts are increasingly aware of AI-generated content; proactive disclosure of AI concerns about evidence integrity is advisable.

### United Kingdom — Civil Evidence Act 1995 + CPR
- Civil proceedings: hearsay in documents admissible under CEA 1995; authenticity still challengeable.
- Expert evidence on digital forensics governed by CPR Part 35 (court-appointed or jointly instructed expert preferred).
- The Forensic Science Regulator's Codes of Practice apply to expert digital forensic work.

### DIFC Courts / ADGM Courts
- Evidence Rules and Practice Directions: authenticity challenges proceed by application; expert evidence under Order 40 (DIFC) or equivalent (ADGM).
- Common-law authentication standards apply; courts look for chain of custody and expert verification.

### MENA civil-law jurisdictions (KSA, UAE, LB, EG)
- Expert-centered system: the court typically appoints a court expert (khabir) to assess disputed evidence.
- Parties can submit private expert reports but the court-appointed expert's opinion carries greater weight.
- Requesting appointment of a digital forensics expert through the court is the primary route for challenging media authenticity.
- UAE Federal Law on Evidence in Civil and Commercial Transactions (Law 10 of 1992, as amended) governs.

## Escalation

Always route to a **certified digital forensic examiner**. Certification bodies include:
- US: IACIS (International Association of Computer Investigative Specialists), ISFCE
- UK: Chartered Institute for IT (BCS), UKSF (UK Secure Forensics)
- MENA: regional IT forensics firms accredited by local courts; some INTERPOL-accredited practitioners

## Related skills

- [[safety-synthetic-witness-flagger]] — complementary skill for detecting AI-generated written testimony
- [[safety-ai-disclosure-required-tribunals]] — disclosure obligations for AI-assisted court work
- [[safety-bar-rule-1-1-competence-ai]] — competence duties when relying on AI analysis
- [[review-evidence-integrity]] — broader evidence integrity review workflow
