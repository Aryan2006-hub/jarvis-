# 🤖 JARVIS Ultimate — AI Voice Assistant

<p align="center">
  <strong>Your Personal AI-Powered Desktop Assistant</strong>
</p>

<p align="center">
  A modular Windows desktop voice assistant built with Python, designed to interact with your computer, understand commands, speak responses, and provide AI-powered conversations.
</p>

---

## 🚀 About the Project

**JARVIS Ultimate** is a Python-based desktop voice assistant inspired by intelligent virtual assistants. It combines speech recognition, text-to-speech, AI-powered conversations, persistent memory, and Windows system controls in one application.

JARVIS can listen to voice commands, respond through speech, perform predefined computer operations, and help with everyday tasks through a modular and extensible architecture.

## ✨ Features

- 🎙️ **Voice Interaction** — Speech recognition and text-to-speech responses.
- 🧠 **AI Conversations** — Optional OpenAI-powered natural language responses.
- 💾 **Persistent Memory** — Stores simple memory locally between sessions.
- 🖥️ **System Controls** — Supports predefined actions for applications, volume, brightness, Wi-Fi, screenshots, and power options.
- 🌐 **Web Search** — Search Google and YouTube using commands.
- 📂 **File & Folder Access** — Open supported local files and folders.
- 🔐 **Safety Confirmations** — Requests confirmation before destructive system actions.
- 💬 **Desktop GUI** — Includes a Tkinter-based chat interface.
- 🔊 **Customizable Voice** — Configure language, speech rate, and voice settings.
- 🧩 **Modular Architecture** — Organized into separate components for voice, tools, security, and assistant logic.
- 📴 **Offline Fallback** — Basic command handling and fallback conversation functionality without an OpenAI API key.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| SpeechRecognition | Voice input |
| PyAudio | Microphone input |
| pyttsx3 | Text-to-speech |
| Tkinter | Desktop GUI |
| OpenAI API | Optional AI conversations |
| psutil | System information and processes |
| PyAutoGUI | Desktop automation |
| Requests | HTTP requests |
| python-dotenv | Environment configuration |
| DDGS | Optional web-result search |

## 📁 Project Structure

```text
JARVIS_Ultimate/
├── main.py
├── gui.py
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

## ⚙️ Installation & Setup

### Prerequisites

- Windows 10 or Windows 11
- Python installed and added to PATH
- A working microphone for voice interaction
- An OpenAI API key for optional AI-powered conversations

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd JARVIS_Ultimate
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a Virtual Environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root using `.env.example` as a template.

Example configuration:

```env
JARVIS_LANGUAGE=en-IN
JARVIS_WAKE_WORD=jarvis
JARVIS_VOICE_RATE=165
JARVIS_VOICE_INDEX=0
JARVIS_REQUIRE_CONFIRMATION=true

OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5.6-mini
OPENWEATHER_API_KEY=
```

Replace the placeholder API key with your own key if you want to enable the corresponding AI features.

**Important:** Never commit your `.env` file or expose API keys publicly.

### 5. Run JARVIS

**Voice assistant:**

```bash
python main.py
```

**Desktop chat interface:**

```bash
python gui.py
```

## 💬 Example Commands

Try commands such as:

- "Jarvis, open Notepad."
- "Jarvis, increase volume."
- "Jarvis, take a screenshot."
- "Jarvis, what's my system status?"
- "Jarvis, search Google for Python decorators."
- "Jarvis, search YouTube for C++ recursion."
- "Jarvis, open Downloads."
- "Jarvis, what's the time?"
- "Jarvis, lock the computer."

Available commands depend on the implemented command handlers and your system configuration.

## 🔒 Security & Privacy

JARVIS is designed to use predefined system actions rather than executing arbitrary shell commands.

- Confirmation is enabled by default for destructive operations.
- API keys should be stored in environment variables.
- Local memory and logs may contain personal information.
- Review requested actions before confirming them.
- Keep credentials and sensitive data out of public repositories.

## 🧠 How It Works

1. **Input:** Receives a voice command or text input.
2. **Processing:** Routes the input to the appropriate assistant or command handler.
3. **Execution:** Performs a supported action or generates a response.
4. **Response:** Displays the result and, in voice mode, speaks the response.
5. **Memory:** Uses local persistent storage for supported memory functionality.

## 🔮 Future Improvements

Potential enhancements include:

- Improved wake-word detection.
- Streaming AI responses.
- More advanced contextual memory.
- Additional desktop automation tools.
- Calendar and email integrations.
- A plugin system for extending capabilities.
- An enhanced futuristic GUI.

## 👨‍💻 Developer

**Aryan Yerpude**

AI/ML Developer | Python Developer | Aspiring AI Engineer

- GitHub: [@Aryan2006-hub](https://github.com/Aryan2006-hub)
- LinkedIn: [Aryan Yerpude](https://www.linkedin.com/in/aryan-yerpude-3338aa334/)

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub!

---

<p align="center">
  <strong>JARVIS Ultimate — Bringing AI-Powered Assistance to Your Desktop.</strong>
</p>
