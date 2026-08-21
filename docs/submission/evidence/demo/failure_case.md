# Reproducible Failure Case — Missing Consented Audio

The demo CLI was executed with the expected path `samples/demo/vi_demo.wav`. No such file exists in the repository because no consented Vietnamese WAV was supplied. The generated `run.json` records the exact `FileNotFoundError` at `input_validation`.

This is a real failure artifact, not ASR or NMT evidence. It establishes that the CLI fails explicitly before model loading rather than silently substituting mock audio or mock text.
