# 📋 Briefing Document — "Say It For Me" | OneVoice AI Challenge

> **Mục đích tài liệu:** Tóm tắt toàn bộ ngữ cảnh cuộc thi, quyết định đã đưa ra, và trạng thái hiện tại của dự án để bất kỳ AI agent nào đọc đều có thể tiếp tục hỗ trợ team mà không cần hỏi lại từ đầu.
>
> **Ngày cập nhật:** 27/07/2026
> **Conversation ID gốc:** `9f3efcef-c685-4011-af80-ebe2e3b23069`
>
> **Quy tắc đọc:** Các mục 1–8 giữ lại bối cảnh hình thành ý tưởng. Khi có
> mâu thuẫn, mục 9–10 và các file hiện hành trong `say-it-for-me/docs/team/`,
> PRD v3 và ADR được chấp nhận là nguồn sự thật mới hơn.

---

## 1. CUỘC THI — ONEVOICE AI CHALLENGE

### 1.1 Thông tin chung

| Mục | Chi tiết |
|---|---|
| **Tên cuộc thi** | OneVoice AI Challenge |
| **Website** | https://saigonaihub.com/OneVoiceAIChallenge |
| **Đăng ký** | https://luma.com/g1rwi7ag |
| **Ban tổ chức** | Saigon AI Hub × Qualcomm |
| **Thời gian** | Tháng 5 – Tháng 11/2026 |
| **Địa điểm chung kết** | VNG Campus, TP.HCM, Việt Nam |
| **Đề bài** | Thiết kế thiết bị dịch thuật giọng nói thời gian thực (realtime translation device) sử dụng **Edge AI**, chạy hoàn toàn **on-device** (không cần cloud/internet), phục vụ giao tiếp cho người lao động tại châu Á |

### 1.2 Timeline cuộc thi (5 Phase)

| Phase | Thời gian | Nội dung |
|---|---|---|
| **Phase 1** | Tháng 5–6/2026 | Đăng ký đội |
| **Phase 2** | 27/07–21/08/2026 | **Nộp Technical Proposal**; hạn chính thức hết ngày 21/08/2026 |
| **Phase 3** | Tháng 8–9/2026 | **Nộp Prototype** (nguyên mẫu hoạt động được) |
| **Phase 4** | Tháng 10/2026 | Field testing & Evaluation (thử nghiệm thực tế) |
| **Phase 5** | Tháng 11/2026 | Chung kết — Live Demo tại TP.HCM |

### 1.3 Tiêu chí chấm điểm

| Tiêu chí | Trọng số | Mô tả |
|---|---|---|
| **Innovation & Novelty** | 25% | Cách tiếp cận sáng tạo, tính năng bổ sung có ý nghĩa |
| **Technical Excellence** | 50% | Hiệu suất hệ thống: accuracy, speed, latency, stability |
| **Business Impact & Real-World Potential** | 25% | Tính khả thi thương mại, khả năng mở rộng, ứng dụng thực tế |

### 1.4 Cặp ngôn ngữ được hỗ trợ

Cuộc thi cho phép chọn 1 trong 3 cặp:
- Vietnamese ↔ English
- Vietnamese ↔ Mandarin (Trung Quốc)
- Vietnamese ↔ Korean (Hàn Quốc)

### 1.5 Yêu cầu kỹ thuật cốt lõi từ BTC

- Giải pháp phải chạy **100% on-device (Edge AI)**, không phụ thuộc cloud
- Có thể triển khai trên **bất kỳ thiết bị di động nào** (không giới hạn form factor)
- Khuyến khích dùng model từ **Qualcomm AI Hub** (đã pre-optimized cho Snapdragon)
- Benchmark cụ thể sẽ được công bố trước Phase 3

### 1.6 Đối tượng tham gia

- Nhà nghiên cứu độc lập, startup, team đại học
- Team bất kỳ kích thước nào
- Giải pháp phải là **bản gốc**, tạo riêng cho cuộc thi
- **Không được** nộp sản phẩm đã thương mại hóa

### 1.7 Ban giám khảo

