from datetime import datetime
import os
from config import WAKE_WORD, OPENAI_API_KEY, OPENAI_MODEL, SCREENSHOT_DIR
from voice.listener import Listener
from voice.speaker import Speaker
from core.memory import Memory
from core.command_router import CommandRouter
from security.confirmation import confirm
from tools import system, browser, files
from utils.logger import get_logger

log = get_logger("Assistant")

SYSTEM_PROMPT = """You are JARVIS, a helpful Windows desktop AI assistant.
Be concise but natural. You can understand normal human language.
Do not claim an action was completed unless the application actually performed it.
The local tool layer handles computer actions; you handle conversation, reasoning,
clarification, planning, and questions. Never provide instructions for unsafe or
destructive actions unless asked normally. When the user asks to control the PC,
the local router may execute supported safe commands.
"""

class AIChat:
    def __init__(self, memory):
        self.memory = memory
        self.history = []

    def ask(self, text):
        if not OPENAI_API_KEY:
            return self.fallback(text)
        try:
            from openai import OpenAI
            client = OpenAI(api_key=OPENAI_API_KEY)
            context = self.memory.summary()
            messages = [{"role":"system","content":SYSTEM_PROMPT}]
            if context:
                messages.append({"role":"system","content":f"Known user memory: {context}"})
            messages.extend(self.history[-10:])
            messages.append({"role":"user","content":text})
            response = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=messages,
                temperature=0.4,
            )
            answer = response.choices[0].message.content.strip()
            self.history += [{"role":"user","content":text},{"role":"assistant","content":answer}]
            return answer
        except Exception as exc:
            log.exception("AI request failed: %s", exc)
            return self.fallback(text)

    def fallback(self, text):
        t = text.lower()
        if any(x in t for x in ["hello", "hi jarvis", "hey jarvis", "hello jarvis"]):
            name = self.memory.get("name")
            return f"Hello{', ' + name if name else ''}. How can I help?"
        if "your name" in t:
            return "I'm JARVIS, your desktop assistant."
        if "my name" in t and self.memory.get("name"):
            return f"Your name is {self.memory.get('name')}."
        if "thank" in t:
            return "You're welcome."
        return "I can handle supported laptop commands, or you can add an OpenAI API key for full natural-language conversation."

class Jarvis:
    def __init__(self):
        self.listener = Listener()
        self.speaker = Speaker()
        self.memory = Memory()
        self.router = CommandRouter()
        self.ai = AIChat(self.memory)
        self.active = True

    def say(self, text):
        self.speaker.speak(text)

    def execute(self, action, args):
        try:
            if action == "shutdown":
                if confirm("shutdown"):
                    return system.power("shutdown")
                return "Shutdown cancelled."
            if action == "restart":
                if confirm("restart"):
                    return system.power("restart")
                return "Restart cancelled."
            if action == "lock":
                if confirm("lock"):
                    system.lock()
                    return "Locking the computer."
                return "Lock cancelled."
            if action == "screenshot":
                path = SCREENSHOT_DIR / f"screenshot_{datetime.now():%Y%m%d_%H%M%S}.png"
                system.screenshot(path)
                return f"Screenshot saved as {path.name}."
            if action == "status":
                return system.system_status()
            if action == "volume_up":
                return system.set_volume("up")
            if action == "volume_down":
                return system.set_volume("down")
            if action == "mute":
                return system.mute_volume()
            if action == "brightness_up":
                return system.set_brightness("up")
            if action == "brightness_down":
                return system.set_brightness("down")
            if action == "wifi_on":
                return system.wifi("on")
            if action == "wifi_off":
                return system.wifi("off")
            if action == "open_app":
                return system.open_app(args["name"])[1]
            if action == "close_app":
                return system.close_app(args["name"])[1]
            if action == "google":
                return browser.google_search(args["query"])
            if action == "youtube":
                return browser.youtube_search(args["query"])
            if action == "folder":
                return files.open_folder(args["name"])[1]
            if action == "time":
                return datetime.now().strftime("It is %I:%M %p.")
            if action == "date":
                return datetime.now().strftime("Today is %A, %d %B %Y.")
            if action == "chat":
                return self.ai.ask(args.get("text", ""))
            return "I don't know that command yet."
        except Exception as exc:
            log.exception("Action failed: %s", exc)
            return f"I couldn't complete that action: {exc}"

    @staticmethod
    def clean(text):
        return text

    def handle(self, text):
        action, args = self.router.route(text)
        if action == "chat":
            return self.ai.ask(text)
        return self.execute(action, args)

    def run(self):
        self.say("JARVIS online. Say Jarvis followed by a command, or say exit to stop.")
        while self.active:
            text = self.listener.listen()
            if not text:
                continue

            if text in {"exit", "quit", "goodbye", "stop jarvis", "shutdown jarvis"}:
                self.say("Going offline. Goodbye.")
                break

            # Wake-word mode: accept "jarvis ..." or direct command for convenience.
            if WAKE_WORD in text:
                text = text.split(WAKE_WORD, 1)[1].strip() or "hello"
            elif text not in {"hello", "hi", "hey"}:
                # Keep direct commands working during setup/testing.
                pass

            response = self.handle(text)
            self.say(response)
