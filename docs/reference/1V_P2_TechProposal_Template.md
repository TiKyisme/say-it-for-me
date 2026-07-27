

**TECHNICAL PROPOSAL**  
**Phase 2 — Technical Submission**

| Team / Project Name | *\[Your team name and project title\]* |
| :---- | :---- |
| **Submission Date** | *\[DD / MM / 2026\]* |
| **Version** | v1.0 |
| **Confidentiality** | Restricted — Challenge Review Only |

**How to use this template**

* **Fill out all sections:** Replace bracketed placeholders *`[example]`* with your response. Do not use the sample *italicized* text in your final submission.  
* **Check the rubric:** Review the Evaluation Criteria on Page 2 before you start; judges evaluate strictly against this framework.  
* **Highlight your advantage:** Dedicate extra effort to Section 3 (Business Solution) to clearly demonstrate why your approach is superior to existing alternatives.  
* **Tailor your response:** Add any supplemental details or visual content that best showcases your solution.

**Evaluation Criteria & Scoring Rubric**

**Read this before writing your proposal. Every section you complete maps to one or more criteria below.**

| Criterion | Weight | What Judges Look For |
| :---- | :---- | :---- |
| 1\. AI Approach & Technical Design | 35% | Pipeline completeness, model choices, on-device optimisation strategy, accuracy targets and evaluation plan |
| 2\. Hardware & Device Concept | 25% | Platform justification, BOM feasibility, power budget, form-factor suitability for the target environment |
| 3\. Business Solution | 15% | How the solution addresses the industry gap, differentiation from existing tools, innovation strength, real-world applicability |
| 4\. Problem Definition & Impact | 15% | Clarity of problem, real-world relevance, target user insight, design constraints identified |
| 5\. Team and Execution Plan | 10% | Complementary skills, realistic timeline, milestone feasibility Early demo is a plus |
| **TOTAL** | **100%** |  |

| 📌  Your proposal is evaluated holistically. Strong AI design cannot compensate for missing business differentiation or weak hardware justification. Aim for depth and specificity in every section. |
| :---- |

**1\.  Executive Summary**

*Provide a 200–300 word overview of your entire proposal — the first section judges read.*

| 📌  Cover: (1) the communication problem, (2) your solution and its business case, (3) target users, (4) key technical differentiator. 3–4 short paragraphs. |
| :---- |

**1.1  Problem Overview**

*\[Describe the real-world voice communication gap — who is affected, where, and why existing tools fall short.\]*

**1.2  Proposed Solution**

*\[One or two sentences: solution name, core technology, deployment environment, and what makes it better than current alternatives.\]*

**1.3  Key Value Proposition**

*\[3–4 distinguishing capabilities versus existing solutions. Be specific and measurable.\]*

**2\.  Problem Definition & Target Users**

*↗ Scoring weight: 15% — Problem Definition & Impact*

**2.1  Problem Statement**

*\[Voice communication challenge: who is affected, the environment, why real-time translation is critical, and why current solutions fail to solve it.\]*

**2.2  Impact Analysis**

| Impact Area | Current Pain Point | Consequence |
| :---- | :---- | :---- |
| Safety / Operations | *\[e.g., Misunderstood verbal safety instructions\]* | *\[e.g., Workplace incidents, compliance failures\]* |
| Productivity | *\[e.g., Translation delays between shifts\]* | *\[e.g., Downtime, rework, missed targets\]* |
| Connectivity | *\[e.g., No reliable internet in target environment\]* | *\[e.g., Existing translation apps unusable\]* |

**2.3  Target Users & Use Cases**

| User Segment | Language Need | Primary Context | Priority |
| :---- | :---- | :---- | :---- |
| *\[e.g., Local operators\]* | *\[e.g., VI ↔ EN\]* | *\[e.g., Assembly line, machine operations\]* | *\[e.g., Critical\]* |
| *\[e.g., Foreign supervisors\]* | *\[e.g., KO / ZH ↔ VI\]* | *\[e.g., Production management\]* | *\[e.g., Critical\]* |
| *\[e.g., Technical trainers\]* | *\[e.g., EN ↔ local lang.\]* | *\[e.g., Training, QA sessions\]* | *\[e.g., High\]* |

**2.4  Key Design Constraints**

| Constraint | Target / Requirement |
| :---- | :---- |
| Internet dependency | Zero — fully offline at runtime |
| End-to-end translation latency | *\[e.g., \< 3 seconds\]* |
| Target deployment environment | *\[e.g., Industrial floor, clinic, checkpoint, field site\]* |
| Language pairs required | *\[e.g., VI ↔ EN, VI ↔ KO\]* |
| Additional constraints | *\[e.g., ruggedised housing, \>8 h battery, no display required\]* |

**3\.  Business Solution & Innovation**

*↗ Scoring weight: 15% — Business Solutions*

**3.1  Industry Problem & Solution Fit**