| Tên | Chức vụ | Tổ chức |
|---|---|---|
| Dr. Châu Thành Đức | Lecturer, Faculty of IT | HCMUS, VNUHCM (SAIH Board) |
| Mr. Võ Trọng Thư | AI Manager, AI Lab | GreenNode (SAIH Board) |
| Prof. Dr. Quản Thành Thơ | Dean, Faculty of CS&E | HCMUT, VNUHCM (SAIH Board) |
| Mr. Hoàng Ngọc Thức | Product Marketing Manager | Qualcomm Vietnam |
| Ms. Nguyễn Thanh Thảo | Staff Manager, Business Dev | Qualcomm Vietnam |

---

## 2. DỰ ÁN — "SAY IT FOR ME"

### 2.1 Thông tin đăng ký

| Mục | Giá trị đã chọn |
|---|---|
| **Tên dự án** | Say It For Me |
| **Cặp ngôn ngữ** | **VN ↔ KR (Vietnamese ↔ Korean)** |
| **Giai đoạn hiện tại** | Idea |
| **Ngành ứng dụng** | **Manufacturing** (Sản xuất) |
| **Team size** | 4 người |

### 2.2 Lý do chọn VN-KR + Manufacturing

- Samsung, LG, Hyosung, CJ... có **hàng trăm ngàn công nhân VN** làm việc cùng quản lý/kỹ sư Hàn Quốc
- Rào cản giao tiếp trên dây chuyền sản xuất là **nỗi đau thực tế lớn** nhưng chưa có giải pháp triệt để
- Môi trường nhà máy **ồn ào** → phù hợp với tính năng noise-aware ASR (điểm Innovation)
- Nhà máy có yêu cầu **bảo mật dữ liệu** nghiêm ngặt → Edge AI offline là giải pháp duy nhất khả thi
- Kết hợp VN-KR + Manufacturing tạo narrative mạnh cho **Business Viability** (25% điểm)

### 2.3 Các câu trả lời form đăng ký đã soạn (Tiếng Anh)

#### "Briefly describe your proposed solution"
> The solution uses a lightweight on-device speech pipeline combining noise-aware speech recognition, a quantized multilingual translation model, and fast local text-to-speech synthesis to deliver natural bilingual conversations with minimal latency.

#### "What makes your solution innovative or different?"
> "Say It For Me" distinguishes itself through three key innovations: (1) Resiliency in Harsh Environments — noise-aware ASR optimized for factories; (2) True Zero-Dependency Edge Processing — 100% on-device, no cloud; (3) Unified Ultra-Low Latency Flow — tightly integrated ASR→Translation→TTS pipeline on Snapdragon.

#### "Describe your technical approach"
> End-to-end offline pipeline: (1) DeepFilterNet3/RNNoise noise suppression → (2) Whisper-tiny/base INT8 ASR → (3) NLLB-200/M2M100 INT8 translation → (4) Piper/VITS TTS. All compiled for Snapdragon NPU via Qualcomm AI Hub / ONNX Runtime.

#### "What impact do you expect?"
> Four pillars: (1) Operational Efficiency — instant bilingual communication; (2) Enhanced Workplace Safety — accurate safety protocol communication in noisy environments; (3) Accelerated Skill Transfer — direct expert-to-worker knowledge sharing; (4) Absolute Data Security — 100% offline, no data leakage.

#### "How could your solution evolve into a real product?"
> Four-phase roadmap: (1) Form-Factor Evolution — from smartphones to smart badges/helmet attachments; (2) Domain-Specific Customization — fine-tuned models per factory; (3) Secure Fleet Management — offline device management portal; (4) Market Scaling — add Mandarin, Japanese modules for broader FDI market.

---

## 3. KIẾN TRÚC KỸ THUẬT

### 3.1 Pipeline tổng quan

```
🎤 Mic → 🔇 Noise Suppression (DeepFilterNet3/RNNoise)
       → 🗣️ ASR (Whisper-tiny/base, INT8)
       → 🌐 Translation (NLLB-200-distilled-600M / M2M100-418M, INT8)
       → 🔊 TTS (Piper/VITS, ONNX)
       → 🔈 Speaker
```

