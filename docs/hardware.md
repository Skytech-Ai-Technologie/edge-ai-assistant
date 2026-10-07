# Hardware setup

## Jetson Orin Nano 8GB (primary target)

1. Flash JetPack 6, enable MAXN power mode.
2. Install system deps:
   ```bash
   sudo apt update && sudo apt install -y python3-pip libopenblas-dev libjpeg-dev
   ```
3. Install torch per NVIDIA Jetson guide (CUDA), then:
   ```bash
   pip install -r requirements.txt
   ```
4. Use `yolov8n.pt` or TensorRT-exported `yolov8n.engine` for best FPS.
5. Run headless if needed: `python main.py --no-preview`

## Raspberry Pi 5 8GB

- Use `yolov8n.pt` at 640px, `fps: 10-15` in `config.yaml`.
- EasyOCR on CPU is slow — run OCR every 90 frames.
- Piper TTS works fine offline.

## RTX GPU laptop / desktop

- Install CUDA torch, then `pip install -r requirements.txt`.
- Can enable `vlm.enabled: true` with a quantized 7B model.

## Tuning

- `detection.conf`: 0.35-0.5
- `app.announce_every_n_frames`: 30 (~2s at 15fps)
- `camera.width/height`: 640x480 is the sweet spot for edge.
