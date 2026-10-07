"""Local Vision-Language Model stub (offline).

Plug your quantized VLM here: LLaVA / Moondream2 / Qwen-VL.
Disabled by default (vlm.enabled=false) so YOLO+OCR run on 8GB edge devices.
"""
from PIL import Image

class LocalVLM:
    def __init__(self, model_id="", prompt="صف ما تراه في الصورة باختصار."):
        self.model_id = model_id
        self.prompt = prompt
        self.pipe = None
        if model_id:
            # Lazy load to keep startup light on Jetson / Pi.
            # Example:
            # from transformers import pipeline
            # self.pipe = pipeline("image-to-text", model=model_id, device="cuda")
            raise NotImplementedError(
                "Wire your local VLM here (transformers / llama.cpp). "
                f"model_id={model_id}"
            )

    def describe(self, frame) -> str:
        if self.pipe is None:
            return ""
        img = Image.fromarray(frame[:, :, ::-1])  # BGR -> RGB
        out = self.pipe(img, prompt=self.prompt)
        if isinstance(out, list) and out:
            return out[0].get("generated_text", "")
        return str(out)
