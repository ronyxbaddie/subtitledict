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
- `pytesseract` – OCR engine wrapper
- `pyautogui` – screen capture
- `tkinter` – GUI for selection & popup
- `keyboard` – global hotkey binding
- `requests` – HTTP requests to fetch definitions

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/subtitle-dictionary-snipper.git
cd subtitle-dictionary-snipper
```
### 2. Set Up Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install Python Requirements
```bash
pip install -r requirements.txt
```
### 4. Install Tesseract OCR
Download from: https://github.com/UB-Mannheim/tesseract/wiki

Install to the default path:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```
✅ Make sure the .exe path is correctly set inside ocr_snip_tool.py.

---

## ✅ How to Use
Run the script:

```bash
python ocr_snip_tool.py
```
While watching a movie or any video with subtitles, press:

```mathematica
Ctrl + Alt + D
```
Drag to select a subtitle word on your screen

A popup will appear showing the definition of the word!

---

## 📁 Project Structure
```bash
subtitle-dictionary-snipper/
│
├── selector_step1.py       # RegionSelector (drag-to-select tool)
├── ocr_snip_tool.py        # Main app script (hotkey + OCR + popup)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 📦 Requirements
Listed in requirements.txt:

```text
Copy code
pytesseract
pillow
pyautogui
keyboard
requests
```

---

## 🧠 Future Ideas
- 🔊 Add pronunciation using Text-to-Speech

- 🌐 Translate to Hindi or other languages

- 📓 Save learned words to a local file (personal vocab list)

- 🪟 Run in background as tray app

- 🧪 Fuzzy matching for unclear OCR results

---

## 🙋‍♂️ Author
Made with ❤️ by Raunak Sharma.

> “Because sometimes the best way to learn English... is through subtitles.” 🎥

---

## 🪪 License
This project is licensed under the MIT License — use it freely, modify it proudly.

---

## ⭐️ Star This Repo
If you found this useful, feel free to give it a ⭐️ on GitHub — it helps more devs find it!
---
