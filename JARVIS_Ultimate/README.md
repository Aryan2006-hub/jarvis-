# JARVIS Ultimate

A modular Windows desktop voice assistant built in Python.

## What is included

- 🎙️ Speech recognition + SAPI5 text-to-speech
- 🧠 Optional OpenAI-powered natural conversation
- 💬 Conversation history during the current session
- 🧠 Persistent simple memory (`data/memory.json`)
- 🖥️ Windows controls: apps, volume, brightness, Wi-Fi, screenshots, lock, shutdown/restart
- 🌐 Google and YouTube search
- 🔎 Optional web-result search through DDGS
- 🔐 Confirmation before destructive actions
- 🧩 Modular architecture
- 🧪 Basic router test
- 📦 GitHub-friendly `.env` and `.gitignore`

## Important

This project is intentionally **not** an arbitrary shell executor. It only exposes predefined system actions.

For full AI conversation, add an OpenAI API key. Without one, JARVIS still works as a local command assistant and uses a small offline fallback conversation layer.

## Windows setup

Open PowerShell inside the folder containing `main.py`:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Create `.env` from `.env.example`.

Then:

```powershell
python main.py
```

## If your terminal opens in the wrong folder

If the project is nested like:

`Downloads\JARVIS_Professional\JARVIS_Ultimate`

run:

```powershell
cd .\JARVIS_Ultimate
python main.py
```

## Example commands

Say:

- "Jarvis, open notepad"
- "Jarvis, increase volume"
- "Jarvis, take a screenshot"
- "Jarvis, what's my system status?"
- "Jarvis, search Google for Python decorators"
- "Jarvis, search YouTube for C++ recursion"
- "Jarvis, open Downloads"
- "Jarvis, what's the time?"
- "Jarvis, lock the computer"

## AI setup

Put these in `.env`:

```text
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-5.6-mini
```

Never commit `.env` to GitHub.

## Project structure

```text
JARVIS_Ultimate/
├── main.py
├── config.py
├── requirements.txt
├── .env.example
├── core/
│   ├── assistant.py
│   ├── command_router.py
│   └── memory.py
├── voice/
│   ├── listener.py
│   └── speaker.py
├── tools/
│   ├── browser.py
│   ├── files.py
│   ├── system.py
│   └── weather.py
├── security/
│   └── confirmation.py
├── utils/
│   └── logger.py
├── data/
└── tests/
```

## Roadmap

The architecture is ready to extend with a GUI, streaming AI responses, richer memory, better wake-word detection, browser automation, calendar/email integrations, and a plugin/tool registry.

## Optional GUI

Run `python gui.py` for a desktop chat interface. Voice mode remains `python main.py`.
