# Edge AI Assistant

> Offline multimodal AI assistant for real-time visual understanding
> on low-power edge devices.

![license](https://img.shields.io/badge/license-MIT-green) ![offline](https://img.shields.io/badge/inference-fully%20offline-blue) ![jetson](https://img.shields.io/badge/Jetson_Orin_Nano-supported-brightgreen)

[Demo] [Documentation](docs/architecture.md) [Models] [License](LICENSE)

## ✨ Features

- 🎥 Real-time camera understanding
- 👁️ Object detection (YOLOv8, offline)
- 🧠 Local Vision-Language Model (opt-in, quantized)
- 🔤 OCR Arabic + English (EasyOCR, offline)
- 🗣️ Arabic speech output (Piper TTS, offline)
- 📡 Optional LiDAR integration (stub)
- ⚡ Optimized for Jetson Orin Nano 8GB / Pi 5
- 🔒 Fully offline inference

## Architecture

```text
Camera
   ↓
YOLO / Vision Encoder
   ↓
Vision-Language Model (optional)
   ↓
Reasoning + OCR
   ↓
Arabic TTS
   ↓
User
```

Details: [docs/architecture.md](docs/architecture.md) · [docs/hardware.md](docs/hardware.md) · [docs/arabic-tts.md](docs/arabic-tts.md)

## Supported Hardware

| Device | RAM | Status |
|---|---:|---|
| Jetson Orin Nano | 8 GB | ✅ primary |
| Raspberry Pi 5 | 8 GB | ✅ |
| RTX GPU | 8+ GB | ✅ |

## 🚀 Quick Start

```bash
git clone https://github.com/midoo2020/edge-ai-assistant.git
cd edge-ai-assistant
pip install -r requirements.txt
python main.py
# headless: python main.py --no-preview
# config:  edit config.yaml
```

## Project structure

```text
main.py            # entry point
config.yaml        # camera / detection / ocr / vlm / tts tunables
src/
  camera.py        # OpenCV capture
  detector.py      # YOLOv8
  ocr_reader.py    # EasyOCR ar+en
  vlm.py           # local VLM stub
  arabic_tts.py    # Piper offline TTS
  assistant.py     # fusion loop
  lidar.py         # optional LiDAR stub
docs/
  architecture.md
  hardware.md
  arabic-tts.md
```

## License

MIT — see [LICENSE](LICENSE).
