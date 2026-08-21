# VI→KO Real-Inference Demo Evidence

## Status

**BLOCKED — no consented Vietnamese WAV was available in the repository, workspace, or accessible Drive search on 21/08/2026.** No successful ASR transcript, Korean translation, TTS output, quality metric, latency result, offline result, or phone result is recorded here.

The implementation entry point is `python -m say_it_for_me.demo_cli`. It has no mock fallback: a successful run requires a real Vietnamese input and installed ASR/NMT runtimes. The supported demonstrated scope is intentionally only `vi-ko`; Korean TTS remains `NOT_IMPLEMENTED`.

## Command to run when a consented input is supplied

```powershell
$env:PYTHONPATH = "src"
python -m say_it_for_me.demo_cli `
  --direction vi-ko `
  --input samples/demo/vi_demo.wav `
  --asr tiny `
  --nmt m2m100 `
  --output-dir docs/submission/evidence/demo
```

Input requirements: mono, 16 kHz, signed PCM-16 WAV; retain consent/provenance alongside the file. `Whisper Tiny` and `facebook/m2m100_418M` are a **provisional demo baseline selected for footprint and MIT-license risk management**, not a measured quality decision. NLLB remains a research candidate because its CC-BY-NC-4.0 model license needs competition-use review.

## Expected successful artifacts

- `run.json` — environment, command inputs, stage timings, status, and limitation fields.
- `transcript_vi.txt` — real Whisper output only after a successful real-audio run.
- `translation_ko.txt` — real M2M100 output only after a successful run; not Korean-reviewed reference text.

`run.json` currently records a real, reproducible missing-input failure instead of inventing output. Network-disabled verification, phone execution, and Korean TTS are not covered.
