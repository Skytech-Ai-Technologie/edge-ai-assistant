"""YAML config loader with safe defaults."""
from pathlib import Path
import yaml

DEFAULTS = {
    "camera": {"index": 0, "width": 640, "height": 480, "fps": 15},
    "detection": {"model": "yolov8n.pt", "conf": 0.45, "imgsz": 640},
    "ocr": {"enabled": True, "langs": ["ar", "en"], "backend": "easyocr"},
    "vlm": {"enabled": False, "model_id": "", "prompt": "صف ما تراه في الصورة باختصار."},
    "tts": {"lang": "ar", "backend": "piper", "voice_model": "models/ar.onnx", "output_wav": "output.wav"},
    "lidar": {"enabled": False, "port": "/dev/ttyUSB0"},
    "app": {"speak_detections": True, "announce_every_n_frames": 30, "show_preview": True},
}

def load_config(path="config.yaml"):
    cfg = {k: dict(v) for k, v in DEFAULTS.items()}
    p = Path(path)
    if p.exists():
        with open(p, encoding="utf-8") as f:
            user = yaml.safe_load(f) or {}
        for k, v in user.items():
            if k in cfg and isinstance(v, dict):
                cfg[k].update(v)
            else:
                cfg[k] = v
    return cfg