### 3.2 Chi tiết model cho mỗi module

| Module | Model chính | Model dự phòng | Size (INT8) | Latency target |
|---|---|---|---|---|
| **Noise Suppression** | DeepFilterNet3 (~5MB) | RNNoise (~85KB) | ~5MB | < 20ms |
| **VAD** | Silero-VAD | — | ~2MB | < 10ms |
| **ASR** | Whisper-tiny (INT8) | Whisper-base (INT8) | ~40–75MB | < 800ms |
| **Translation** | NLLB-200-distilled-600M (INT8 via CTranslate2) | M2M100-418M | ~200–300MB | < 500ms |
| **TTS Vietnamese** | Piper-VITS (ONNX) | MeloTTS | ~25MB | < 500ms |
| **TTS Korean** | Piper/MB-iSTFT-VITS-Korean (ONNX) | MeloTTS | ~25MB | < 500ms |
| **TỔNG** | | | **~300–400MB** | **< 2.3s** |

### 3.3 Mục tiêu hiệu suất

| Metric | Target |
|---|---|
| End-to-end Latency | < 3 giây |
| BLEU (VN↔KR) | ≥ 25 |
| Offline | 100% |
| Hoạt động trong tiếng ồn | SNR ≥ 5dB |
| Tổng RAM | < 2GB |
| Peak Memory | < 2.5GB |
| Model Loading Time | < 5s |

### 3.4 Hardware & Software Stack

- **Target SoC:** Qualcomm Snapdragon 8 Gen 2/3 hoặc QCS8550 (IoT)
- **Accelerator:** Hexagon NPU + DSP
- **Dev baseline:** ONNX Runtime (Sprint 1 trên PC)
- **Production target:** Qualcomm AI Runtime (QAIRT) / QNN (Phase 3 trên Snapdragon)
- **Key tools:** Qualcomm AI Hub, CTranslate2, HuggingFace Transformers, PyAudio, Silero-VAD

### 3.5 Architecture Decision Records (ADR) — đã đưa ra

| ADR | Quyết định | Lý do |
|---|---|---|
| ADR-001 | Whisper cho ASR | Đa ngôn ngữ, hệ sinh thái quantize trưởng thành, có tiny/base để trade-off |
| ADR-002 | M2M100/MarianMT thay vì NLLB làm primary (đang **bị đặt câu hỏi** — xem Review) | Nhẹ hơn, chỉ cần 1 cặp ngôn ngữ |
| ADR-003 | Kiến trúc hoàn toàn offline | Bảo mật nhà máy, mạng air-gapped, internet không ổn định |
| ADR-004 | Sprint 1 chỉ target PC | Chưa chắc có Snapdragon device, tránh cam kết không chứng minh được |

---

## 4. TEAM & PHÂN CÔNG

### 4.1 Vai trò (4 người)

| Vai trò | Ký hiệu | Trách nhiệm chính |
|---|---|---|
| **Team Lead / System Architect** | TL | Kiến trúc, Pipeline Orchestrator, Tech Spec, Qualcomm research, ADR |
| **ASR & Translation Engineer** | ATE | Whisper ASR, NLLB/M2M100 Translation, VAD, Quantization |
| **Audio & TTS Engineer** | AUD | DeepFilterNet3/RNNoise, Piper TTS, Audio I/O, Incremental Playback |
| **App & Integration Engineer** | APP | UI/UX direction-first, Evaluation Harness (BLEU/WER), provenance, Benchmark UI, reviewer logistics, demo/submission assets |

### 4.2 Thay đổi workload v1 → v2

Evaluation Harness (script BLEU/WER), provenance và Benchmark UI đã được
**chuyển từ ATE sang APP** để giảm tải cho ATE — ATE tập trung vào ASR +
Translation và review metric logic. Auto language detection không nằm trong
critical path; người dùng chọn rõ `VI→KO` hoặc `KO→VI`.

---

