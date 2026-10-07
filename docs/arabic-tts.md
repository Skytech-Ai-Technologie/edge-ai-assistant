# Arabic TTS (offline)

We use [Piper TTS](https://github.com/rhasspy/piper) — fast, offline, Arabic voices available.

## 1. Install

```bash
pip install piper-tts
sudo apt install -y alsa-utils  # for aplay on Jetson/Pi
```

## 2. Download an Arabic voice

From Piper releases, grab e.g. `ar_JO-kareem-medium.onnx` + `.onnx.json`,
place under `models/`:

```bash
mkdir -p models
mv ~/Downloads/ar*.onnx* models/
```

Update `config.yaml`:

```yaml
tts:
  voice_model: "models/ar_JO-kareem-medium.onnx"
```

## 3. Test

```bash
echo "مرحبا، أنا مساعدك البصري." | piper --model models/ar_JO-kareem-medium.onnx --output_file output.wav
aplay output.wav
```

If no voice model is present, the app prints `[TTS-ar] ...` and continues without audio.
