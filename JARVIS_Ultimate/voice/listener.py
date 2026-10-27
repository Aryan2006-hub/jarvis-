import speech_recognition as sr
from config import LANGUAGE
from utils.logger import get_logger

log = get_logger("Listener")

class Listener:
    def __init__(self, language=LANGUAGE):
        self.recognizer = sr.Recognizer()
        self.language = language
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        self.recognizer.non_speaking_duration = 0.4

    def listen(self, timeout=6, phrase_time_limit=12):
        try:
            with sr.Microphone() as source:
                print("\nListening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.35)
                audio = self.recognizer.listen(
                    source, timeout=timeout, phrase_time_limit=phrase_time_limit
                )
            text = self.recognizer.recognize_google(audio, language=self.language).strip().lower()
            print(f"YOU: {text}")
            return text
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError as exc:
            log.error("Speech service error: %s", exc)
            return None
        except Exception as exc:
            log.exception("Microphone error: %s", exc)
            return None