*\[Name 1–2 existing tools or approaches. For each, state the specific failure mode — latency, connectivity requirement, cost, or domain accuracy — and show how your solution directly addresses that gap.\]*

**3.2  Innovation & Competitive Strengths**

| Dimension | Existing Solutions | Your Solution |
| :---- | :---- | :---- |
| Connectivity | *\[e.g., Cloud-required; fails in offline or low-bandwidth environments\]* | *\[e.g., Fully offline — no internet required at runtime\]* |
| Latency | *\[e.g., \>5 s round-trip for cloud apps\]* | *\[e.g., \<3 s end-to-end on-device\]* |
| Domain Accuracy | *\[e.g., Generic models; poor on technical or industry vocabulary\]* | *\[e.g., Fine-tuned on \[industry\] glossary; custom pronunciation lexicon\]* |
| Data Privacy | *\[e.g., Audio and text transmitted to external cloud servers\]* | *\[e.g., All processing on-device; no data leaves the hardware\]* |

| 📌  Be specific — vague claims like "faster" or "more accurate" score low. Quantify the gap: e.g., "Cloud apps return in \>5 s; our solution in \<3 s at zero connectivity." |
| :---- |

*\[In 2–3 sentences, summarise what makes your solution distinctly innovative compared with all available alternatives today.\]*

**4\.  AI Approach & Technical Design**

*↗ Scoring weight: 35% — Highest weighted criterion*

**4.1  System Pipeline Overview**

Describe your end-to-end AI pipeline and justify each stage. Include a pipeline diagram in your final submission.

*\[Map your pipeline stages — e.g., Audio Capture → VAD → ASR → NMT → TTS → Audio Output. Teams using end-to-end multilingual models or LLM-based approaches should describe their architecture equivalently.\]*

**4.2  Module-by-Module Design**

| Module | Model / Framework | Size (est.) | Latency Target | Key Technique |
| :---- | :---- | :---- | :---- | :---- |
| *\[e.g., VAD\]* | *\[e.g., Silero-VAD\]* | *\[\~1 MB\]* | *\[\< 10 ms/frame\]* | *\[Noise suppression, streaming\]* |
| *\[e.g., ASR\]* | *\[e.g., SenseVoice-Small\]* | *\[\~250 MB\]* | *\[\< 500 ms\]* | *\[INT8 QNN, CTC chunked decode\]* |
| *\[e.g., NMT / LLM\]* | *\[e.g., NLLB-200 Distilled\]* | *\[\~300 MB\]* | *\[\< 1,000 ms\]* | *\[4-bit quant, beam search\]* |
| *\[e.g., TTS\]* | *\[e.g., VITS / MMS-TTS\]* | *\[\~80 MB\]* | *\[\< 700 ms\]* | *\[ONNX on NPU/HTP\]* |

**4.3  On-Device Optimisation & Memory Management**

*\[Describe your quantisation approach and memory management strategy (streaming, lazy loading). State your target RAM ceiling and how you stay within it.\]*

**4.4  Robustness & Edge Case Handling**

*\[Describe how the system handles: (a) acoustic challenges — noise, echo, multiple speakers; (b) linguistic challenges — dialects, accents, code-switching; (c) edge cases — silence, rapid speech, out-of-vocabulary terms.\]*

**5\.  Hardware & Device Concept**

*↗ Scoring weight: 25% — Hardware & Device Concept*

**5.1  Platform Selection & Justification**

Compare at least one SoC / compute platform options and justify your choice.

| Criteria | \[Option A — name\] | \[Option B — name\] | Selected? |
| :---- | :---- | :---- | :---- |
| NPU Performance (TOPS) | *\[e.g., 12 TOPS\]* | *\[e.g., 45 TOPS\]* | \[✓ / —\] |
| Power Consumption (TDP) | *\[e.g., 5–7 W\]* | *\[e.g., 23 W\]* | \[✓ / —\] |
| RAM / Storage Support | *\[e.g., 8 GB LPDDR5\]* | *\[e.g., 32 GB LPDDR5x\]* | \[✓ / —\] |
| AI SDK / Toolchain | *\[e.g., QNN, SNPE\]* | *\[e.g., QNN, ONNX\]* | \[✓ / —\] |
| Form Factor Suitability | *\[e.g., Wearable/handheld\]* | *\[e.g., Portable device\]* | \[✓ / —\] |

*\[In 2–3 sentences, justify your final platform choice and describe the device form factor — type (wearable, handheld, lanyard), dimensions, weight, and environmental rating.\]*

**5.2  Key Hardware Components & Power Budget**

