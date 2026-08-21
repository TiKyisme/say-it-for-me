# Public-Licensed Diagnostic Audio Search Record

Date: 21/08/2026

## Result

**No clip was added.** The real demo remains blocked on a valid Vietnamese speech
input. This record prevents the missing-input result from being misrepresented as
an inference result.

## Authoritative source checked

Mozilla Data Collective lists **Common Voice Scripted Speech 26.0 — Vietnamese**
as Vietnamese ASR data in MP3 format under **CC0-1.0**:

- https://commonvoice.mozilla.org/data
- https://dev.datacollective.mozillafoundation.org/datasets/cmflnn484oaiy1nwkq2dp76ig

The source is appropriate in principle for a public-licensed diagnostic input;
it must be labelled **PUBLIC-LICENSED DIAGNOSTIC AUDIO**, never team-recorded
audio. During the deadline search, the environment could not obtain a single
identifiable audio clip and its matching transcript/provenance without a
dataset-access/download flow. The full Vietnamese release is approximately
461.86 MB and is MP3, not a direct ready-to-run WAV sample.

## Required conversion if an authorised clip is obtained

Record the source URL, dataset release, clip filename, associated transcript,
licence and download date. Convert the original MP3 only with a reproducible
command such as:

```powershell
ffmpeg -i <original.mp3> -ac 1 -ar 16000 -c:a pcm_s16le <diagnostic_vi.wav>
```

Then record that the resulting file is mono, 16 kHz, signed PCM-16 WAV before
using `python -m say_it_for_me.demo_cli`. No conversion or audio file was
created in this closeout pass.
