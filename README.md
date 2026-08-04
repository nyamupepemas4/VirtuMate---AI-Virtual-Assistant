# VirtuMate — AI-Powered Voice Assistant

An independently built Python voice assistant supporting voice-controlled 
system navigation, app/web control, task automation, and conversational 
chat. Technical basis for an academic working paper on privacy-preserving 
voice assistant architecture.

## Demo

![VirtuMate GUI](screenshots/screenshot_20250317_204958.jpg)
![VirtuMate Chatbot Mode](screenshots/screenshot_20250401_102517.jpg)

*Screenshots show the PyQt5 GUI version of VirtuMate in action.*

## Features

- **Voice control** — wake word activation, speech recognition, text-to-speech
- **App/web control** — open/close applications and websites (`Dictapp.py`)
- **Task automation** — alarms, scheduling, reminders (`alarm.py`, `tasks.txt`)
- **Web search & info** — Google, YouTube, Wikipedia search (`SearchNow.py`); 
  live news by category (`NewsRead.py`); WolframAlpha-powered calculations 
  (`Calculatenumbers.py`)
- **Chatbot mode** — conversational fallback with persistent, passphrase-based 
  chat history (`VirtuMateChatbot.py`)
- **System utilities** — internet speed test, volume control, WhatsApp 
  messaging automation, IPL score fetching
- **GUI front-end** — a PyQt5-based interface (`jarvisUi.py`), shown in the 
  screenshots above

## Structure

| File | Purpose |
|---|---|
| `Jarvis_main.py` | CLI entry point — command routing and password-gated startup |
| `jarvisUi.py` | PyQt5 GUI front-end |
| `VirtuMateChatbot.py` | Conversational chatbot mode with persistent chat history |
| `Dictapp.py` | App/website open and close handling |
| `Calculatenumbers.py` | WolframAlpha-powered calculation queries |
| `NewsRead.py` | Category-based news reading |
| `SearchNow.py` | Google/YouTube/Wikipedia search |
| `Whatsapp.py` | WhatsApp message automation |
| `alarm.py` / `GreetMe.py` / `keyboard.py` | Supporting utilities |

## Setup

Requires your own API keys for OpenAI, WolframAlpha, and NewsAPI — set as 
environment variables (`OPENAI_API_KEY`, etc.), not hardcoded.

```bash
pip install -r requirements.txt
python Jarvis_main.py
```

**Note on the GUI:** `jarvisUi.py` is included as the interface layer shown 
in the screenshots above. It depends on a `Features.py` module and image/GIF 
assets that are part of active local development and not yet included in 
this repo. The CLI entry point (`Jarvis_main.py`) is fully self-contained 
and runnable as-is.

## Status

Built independently during my BCA. Forms the technical basis for an academic 
working paper on privacy-preserving voice assistant architecture.
