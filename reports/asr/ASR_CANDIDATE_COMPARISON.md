# ASR Candidate Comparison

> **Owner:** ATE — Nguyễn Tiến Đạt  
> **Status:** INVENTORY_COMPLETE — awaiting real WAV for evaluation  
> **Date:** 19/08/2026

## Candidates

| Field | Whisper Tiny | Whisper Base |
|:------|:-------------|:-------------|
| Exact checkpoint | `openai/whisper-tiny` | `openai/whisper-base` |
| HuggingFace URL | https://huggingface.co/openai/whisper-tiny | https://huggingface.co/openai/whisper-base |
| Parameters | 39M | 74M |
| Architecture | Encoder-decoder Transformer (4 encoder + 4 decoder layers, d=384) | Encoder-decoder Transformer (6 encoder + 6 decoder layers, d=512) |
| Runtime | faster-whisper (CTranslate2 backend) | faster-whisper (CTranslate2 backend) |
| CTranslate2 checkpoint | Auto-downloaded by faster-whisper from `Systran/faster-whisper-tiny` | Auto-downloaded by faster-whisper from `Systran/faster-whisper-base` |
| Precision / compute type | int8 on CPU; float16 on CUDA | int8 on CPU; float16 on CUDA |
| Artifact size (float16) | ~75 MB | ~142 MB |
| Artifact size (int8) | ~40 MB | ~75 MB |
| VRAM (GPU) | ~1 GB | ~1 GB |
| RAM (CPU int8) | ~273 MB | ~388 MB |
| Vietnamese support | Yes — multilingual model covers vi | Yes — multilingual model covers vi |
| Korean support | Yes — multilingual model covers ko | Yes — multilingual model covers ko |
| License | MIT | MIT |
| License URL | https://github.com/openai/whisper/blob/main/LICENSE | https://github.com/openai/whisper/blob/main/LICENSE |
| Paper | Radford et al., "Robust Speech Recognition via Large-Scale Weak Supervision", 2022 | Same |
| Input requirements | Mono 16 kHz PCM float32 | Mono 16 kHz PCM float32 |
| Competition use | Permitted (MIT) | Permitted (MIT) |

## Selection rationale

Both candidates share the same codebase, license, and runtime. The tradeoff is accuracy vs. latency/size:

- **Whisper Tiny**: fastest inference, smallest footprint, viable for phone deployment. Expected higher WER on noisy Vietnamese.
- **Whisper Base**: ~2x larger, measurably better WER on multilingual benchmarks. Still fits in ~1 GB RAM.

## Status

Neither candidate is selected as baseline yet. Selection requires:

1. Real Vietnamese ASR output on WAV supplied by AUD.
2. CER/WER comparison on shared evaluation sentences.
3. Latency measurement on target environment (PC first, phone if feasible).
4. TL approval per ADR-003 evidence gate.

## Blockers

| Blocker | Impact | Mitigation |
|:--------|:-------|:-----------|
| No WAV from AUD yet | Cannot run real inference | Proceed with inventory; run as soon as WAV arrives |
| Phone runtime untested | Cannot claim phone latency | Label all results as PC until phone evidence exists |

## Evidence sources

- OpenAI Whisper model card: https://github.com/openai/whisper/blob/main/model-card.md
- faster-whisper repository: https://github.com/SYSTRAN/faster-whisper
- HuggingFace model pages (linked above)
