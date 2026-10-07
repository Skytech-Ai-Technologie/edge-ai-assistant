"""YOLO object detection (Ultralytics). Offline after model download."""
try:
    from ultralytics import YOLO
except ImportError:  # allow import without ultralytics for testing
    YOLO = None

class Detector:
    def __init__(self, model="yolov8n.pt", conf=0.45, imgsz=640):
        if YOLO is None:
            raise RuntimeError("ultralytics not installed. pip install ultralytics")
        self.model = YOLO(model)
        self.conf = conf
        self.imgsz = imgsz

    def detect(self, frame):
        """Return list of {label, conf, box}."""
        results = self.model.predict(frame, conf=self.conf, imgsz=self.imgsz, verbose=False)
        out = []
        for r in results:
            for b in r.boxes:
                cls = int(b.cls[0])
                label = r.names.get(cls, str(cls))
                out.append({
                    "label": label,
                    "conf": float(b.conf[0]),
                    "box": [float(x) for x in b.xyxy[0].tolist()],
                })
        return out