## 5. TRẠNG THÁI HIỆN TẠI (Tính đến 27/07/2026)

### 5.1 Đã hoàn thành
- ✅ Đăng ký cuộc thi (form đã điền đầy đủ)
- ✅ PRD v1 — bản đầu tiên
- ✅ PRD v2 — bản cập nhật với scope giảm, ADR, buffer time, milestone gates
- ✅ Review PRD v2 — đã identify 7 vấn đề cần sửa
- ✅ PRD v3 — scope reset theo feedback mentor, tách target khỏi measured evidence
- ✅ Repository foundation — contracts, mock pipeline, bounded segmenter, model manifest/checksum, tests
- ✅ Technical Proposal working draft — bám template Phase 2, còn các trường TBC cần team xác nhận
- ✅ Team operating system — start page, playbook, calendar, four role prompts,
  four active cards, reviewer/gate/handoff rules
- ✅ Gate 2 evaluation foundation implementation — strict JSONL, approved-only
  policy ở CLI và public API, CER/WER, protected tokens, `sacrebleu` adapter,
  Unicode hardening và contract
- ✅ 32/32 repository tests pass; 25/25 evaluation tests pass trên môi trường
  chuẩn bị ngày 27/07/2026

### 5.2 Chưa hoàn thành / Cần làm tiếp

- ❌ **Technical Specification Document bản final** — working draft đã có, cần điền team/deadline và benchmark evidence
- ❌ **PoC trên PC** — pipeline chạy end-to-end
- ❌ **Benchmark** — đo latency, BLEU, WER, CPU, RAM
- ❌ **Demo video** — 2-3 phút minh họa
- ❌ **Prototype trên Snapdragon** — Phase 3 (tháng 8-9)

### 5.3 Timeline còn lại

| Deadline | Việc cần làm |
|---|---|
| **21/08/2026** | Hạn chính thức nộp Technical Proposal Phase 2; team đặt internal deadline 20/08 18:00 |
| **Tháng 8–9/2026** | Xây dựng Prototype chạy trên Snapdragon (Phase 3) |
| **Tháng 10/2026** | Field testing (Phase 4) |
| **Tháng 11/2026** | Chung kết Live Demo (Phase 5) |

---

## 6. KẾT QUẢ REVIEW PRD v2 — 7 VẤN ĐỀ CẦN SỬA

| # | Mức độ | Vấn đề | Hành động đề xuất |
|---|---|---|---|
| 1 | 🔴 Cao | **M2M100-418M có thể kém hơn NLLB cho cặp VN↔KR low-resource.** Lý do "dư thừa 200 ngôn ngữ" không chính xác — NLLB dùng cross-lingual transfer nên dịch low-resource tốt hơn | Đổi default sang NLLB-200-distilled-600M, giữ M2M100 làm fallback nếu OOM |
| 2 | 🔴 Cao | **Không ai trong team biết tiếng Hàn** (chưa xác nhận) — không thể đánh giá chất lượng dịch VN→KR | Tìm external reviewer biết tiếng Hàn; dùng back-translation sanity check; dùng BLEU từ reference corpus (OPUS/Tatoeba) |
| 3 | 🟡 Trung bình | **Thiếu kế hoạch thu thập test data VN↔KR** — 20 câu test ai viết? có từ chuyên ngành manufacturing không? | Thêm task chuẩn bị test sentences Ngày 1-2; chia 10 general + 10 manufacturing domain |
| 4 | 🟡 Trung bình | **Ngày 3 (integration) quá tham vọng** — ghép 4 module trong 1 ngày rủi ro cao | Thêm interface contracts + integration stubs vào Ngày 2; Gate 4 chấp nhận 1 chiều (VN→KR) trước |
| 5 | 🟢 Nhỏ | **Thiếu Definition of Done** cho mỗi module — dễ gây hiểu lầm "xong chưa" | Thêm DoD rõ ràng: module X "done" khi có script chạy được input→output |
| 6 | 🟢 Nhỏ | **Benchmark thiếu baseline comparison** với Google Translate | Thêm bảng so sánh: latency, offline capability, noise handling, data privacy |
| 7 | 🟢 Nhỏ | **Vài lỗi lịch trình**: thiếu task download models Ngày 1; Ngày 6-7 là cuối tuần (cần confirm availability); evaluate.py ownership mơ hồ | Sửa lịch trình cụ thể |

