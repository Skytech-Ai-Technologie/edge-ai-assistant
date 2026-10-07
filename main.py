"""Edge AI Assistant - entry point (offline multimodal loop)."""
import argparse
from src.config import load_config
from src.assistant import Assistant

def main():
    ap = argparse.ArgumentParser(description="Edge AI Assistant (offline)")
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--camera", type=int, default=None)
    ap.add_argument("--no-preview", action="store_true")
    args = ap.parse_args()

    cfg = load_config(args.config)
    if args.camera is not None:
        cfg["camera"]["index"] = args.camera
    if args.no_preview:
        cfg["app"]["show_preview"] = False

    Assistant(cfg).run()

if __name__ == "__main__":
    main()
