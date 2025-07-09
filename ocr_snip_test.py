import pytesseract
from PIL import ImageGrab
from selector_step1 import RegionSelector  # your DPI-aware snipping class
import requests
import tkinter as tk
import re
import keyboard
import threading
import pyautogui

# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ==============================
# 🔎 Get meaning from dictionary
# ==============================
def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Meaning not found."

    try:
        data = response.json()
        meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
        return meaning
    except Exception as e:
        return "Meaning not found."

# ==============================
# 💬 Popup meaning window
# ==============================
def show_popup(word, meaning):
    popup = tk.Tk()
    popup.title(f"Meaning: {word}")
    popup.geometry("400x200")
    tk.Label(popup, text=f"{word}", font=("Helvetica", 16, "bold")).pack(pady=10)
    tk.Message(popup, text=meaning, width=380).pack(padx=10)
    popup.after(10000, popup.destroy)  # auto-close after 10s
    popup.mainloop()

# ==============================
# 🧠 OCR + Meaning Handler
# ==============================
def process_bbox(bbox):
    left, top = bbox[0], bbox[1]
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]

    img = pyautogui.screenshot(region=(left, top, width, height))
    text = pytesseract.image_to_string(img)

    print("🧠 OCR text:", text)

    # Clean word
    matches = re.findall(r'\b[a-zA-Z]{2,}\b', text)
    word = matches[0] if matches else ""

    if word:
        meaning = get_meaning(word)
        show_popup(word, meaning)
    else:
        show_popup("No word", "Could not detect any valid word.")

# ==============================
# 🖱️ Snip Trigger (MAIN THREAD)
# ==============================
def run_snip():
    print("🔁 Snip triggered!")
    selector = RegionSelector()
    bbox = selector.get_bbox()

    if bbox:
        threading.Thread(target=process_bbox, args=(bbox,)).start()

# ==============================
# 🎯 Main Hotkey Listener
# ==============================
def main():
    print("🔥 Ready! Press Ctrl + Alt + D to activate snip.")
    keyboard.add_hotkey("ctrl+alt+d", run_snip)
    keyboard.wait()  # Keep script alive

if __name__ == "__main__":
    main()
