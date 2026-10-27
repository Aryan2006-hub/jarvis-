import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

LANGUAGE = os.getenv("JARVIS_LANGUAGE", "en-IN")
WAKE_WORD = os.getenv("JARVIS_WAKE_WORD", "jarvis")
VOICE_RATE = int(os.getenv("JARVIS_VOICE_RATE", "165"))
VOICE_INDEX = int(os.getenv("JARVIS_VOICE_INDEX", "0"))
REQUIRE_CONFIRMATION = os.getenv("JARVIS_REQUIRE_CONFIRMATION", "true").lower() == "true"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6-mini")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")

DATA_DIR = ROOT / "data"
LOG_DIR = ROOT / "logs"
SCREENSHOT_DIR = DATA_DIR / "screenshots"
MEMORY_FILE = DATA_DIR / "memory.json"

for folder in (DATA_DIR, LOG_DIR, SCREENSHOT_DIR):
    folder.mkdir(parents=True, exist_ok=True)
