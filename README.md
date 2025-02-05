# Virtual Assistant Project 🤖

This project is a Python-based virtual assistant that can perform a wide range of tasks such as searching the web, controlling applications, sending emails, managing media, interacting with the user through voice commands, and more. It integrates several libraries to achieve its functionalities and provides an interactive experience, particularly designed to assist users in everyday activities.

## Features 🌟

- **Voice Command Recognition 🎙️**: The assistant listens to voice commands using the `speech_recognition` library and responds accordingly.
- **Text-to-Speech 🗣️**: It speaks back to the user using the `pyttsx3` and `gTTS` libraries for text-to-speech synthesis.
- **Web Search 🔍**: The assistant can search Google and Wikipedia, open specific search results, and fetch data from various sources.
- **Email Integration 📧**: Send and read emails using `smtplib` and `imaplib`. The assistant can send email messages and read the latest emails from a Gmail account.
- **Internet Speed Test 🌐**: It can perform an internet speed test and report download and upload speeds using the `speedtest` library.
- **Weather Information 🌦️**: It can fetch and announce the current temperature of the user's location.
- **Webcam Access 📷**: The assistant can open and control the webcam using `OpenCV` for video capture.
- **Social Media Integration 📱**: It supports opening Instagram profiles and downloading profile pictures.
- **System Monitoring ⚙️**: It checks CPU usage and battery status and provides feedback on the system’s current condition.
- **QR Code Generation 🔲**: The assistant can generate QR codes from text input.
- **Automated Tasks ⚡**: It can take screenshots, generate random numbers, tell jokes, and even manage browser tabs.

## Installation 🛠️

### Prerequisites 📦

You need to have Python installed on your machine. The following libraries are required to run the assistant:

- `speech_recognition`
- `gTTS`
- `openai`
- `pyjokes`
- `requests`
- `smtplib`
- `imaplib`
- `pyttsx3`
- `instaloader`
- `pyautogui`
- `psutil`
- `speedtest-cli`
- `wikipedia`
- `pywhatkit`
- `opencv-python`
- `pytube`
- `qrcode`
- `beautifulsoup4`

### Install the Required Libraries 📥

You can install the necessary libraries using `pip`:

```bash
pip install speechrecognition gtts openai pyjokes requests smtplib imaplib pyttsx3 instaloader pyautogui psutil speedtest-cli wikipedia pywhatkit opencv-python pytube qrcode beautifulsoup4
