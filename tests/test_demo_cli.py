from __future__ import annotations

import tempfile
import unittest
import wave
from pathlib import Path

from say_it_for_me.demo_cli import load_pcm16_mono_wav


class DemoWavInputTests(unittest.TestCase):
    def _write_wav(self, path: Path, *, channels: int = 1, sample_rate: int = 16_000) -> None:
        with wave.open(str(path), "wb") as writer:
            writer.setnchannels(channels)
            writer.setsampwidth(2)
            writer.setframerate(sample_rate)
            writer.writeframes(b"\x00\x00" * channels * 8)

    def test_loads_mono_pcm16_16khz_audio(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "input.wav"
            self._write_wav(path)
            audio = load_pcm16_mono_wav(path)
        self.assertEqual(audio.sample_rate_hz, 16_000)
        self.assertEqual(audio.channels, 1)
        self.assertEqual(len(audio.samples), 8)

    def test_rejects_stereo_audio(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "stereo.wav"
            self._write_wav(path, channels=2)
            with self.assertRaisesRegex(ValueError, "mono"):
                load_pcm16_mono_wav(path)

    def test_rejects_non_16khz_audio(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "8khz.wav"
            self._write_wav(path, sample_rate=8_000)
            with self.assertRaisesRegex(ValueError, "16 kHz"):
                load_pcm16_mono_wav(path)
