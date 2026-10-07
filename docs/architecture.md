# Architecture

```text
Camera (OpenCV)
   ↓  BGR frame
YOLO Detector (ultralytics, yolov8n.pt)
   ↓  [{label, conf, box}]
Reasoning (src/assistant.py)
   ├─ periodic Arabic summary (every N frames)
   ├─ OCR (EasyOCR ar+en) every 3xN frames
   └─ Local VLM (optional, disabled by default)
   ↓  Arabic text
Arabic TTS (Piper, offline .onnx voice)
   ↓  WAV -> speaker
User
   ↑
Preview window (Q to quit) + console log
```

## Modules

| File | Role |
|---|---|
| `src/camera.py` | OpenCV capture |
| `src/detector.py` | YOLOv8 detection |
| `src/ocr_reader.py` | EasyOCR ar/en |
| `src/vlm.py` | Local VLM stub (LLaVA / Moondream2 / Qwen-VL) |
| `src/arabic_tts.py` | Piper offline Arabic speech |
| `src/lidar.py` | Optional LiDAR stub |
| `src/assistant.py` | Fusion loop + Arabic summaries |
| `config.yaml` | All tunables |

## Why offline-first

- No cloud calls in the loop.
- YOLO + EasyOCR + Piper all run locally after one-time downloads.
- VLM is opt-in because 7B models need quantization on 8GB edge devices.
