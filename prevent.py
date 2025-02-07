import os
import sys
import time
import psutil
import pyautogui
import pytesseract
import cv2
import numpy as np
import win32gui
import win32process

# 🔥 The keyword to protect 🔥
PROTECTED_WORD = "bammus"

# ✅ Detect if running as an EXE or script
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS  # PyInstaller temp folder
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ Set Tesseract path dynamically
TESSERACT_PATH = os.path.join(BASE_DIR, "tesseract", "tesseract.exe")
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

# ✅ Set tessdata path
os.environ["TESSDATA_PREFIX"] = os.path.join(BASE_DIR, "tesseract", "tessdata")

# ✅ Debugging check
print(f"🔍 Using Tesseract at: {TESSERACT_PATH}")
print(f"🔍 Tessdata location: {os.environ['TESSDATA_PREFIX']}")

# 🛑 Windows API function to close a specific application
def close_application(hwnd):
    """Close the application that contains the detected text."""
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        proc = psutil.Process(pid)
        print(f"🔴 Closing application: {proc.name()} (PID: {pid}) - Detected '{PROTECTED_WORD}' on screen")
        proc.terminate()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        print("Could not close process, access denied.")

# 🖥 Identify which window contains the detected text
def get_foreground_window():
    """Get the currently focused window."""
    return win32gui.GetForegroundWindow()

# ⚡ Capture the active window and scan for "bammus"
def scan_screen():
    """Capture only the foreground window and check for the protected word."""
    hwnd = get_foreground_window()
    if hwnd:
        rect = win32gui.GetWindowRect(hwnd)
        x, y, x1, y1 = rect
        width, height = x1 - x, y1 - y

        if width > 0 and height > 0:
            screenshot = pyautogui.screenshot(region=(x, y, width, height))
            image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

            # 🔍 Extract text using Tesseract OCR
            detected_text = pytesseract.image_to_string(image, config="--psm 6").lower()
            print(f"🔠 Detected text: {detected_text}")
            
            if PROTECTED_WORD in detected_text:
                print(f"⚠ DETECTED '{PROTECTED_WORD}' IN ACTIVE WINDOW! Closing application...")
                close_application(hwnd)
                return True
    return False

# ⚠ Display warning message
def warn_user():
    os.system('msg * "⚠ DO NOT TRY TO UNINSTALL THIS PROGRAM! ⚠"')

# 🔄 Main loop (runs every 0.1s)
def monitor_screen():
    print(f"🚀 Monitoring live screen for '{PROTECTED_WORD}' in the active window...")

    while True:
        scan_screen()
        time.sleep(0.1)  # 🔥 Faster detection

if __name__ == "__main__":
    monitor_screen()