---

## 7. CẤU TRÚC THƯ MỤC DỰ ÁN (LỊCH SỬ)

Sơ đồ cũ phía trên đã được thay bởi package layout thực tế
`src/say_it_for_me/`. Xem `say-it-for-me/README.md` và
`say-it-for-me/docs/team/TEAM_PLAYBOOK.md`; không tạo lại root `audio/`,
`evaluation/` hoặc `pipeline.py`.

---

## 8. GHI CHÚ CHO AI AGENTS

### Ngôn ngữ giao tiếp
- User (team lead) nói **tiếng Việt**.
- Tài liệu kỹ thuật, form đăng ký, Tech Spec nộp bằng **tiếng Anh**.
- PRD nội bộ team viết bằng **tiếng Việt** (có thuật ngữ kỹ thuật tiếng Anh).

### Quy tắc quan trọng
- **Không over-commit:** Sprint 1 chỉ PoC trên PC. Tránh hứa hẹn gì về Snapdragon/Android.
- **Qualcomm AI Hub:** Nói "evaluate as primary toolchain", KHÔNG nói "will compile everything through".
- **Model dịch:** NLLB-200-distilled-600M là Candidate A cho prototype, không còn là cam kết mặc định; phải qua quality/resource/license gate cùng M2M100 hoặc ứng viên bilingual.
- **TTS:** Incremental Playback (dịch xong câu → phát), KHÔNG phải Streaming TTS chunk-by-chunk.
- **Demo:** Gradio web app cho Sprint 1 (không phải Android app).

### Khi hỗ trợ code
- Python là ngôn ngữ chính cho PoC.
- ONNX Runtime là inference engine baseline.
- CTranslate2 cho Translation model.
- Tuân theo layout thực tế trong `say-it-for-me/README.md` và exact paths của
  active card, không dùng sơ đồ lịch sử ở mục 7.
- Mỗi module phải có script standalone chạy được riêng (testable independently).

### Khi viết tài liệu tiếng Anh cho cuộc thi
- Luôn nhấn mạnh 3 keyword: **Edge AI**, **Offline**, **Manufacturing VN-KR**
- Highlight data privacy / security (điểm cộng lớn với giám khảo Qualcomm)
- Nhắc đến Qualcomm AI Hub / Snapdragon NPU (nhà tài trợ muốn nghe)
- Dùng số liệu cụ thể (latency < 3s, model size < 400MB, 100% offline)

---

## 9. CẬP NHẬT PHIÊN 23/07/2026 — BASELINE MỚI

> Mục này **supersede** các ước lượng model/RAM/latency ở mục 3 và các ghi chú cũ nếu có mâu thuẫn. Chi tiết chuẩn nằm trong `PRD_SayItForMe.md`.

### 9.1 Quyết định đã thay đổi

- `< 3 giây` là **target chưa kiểm chứng**, phải báo cáo p50/p95 trên hardware cụ thể.
- Bỏ cam kết RAM `< 2GB` và model tổng `~400MB`; runtime RSS, activation, tokenizer và allocator phải được đo.
- UI dùng lựa chọn rõ `VI→KO` / `KO→VI`; auto language detection ra khỏi critical path.
- Audio capture/denoise contract là **48 kHz**, sau đó resample xuống **16 kHz** cho ASR.
- Chunking theo VAD/silence với queue bounded; mặc định chỉ 1 heavy inference request in-flight để tránh peak RAM.
- NLLB là Candidate A nhưng có license CC-BY-NC và research/non-production caveat; phải có license gate.
- Piper official voices có Vietnamese nhưng không liệt kê Korean; Korean TTS cần checkpoint khác được xác minh.
- QCS6490/RB3 Gen 2 là candidate hardware chính; QCS8550 là performance fallback sau profiling.

