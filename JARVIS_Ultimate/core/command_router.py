import re
from datetime import datetime

class CommandRouter:
    def route(self, text):
        t = text.lower().strip()

        if any(x in t for x in ["shutdown", "shut down", "turn off computer"]):
            return ("shutdown", {})
        if any(x in t for x in ["restart computer", "restart the computer", "reboot"]):
            return ("restart", {})
        if "lock computer" in t or t == "lock":
            return ("lock", {})
        if "screenshot" in t or "screen shot" in t:
            return ("screenshot", {})
        if "system status" in t or "cpu usage" in t or "ram usage" in t:
            return ("status", {})
        if "volume up" in t or "increase volume" in t:
            return ("volume_up", {})
        if "volume down" in t or "decrease volume" in t:
            return ("volume_down", {})
        if "mute" in t:
            return ("mute", {})
        if "brightness up" in t or "increase brightness" in t:
            return ("brightness_up", {})
        if "brightness down" in t or "decrease brightness" in t:
            return ("brightness_down", {})
        if "turn wifi on" in t or "enable wifi" in t:
            return ("wifi_on", {})
        if "turn wifi off" in t or "disable wifi" in t:
            return ("wifi_off", {})

        m = re.search(r"(?:open|launch|start)\s+(notepad|calculator|calc|paint|explorer|file explorer|cmd|terminal)$", t)
        if m:
            return ("open_app", {"name": m.group(1)})

        m = re.search(r"(?:close|quit)\s+(notepad|calculator|calc|paint|chrome|edge|firefox)$", t)
        if m:
            return ("close_app", {"name": m.group(1)})

        m = re.search(r"(?:search google for|google)\s+(.+)", t)
        if m:
            return ("google", {"query": m.group(1)})

        m = re.search(r"(?:search youtube for|youtube)\s+(.+)", t)
        if m:
            return ("youtube", {"query": m.group(1)})

        m = re.search(r"(?:open folder|open)\s+(downloads|documents|desktop|pictures)$", t)
        if m and ("folder" in t or m.group(1) in {"downloads","documents","desktop","pictures"}):
            return ("folder", {"name": m.group(1)})

        if t in {"time", "what time is it", "tell me the time"}:
            return ("time", {})

        if t in {"date", "what is today's date", "what's the date"}:
            return ("date", {})

        return ("chat", {"text": text})