| Component | Specification | Peak Power | Notes |
| :---- | :---- | :---- | :---- |
| SoC Module | *\[e.g., QCS6490 Dev Kit\]* | *\[e.g., 5.0 W\]* | *\[CPU \+ NPU active\]* |
| Microphone Array | *\[e.g., 3× MEMS, 16 kHz\]* | *\[e.g., 0.1 W\]* | *\[Beamforming, noise-cancelling\]* |
| Speaker / Audio Out | *\[e.g., 3.5 mm \+ BT 5.3\]* | *\[e.g., 0.5 W\]* |  |
| Battery | *\[e.g., 4,000 mAh Li-Po\]* | — | *\[Target: \>8 h continuous\]* |
| Storage | *\[e.g., 64 GB UFS 3.1\]* | *\[e.g., 0.2 W\]* | *\[OS \+ all AI models\]* |
| Display (optional) | *\[e.g., 2.4″ OLED / None\]* | *\[e.g., 0.3 W\]* |  |
| Total System Budget |  | *\[e.g., \~6.1 W\]* | *\[Must sustain \>8 h on target battery\]* |

# 

# 

# **6\.  System Architecture & Integration**

## 

*↗ This section bridges your AI pipeline (Section 4\) and your hardware platform (Section 5). Judges assess whether the software and hardware layers work coherently as a complete system.* 

## **6.1  Software Stack**

| Layer | Component / Framework | Role |
| ----- | ----- | ----- |
| **OS** | *\[e.g., Android / Linux\]* | *Base runtime & audio I/O* |
| **AI Runtime** | *\[e.g., Qualcomm QNN SDK\]* | *NPU inference execution* |
| **Audio Processing** | *\[e.g., WebRTC / RNNoise\]* | *Noise reduction & VAD* |
| **Model Serving** | *\[e.g., ONNX Runtime / QNN\]* | *ASR, NMT, TTS inference* |
| **App Layer** | *\[e.g., Kotlin / C++ / Python\]* | *UI, pipeline orchestration* |

## 

## **6.2  Architecture Diagram Placeholder**

|  *\[ Insert Architecture Diagram Here\]* |
| ----- |

## 

## **6.3  Offline-First Design Principles** *(if any)*

 *\[e.g,*

1. *All AI models stored on-device; no API calls at runtime*  
2. *Language pack management: pre-load required language pairs on setup*  
3. *Local caching of common phrase translations for sub-100 ms repeat responses*  
4. *Fail-safe audio output: text-to-speaker fallback if TTS model load fails\]*

**7\.  Team Profile & Project Timeline**

*↗ Scoring weight: 10% — Team and Execution Plan*

**7.1  Team Members**

| Name | Role | Expertise | Contribution Area |
| :---- | :---- | :---- | :---- |
| *\[Full Name\]* | *\[e.g., Team Lead / AI Engineer\]* | *\[e.g., NLP, On-device ML\]* | *\[e.g., ASR \+ NMT pipeline\]* |
| *\[Full Name\]* | *\[e.g., Hardware Engineer\]* | *\[e.g., Embedded Systems, SoC\]* | *\[e.g., BOM \+ power design\]* |
| *\[Full Name\]* | *\[e.g., ML Engineer\]* | *\[e.g., Model optimisation, QNN\]* | *\[e.g., Quantisation \+ NPU tuning\]* |
| *\[Full Name\]* | *\[e.g., UX / Product Designer\]* | *\[e.g., UI/UX, User Research\]* | *\[e.g., Form factor \+ UAT\]* |

**7.2  Project Timeline**

| Phase | Milestone | Key Activities | Target Date |
| :---- | :---- | :---- | :---- |
| 1 | Requirements & Research | *\[Problem validation, platform selection, model survey\]* | *\[DD/MM/YYYY\]* |
| 2 | Model Selection & Optimisation | *\[Model selection, quantisation, initial benchmarks\]* | *\[DD/MM/YYYY\]* |
| 3 | On-Device Integration & Testing | *\[SDK deployment, pipeline integration, WER/BLEU/MOS/UAT\]* | *\[DD/MM/YYYY\]* |
| 4 | Finalisation & Submission | *\[Write-up, demo video, packaging, export PDF \+ DOCX\]* | *\[DD/MM/YYYY\]* |

**8\.  Submission Checklist**

All items must be completed before final submission. Missing sections score zero on the relevant rubric criterion.

| \# | Checklist Item | Status |
| :---- | :---- | :---- |
| 1 | Executive Summary written (200–300 words) | \[ \] Done |
| 2 | Problem Statement, Target Users, and Design Constraints completed | \[ \] Done |
| 3 | Business Solution completed — industry gap, solution fit, and competitive differentiation described | \[ \] Done |
| 4 | AI pipeline documented with model specs, latency targets, and optimisation strategy | \[ \] Done |
| 5 | Hardware platform justified; form factor, BOM and power budget filled in | \[ \] Done |
| 6 | Team profiles and project timeline filled in | \[ \] Done |
| 7 | All placeholder text replaced; pipeline/architecture diagram inserted (Section 6.2) | \[ \] Done |
| 8 | Demo video or prototype link attached (if available); document exported as .PDF | \[ \] Done |

