"""Offline Arabic TTS via Piper (no internet needed after voice download).

Install voice model once, e.g.:
  https://github.com/rhasspy/piper/releases
  -> Arabic voice -> models/ar.onnx + models/ar.onnx.json

Fallback: print text if piper not available.
"""
import subprocess
from pathlib import Path

class ArabicTTS:
    def __init__(self, voice_model="models/ar.onnx", output_wav="output.wav"):
        self.voice_model = Path(voice_model)
        self.output_wav = Path(output_wav)

    def speak(self, text_ar: str):
        text_ar = text_ar.strip()
        if not text_ar:
            return
        if not self.voice_model.exists():
            print(f"[TTS-ar] {text_ar} (no voice model at {self.voice_model}, skipping audio)")
            return
        try:
            # echo text | piper --model ar.onnx --output_file output.wav
            p1 = subprocess.Popen(["echo", text_ar], stdout=subprocess.PIPE)
            subprocess.run(
                ["piper", "--model", str(self.voice_model),
                 "--output_file", str(self.output_wav)],
                stdin=p1.stdout, check=True,
            )
            # play offline: aplay / paplay / ffplay depending on device
            for player in (["aplay", str(self.output_wav)], ["paplay", str(self.output_wav)]):
                try:
                    subprocess.run(player, check=True)
                    break
                except FileNotFoundError:
                    continue
        except Exception as e:
            print(f"[TTS error] {e}\n[TTS-ar] {text_ar}")
