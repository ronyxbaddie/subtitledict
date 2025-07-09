# 🎬 Subtitle Dictionary Snipper

A real-time, hotkey-triggered subtitle dictionary tool for Windows — made for movie lovers and language learners.  
Select a subtitle word on-screen while watching a movie, and instantly get its meaning in a popup using OCR and a free dictionary API.

---

## 🚀 Features

- 🖱️ Snip any part of your screen using a custom hotkey
- 🧠 Extracts text using Tesseract OCR
- 📚 Looks up the word’s meaning using [Free Dictionary API](https://dictionaryapi.dev/)
- 💬 Displays the meaning in a clean popup (auto-closes after 10 seconds)
- ⚡ Global hotkey support — works even while watching movies in VLC or Netflix
- ✅ Works offline (except for API lookup)

---

## 🛠️ Built With

- **Python**
- [`pytesseract`](https://pypi.org/project/pytesseract/) – OCR engine wrapper
- [`pyautogui`](https://pypi.org/project/pyautogui/) – screen capture
- [`tkinter`](https://docs.python.org/3/library/tkinter.html) – GUI for selection & popup
- [`keyboard`](https://pypi.org/project/keyboard/) – global hotkey binding
- [`requests`](https://pypi.org/project/requests/) – HTTP requests to fetch definitions

---

## 📸 Demo

![demo](demo.gif)  
> (You can add a demo GIF or image here to show the drag-and-define in action!)

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/subtitle-dictionary-snipper.git
cd subtitle-dictionary-snipper
