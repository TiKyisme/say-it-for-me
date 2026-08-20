# NMT Candidate Comparison — VI→KO

> **Owner:** ATE — Nguyễn Tiến Đạt  
> **Status:** INVENTORY_COMPLETE — awaiting real ASR transcript for evaluation  
> **Date:** 19/08/2026

## Candidates

| Field | NLLB-200-distilled-600M | M2M100-418M |
|:------|:------------------------|:------------|
| Exact checkpoint | `facebook/nllb-200-distilled-600M` | `facebook/m2m100_418M` |
| HuggingFace URL | https://huggingface.co/facebook/nllb-200-distilled-600M | https://huggingface.co/facebook/m2m100_418M |
| Parameters | 600M | 418M |
| Architecture | Encoder-decoder Transformer (dense, distilled from 3.3B) | Encoder-decoder Transformer (12 enc + 12 dec, d=1024) |
| Runtime | transformers (PyTorch) | transformers (PyTorch) |
| Precision | float32 (CPU) / float16 (CUDA) | float32 (CPU) / float16 (CUDA) |
| Artifact size | ~2.3 GB (safetensors) | ~1.8 GB (safetensors) |
| Vietnamese lang code | `vie_Latn` | `vi` |
| Korean lang code | `kor_Hang` | `ko` |
| VI supported | Yes | Yes |
| KO supported | Yes | Yes |
| Number of languages | 200 | 100 |
| License | **CC-BY-NC-4.0** | **MIT** |
| License URL | https://huggingface.co/facebook/nllb-200-distilled-600M (model card) | https://huggingface.co/facebook/m2m100_418M (model card) |
| Paper | NLLB Team et al., "No Language Left Behind", 2022 | Fan et al., "Beyond English-Centric Multilingual Machine Translation", 2020 |
| Competition use | **REQUIRES TL REVIEW** — NC clause may restrict commercial/competition use | Permitted (MIT) |
| Phone feasibility | ~2.3 GB model + ~1.5 GB runtime RAM — tight for phone | ~1.8 GB model + ~1.2 GB runtime RAM — more feasible |

## License risk assessment

| Candidate | License | Risk |
|:----------|:--------|:-----|
| NLLB-200 distilled 600M | CC-BY-NC-4.0 | The "NonCommercial" clause may prohibit use in a competition submission if the competition has commercial intent. **TL must decide.** |
| M2M100-418M | MIT | No restriction. Safe for any use. |

## Quality expectations

- NLLB-200 was specifically trained with low-resource language pairs in mind and is expected to produce better VI→KO quality.
- M2M100-418M is older (2020) and smaller but has no license restriction.
- Both need real evaluation on project sentences before any quality claim.

## Status

Neither candidate is selected as baseline yet. Selection requires:

1. Real Vietnamese text from ASR stage.
2. Korean translation output on shared evaluation sentences.
3. chrF++ / sacreBLEU comparison.
4. License decision from TL (especially NLLB NC clause).
5. TL approval per ADR-003 evidence gate.

## Blockers

| Blocker | Impact | Mitigation |
|:--------|:-------|:-----------|
| NLLB license NC clause | May disqualify from competition | M2M100 as MIT fallback |
| No real ASR transcript yet | Cannot run end-to-end | Run NMT standalone on sample Vietnamese text first |
| Phone RAM ~2-3 GB for either model | May not fit phone | CTranslate2 conversion or quantization as future P1 |

## Evidence sources

- NLLB paper: https://arxiv.org/abs/2207.04672
- M2M100 paper: https://arxiv.org/abs/2010.11125
- HuggingFace model pages (linked above)
