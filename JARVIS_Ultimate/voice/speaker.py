import pyttsx3
from config import VOICE_RATE, VOICE_INDEX
from utils.logger import get_logger

log = get_logger("Speaker")

class Speaker:
    def __init__(self):
        self.rate = VOICE_RATE
        self.voice_index = VOICE_INDEX

    def speak(self, text: str):
        if not text:
            return
        text = str(text)
        print(f"JARVIS: {text}")
        engine = None
        try:
            engine = pyttsx3.init("sapi5")
            voices = engine.getProperty("voices")
            if voices:
                index = min(max(self.voice_index, 0), len(voices) - 1)
                engine.setProperty("voice", voices[index].id)
            engine.setProperty("rate", self.rate)
            engine.setProperty("volume", 1.0)
            engine.say(text)
            engine.runAndWait()
        except Exception as exc:
            log.exception("TTS failed: %s", exc)
        finally:
            if engine:
                try:
                    engine.stop()
                except Exception:
                    pass
