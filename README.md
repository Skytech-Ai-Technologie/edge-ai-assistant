# Edge AI Assistant

> Offline multimodal AI assistant for real-time visual understanding
> on low-power edge devices.

[Demo] [Documentation] [Paper] [Models] [License]

## ✨ Features

- 🎥 Real-time camera understanding
- 👁️ Object detection
- 🧠 Local Vision-Language Model
- 🔤 OCR
- 🗣️ Arabic speech output
- 📡 Optional LiDAR integration
- ⚡ Optimized for Jetson Orin Nano
- 🔒 Fully offline inference

## Architecture

```text
Camera
   ↓
YOLO / Vision Encoder
   ↓
Vision-Language Model
   ↓
Reasoning
   ↓
Arabic TTS
   ↓
User
```

## Supported Hardware

| Device | RAM | Status |
|---|---:|---|
| Jetson Orin Nano | 8 GB | ✅ |
| Raspberry Pi 5 | 8 GB | ✅ |
| RTX GPU | 8+ GB | ✅ |

## 🚀 Quick Start

```bash
git clone https://github.com/midoo2020/edge-ai-assistant.git
cd edge-ai-assistant
pip install -r requirements.txt
python main.py
```