### 9.2 Artifact mới

```text
PRD_SayItForMe.md                         # PRD v3 hiện hành
PRD_SayItForMe_v2_archive.md              # Bản cũ được giữ lại
say-it-for-me/
├── README.md
├── docs/
│   ├── technical_proposal_working_draft.md
│   ├── execution_backlog.md
│   ├── evidence_register.md
│   └── adr/
├── models/manifest.example.json
├── src/say_it_for_me/                    # Contracts, orchestrator, model manager, segmenter, mocks
├── scripts/benchmark_mock.py
├── docs/team/                            # Start page, playbook, prompts, cards, handoffs
├── docs/testing/evaluation_contract.md
├── examples/evaluation/                  # NON_EVIDENCE diagnostic fixtures
├── reports/asr/ và reports/nmt/          # Candidate inventory scaffolds
└── tests/                                # 32 tests đang pass; 25 thuộc evaluation
```

### 9.3 Blocker cần team trả lời trước khi final proposal

1. Giờ cutoff chính xác ngày 21/08, format và giới hạn file/page Phase 2.
2. Team name, tên/thế mạnh của 4 thành viên.
3. Thiết bị Snapdragon/RB3/Android đang có trong tay.
4. Baseline PC dùng benchmark.
5. Người review biết tiếng Hàn.
6. Xác nhận phạm vi sử dụng model CC-BY-NC trong cuộc thi.

---

## 10. CẬP NHẬT PHIÊN 27/07/2026 — BƯỚC TIẾP THEO

### 10.1 Bắt đầu ở đâu

Mọi thành viên bắt đầu tại:

`say-it-for-me/docs/team/TEAM_START_HERE.md`

Mỗi phiên AI chỉ dùng:

1. `00_MASTER_PROJECT_PROMPT.md`;
2. đúng một role prompt;
3. đúng một active task card.

Active card hiện đã có exact output paths, command/threshold nghiệm thu,
dependency time, reviewer, gate owner, escalation và handoff.

### 10.2 Trạng thái Gate 2

- APP evaluation foundation: `REVIEW`.
- Handoff sẵn tại
  `say-it-for-me/docs/team/handoffs/APP_evaluation_foundation.md`.
- ATE review scaffold:
  `say-it-for-me/docs/team/handoffs/ATE_evaluation_review.md`.
- Public API và CLI đều áp dụng `approved_only` mặc định.
- Non-approved records chỉ chạy khi bật diagnostic và luôn có policy label.
- Unsafe surrogate/bidi/zero-width bị từ chối bằng structured error.
- `sacrebleu` thật chưa được cài/chạy trong môi trường chuẩn bị; ATE phải xác minh
  version/signature trước khi gate PASS.
- Chưa có 20-pair approved set, Korean review hoặc license approval; vì vậy
  chưa có metric nào đủ điều kiện đưa vào proposal.

### 10.3 Blocker con người duy nhất trước onboarding PASS

`say-it-for-me/docs/team/TEAM_FACTS.md` đang ghi rõ `BLOCKED`/`UNASSIGNED` cho:

1. tên thật và mapping TL/ATE/AUD/APP;
2. availability/unavailable dates;
3. baseline PC và thiết bị Snapdragon/Android/RB3 thực có;
4. Korean reviewer và hai review windows;
5. consent/privacy và license decisions;
6. cutoff/format/page-size/link policy từ BTC.
7. review và tạo initial baseline commit của nested repo; hiện toàn bộ project
   worktree vẫn untracked.

Không agent nào được tự điền các facts này.

### 10.4 Trình tự ngay sau khi có roster

1. TL + APP đóng Gate 0 theo card trước 29/07 12:00.
2. Named APP gửi handoff evaluation trước 29/07 15:00.
3. Named ATE chạy review thực, gồm `sacrebleu`, trước 30/07 11:00.
4. TL quyết định evaluation-foundation gate trước 30/07 12:00.
5. Sau PASS, APP mở card riêng cho traceable 20-pair set; không tái sử dụng
   diagnostic fixture làm evidence.
