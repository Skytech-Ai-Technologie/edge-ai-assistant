"""Edge AI Assistant - entry point (offline multimodal loop)."""
import argparse

def main(camera: int = 0, lang: str = "ar"):
    print(f"Edge AI Assistant starting (camera={camera}, lang={lang})")
    print("TODO: add YOLO / VLM / OCR / Arabic TTS pipeline here.")
    print("Fully offline inference - see README.md")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Edge AI Assistant")
    parser.add_argument("--camera", type=int, default=0)
    parser.add_argument("--lang", type=str, default="ar")
    args = parser.parse_args()
    main(camera=args.camera, lang=args.lang)
