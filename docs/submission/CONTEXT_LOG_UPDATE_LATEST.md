# Context Log Update — Ready to Paste

UPDATE — 06/08/2026 17:58 ICT

## ĐÃ HOÀN THÀNH

- TEAM_FACTS mới đã được đọc; role ownership đã đồng bộ trong repository.
- Roster đã xác nhận: TL là Team Lead (chưa có tên cá nhân); ATE là Nguyễn Tiến Đạt; AUD là Nguyễn Đăng Gia Đạo; APP là Hà Duy Lộc.
- Đã tạo packet kickoff, rescue plan, và handoff riêng cho ATE/AUD/APP.
- Đã kiểm tra Git diff; `PYTHONPATH=src python -m unittest discover -s tests -v` pass 32/32 tests trong 0.166 s.
- Commit `1eabaf0` — `docs(team): sync confirmed roles and add Phase 2 kickoff handoffs` — đã push thành công lên `origin/tl/g0-operations`.

## TEAM HIỆN TẠI

- TL: Team Lead — tên cá nhân, availability và detailed expertise chưa được cung cấp.
- ATE: Nguyễn Tiến Đạt — ASR, VI→KO NMT, model selection/evaluation, technical evidence.
- AUD: Nguyễn Đăng Gia Đạo — WAV/audio, Korean TTS, microphone/playback, phone/hardware/device evidence.
- APP: Hà Duy Lộc — dataset/evaluator, Korean reviewer coordination, application/demo, proposal package, submission requirements.

## TRẠNG THÁI PROPOSAL/KỸ THUẬT

- Proposal vẫn là evidence-backed working draft: real ASR/NMT/TTS, WAV I/O, offline run, phone profile, latency/RSS và Korean review chưa có evidence mới.
- M1 được giữ là VI→KO real evidence slice; không được dùng mock timing hoặc diagnostic data làm measured claim.

## QUYẾT ĐỊNH MỚI

- Role ownership đã chốt theo ATE/AUD/APP/TL; AI là công cụ hỗ trợ, không phải owner.
- Current rescue deadlines và acceptance criteria trong `docs/team/PHASE2_RESCUE_TASKS_3_MEMBERS.md` thay thế các mốc July đã qua.

## BLOCKER

- Chưa có tên cá nhân/availability TL, phone profile, Korean reviewer, organizer rules, real WAV, model candidate evidence hoặc device measurement.
- Không có Google Docs write connector trong phiên này; TL cần paste update này thủ công vào context log.

## VIỆC MỖI ROLE LÀM TIẾP

- TL: xác nhận thông tin còn thiếu và chốt unblock/scope.
- ATE: ASR candidates, real Vietnamese ASR, rồi VI→KO NMT evidence.
- AUD: phone profile, WAV I/O/10 clips, Korean TTS candidate/evidence.
- APP: dataset clean-up, organizer rules, Korean reviewer, proposal controls.

## 3 HÀNH ĐỘNG TIẾP THEO

1. AUD cung cấp phone profile và WAV input đầu tiên.
2. ATE chạy ASR thật và ghi exact checkpoint/runtime/license.
3. APP xác nhận organizer rules và Korean reviewer.

## FILE ĐÃ THAY ĐỔI

- `docs/team/TEAM_FACTS.md`, `TEAM_START_NOW.md`, rescue plan, kickoff message, three role handoffs, active-card roster labels, and proposal-input owners.
