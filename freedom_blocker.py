import os
import cv2
import numpy as np
import pyautogui
import time
import psutil
import pygetwindow as gw
from nudenet import NudeDetector
import win32gui
import win32process
import subprocess
import glob

WATCHDOG_NAME = "watchdog.exe"
STORED_WATCHDOG_PATH = os.path.expanduser("~\\watchdog_path.txt")

# Get the directory where the EXE/script is running
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the NudeNet model from the "models" folder
MODEL_PATH = os.path.join(BASE_DIR, "models", "640m.onnx")
detector = NudeDetector(MODEL_PATH)

def find_watchdog():
    """Search common directories for watchdog.exe if not found in stored path."""
    search_dirs = [
        os.path.expanduser("~\\Documents"),  
        os.path.expanduser("~\\Desktop"),  
        "C:\\Program Files",
        "C:\\Program Files (x86)",
        "C:\\Users\\Public",
    ]

    for directory in search_dirs:
        exe_path = os.path.join(directory, WATCHDOG_NAME)
        if os.path.exists(exe_path):
            return exe_path

    print("Scanning entire C: drive for watchdog.exe (this may take a while)...")
    for file in glob.glob(f"C:\\**\\{WATCHDOG_NAME}", recursive=True):
        return file  

    return None

def get_watchdog_path():
    """Retrieve watchdog.exe path from file or search if not found."""
    if os.path.exists(STORED_WATCHDOG_PATH):
        with open(STORED_WATCHDOG_PATH, "r") as f:
            exe_path = f.read().strip()
            if os.path.exists(exe_path):
                return exe_path  

    exe_path = find_watchdog()
    if exe_path:
        with open(STORED_WATCHDOG_PATH, "w") as f:
            f.write(exe_path)  
    return exe_path

def is_watchdog_running():
    """Check if watchdog.exe is running."""
    for process in psutil.process_iter(['name']):
        if process.info['name'] and process.info['name'].lower() == WATCHDOG_NAME.lower():
            return True
    return False

def start_watchdog():
    """Start watchdog.exe."""
    exe_path = get_watchdog_path()
    if exe_path:
        print(f"Starting {exe_path}...")
        subprocess.Popen(exe_path, creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        print("Error: Watchdog not found!")

def capture_screen_regions():
    screenshot = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    height, width, _ = image.shape
    regions = []
    grid_size = 3  
    step_h, step_w = height // grid_size, width // grid_size
    
    for i in range(grid_size):
        for j in range(grid_size):
            region = image[i * step_h:(i + 1) * step_h, j * step_w:(j + 1) * step_w]
            regions.append(((i, j), region))  # Return position for tracking
    
    return regions

def check_nudity(image):
    _, encoded_image = cv2.imencode(".jpg", image)
    image_bytes = encoded_image.tobytes()
    detections = detector.detect(image_bytes)
    
    nsfw_labels = {
        "BUTTOCKS_EXPOSED", "FEMALE_BREAST_EXPOSED",
        "FEMALE_GENITALIA_EXPOSED", "MALE_BREAST_EXPOSED", "ANUS_EXPOSED",
        "MALE_GENITALIA_EXPOSED", "ANUS_COVERED",
    }
    
    return any(d['class'] in nsfw_labels for d in detections)

def get_window_at_position(region_coords, screen_size):
    """
    Identify which application window matches the region where nudity was detected.
    """
    x, y = region_coords
    width, height = screen_size

    abs_x = x * (width // 3)
    abs_y = y * (height // 3)

    hwnd = win32gui.WindowFromPoint((abs_x, abs_y))
    
    if hwnd:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        return pid
    return None

def close_application(pid):
    """
    Close the application with the given Process ID (PID).
    """
    try:
        proc = psutil.Process(pid)
        print(f"Closing application: {proc.name()}")
        proc.terminate()
    except psutil.NoSuchProcess:
        print("Process not found.")
    except psutil.AccessDenied:
        print("Access denied. Try running as administrator.")

def main():
    print("NSFW Blocker running in background...")
    screen_size = pyautogui.size()  
    
    try:
        while True:
            if not is_watchdog_running():
                print("Watchdog is not running! Restarting it...")
                start_watchdog()

            for region_coords, region_image in capture_screen_regions():
                if check_nudity(region_image):
                    print("Nudity detected! Searching for the application...")

                    pid = get_window_at_position(region_coords, screen_size)
                    if pid:
                        close_application(pid)
                    else:
                        print("Could not determine the application. Try adjusting detection.")

                    break  
            time.sleep(0.5)  
    except KeyboardInterrupt:
        print("NSFW Blocker stopped.")

if __name__ == "__main__":
    main()
