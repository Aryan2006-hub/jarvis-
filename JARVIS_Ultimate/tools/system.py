import os
import subprocess
import ctypes
from pathlib import Path
import psutil
import pyautogui

APP_ALIASES = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "calc": "calc.exe",
    "paint": "mspaint.exe",
    "explorer": "explorer.exe",
    "file explorer": "explorer.exe",
    "cmd": "cmd.exe",
    "terminal": "wt.exe",
}

def open_app(name):
    name = name.lower().strip()
    exe = APP_ALIASES.get(name)
    if not exe:
        return False, f"I don't have a safe app shortcut for {name}."
    try:
        subprocess.Popen([exe], shell=False)
        return True, f"Opening {name}."
    except Exception as exc:
        return False, f"I couldn't open {name}: {exc}"

def close_app(name):
    name = name.lower().strip().replace(".exe", "")
    safe = {"notepad", "calc", "calculator", "mspaint", "paint", "chrome", "msedge", "firefox"}
    if name not in safe:
        return False, "For safety, I can only close selected common apps."
    exe = {"calculator":"CalculatorApp.exe","calc":"CalculatorApp.exe",
           "paint":"mspaint.exe","chrome":"chrome.exe","msedge":"msedge.exe",
           "firefox":"firefox.exe","notepad":"notepad.exe"}.get(name, name + ".exe")
    os.system(f'taskkill /IM "{exe}" /F >nul 2>&1')
    return True, f"Closed {name} if it was running."

def system_status():
    cpu = psutil.cpu_percent(interval=0.4)
    ram = psutil.virtual_memory()
    battery = psutil.sensors_battery()
    batt = f"{battery.percent:.0f} percent" if battery else "not available"
    return f"CPU is at {cpu:.0f} percent, memory usage is {ram.percent:.0f} percent, battery is {batt}."

def set_volume(direction):
    # Windows media keys: reliable and does not require admin rights.
    key = "volumeup" if direction == "up" else "volumedown"
    pyautogui.press(key, presses=5, interval=0.04)
    return f"Volume turned {direction}."

def mute_volume():
    pyautogui.press("volumemute")
    return "Volume toggled mute."

def set_brightness(direction):
    try:
        import screen_brightness_control as sbc
        current = sbc.get_brightness(display=0)
        current = current[0] if isinstance(current, list) else current
        step = 10 if direction in {"up", "down"} else 0
        value = max(0, min(100, current + (step if direction == "up" else -step)))
        sbc.set_brightness(value, display=0)
        return f"Brightness set to {value} percent."
    except Exception as exc:
        return f"Brightness control is unavailable on this display: {exc}"

def wifi(action):
    if action == "on":
        os.system('netsh interface set interface name="Wi-Fi" admin=enabled')
        return "Wi-Fi enabled."
    if action == "off":
        os.system('netsh interface set interface name="Wi-Fi" admin=disabled')
        return "Wi-Fi disabled."
    out = subprocess.run(["netsh","wlan","show","interfaces"], capture_output=True, text=True, errors="ignore").stdout
    return out[:1500] if out else "I couldn't read Wi-Fi status."

def screenshot(path):
    image = pyautogui.screenshot()
    image.save(path)
    return str(path)

def lock():
    ctypes.windll.user32.LockWorkStation()

def power(action):
    if action == "shutdown":
        subprocess.Popen(["shutdown", "/s", "/t", "10"])
    elif action == "restart":
        subprocess.Popen(["shutdown", "/r", "/t", "10"])
    return f"{action.title()} scheduled in 10 seconds."
