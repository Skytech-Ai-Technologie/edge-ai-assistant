"""Main assistant loop: camera -> YOLO -> OCR/VLM -> Arabic TTS."""
import cv2
from .camera import Camera
from .detector import Detector
from .ocr_reader import OCRReader
from .arabic_tts import ArabicTTS

AR_LABELS = {
    "person": "شخص", "car": "سيارة", "chair": "كرسي", "bottle": "قارورة",
    "cup": "كوب", "book": "كتاب", "laptop": "حاسوب", "phone": "هاتف",
    "dog": "كلب", "cat": "قط",
}

class Assistant:
    def __init__(self, cfg):
        c = cfg["camera"]
        self.camera = Camera(c["index"], c["width"], c["height"], c["fps"])
        d = cfg["detection"]
        self.detector = Detector(d["model"], d["conf"], d["imgsz"])
        self.ocr = OCRReader(tuple(cfg["ocr"]["langs"])) if cfg["ocr"]["enabled"] else None
        self.tts = ArabicTTS(cfg["tts"]["voice_model"], cfg["tts"]["output_wav"])
        self.vlm = None
        if cfg["vlm"]["enabled"] and cfg["vlm"]["model_id"]:
            from .vlm import LocalVLM
            self.vlm = LocalVLM(cfg["vlm"]["model_id"], cfg["vlm"]["prompt"])
        self.cfg = cfg
        self.frame_id = 0

    def describe_detections_ar(self, dets):
        if not dets:
            return "لا أرى شيئا واضحا."
        names = []
        for x in dets[:5]:
            label = x["label"]
            names.append(AR_LABELS.get(label, label))
        return "أرى: " + "، ".join(names) + "."

    def run(self):
        app = self.cfg["app"]
        print("Running - press Q to quit.")
        while True:
            frame = self.camera.read()
            if frame is None:
                break
            self.frame_id += 1
            dets = []
            try:
                dets = self.detector.detect(frame)
            except Exception as e:
                print(f"[detect] {e}")
            # draw boxes
            for x in dets:
                x1, y1, x2, y2 = map(int, x["box"])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, x["label"], (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            # periodic Arabic announcement
            if self.frame_id % app["announce_every_n_frames"] == 0:
                msg = self.describe_detections_ar(dets)
                if self.ocr and self.frame_id % (app["announce_every_n_frames"] * 3) == 0:
                    try:
                        texts = self.ocr.read(frame)
                        if texts:
                            msg += " نص مقروء: " + "، ".join(texts[:3])
                    except Exception as e:
                        print(f"[ocr] {e}")
                if self.vlm:
                    try:
                        extra = self.vlm.describe(frame)
                        if extra:
                            msg += " " + extra
                    except Exception as e:
                        print(f"[vlm] {e}")
                print(msg)
                if app["speak_detections"]:
                    self.tts.speak(msg)
            if app["show_preview"]:
                cv2.imshow("Edge AI Assistant", frame)
                if cv2.waitKey(1) & 0xFF in (ord("q"), ord("Q")):
                    break
        self.camera.release()
        cv2.destroyAllWindows()
