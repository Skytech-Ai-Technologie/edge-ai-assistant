"""OCR: EasyOCR (offline) with Tesseract fallback."""
class OCRReader:
    def __init__(self, langs=("ar", "en"), backend="easyocr"):
        self.backend = backend
        self.reader = None
        if backend == "easyocr":
            try:
                import easyocr
                self.reader = easyocr.Reader(list(langs), gpu=False)
            except ImportError as e:
                raise RuntimeError("easyocr not installed. pip install easyocr") from e

    def read(self, frame):
        """Return list of recognized strings."""
        if self.backend == "easyocr" and self.reader:
            import cv2
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            results = self.reader.readtext(gray)
            return [t[1] for t in results if t[1].strip()]
        else:  # tesseract fallback
            try:
                import pytesseract
                from PIL import Image
                import cv2
                text = pytesseract.image_to_string(
                    Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)),
                    lang="+".join(["ara", "eng"]),
                )
                return [l.strip() for l in text.splitlines() if l.strip()]
            except ImportError as e:
                raise RuntimeError("pytesseract not installed.") from e
