import psutil
import subprocess
import time
import os
import glob

APP_NAMES = ["freedom_blocker.exe", "preventer.exe"]
STORED_PATH_FILES = {
    "freedom_blocker.exe": os.path.expanduser("~\\freedom_blocker_path.txt"),
    "preventer.exe": os.path.expanduser("~\\preventer_path.txt")
}

def find_exe(app_name):
    """Search common directories for the EXE if not found in stored path."""
    search_dirs = [
        os.path.expanduser("~\\Documents"),  # User's Documents
        os.path.expanduser("~\\Desktop"),  # User's Desktop
        "C:\\Program Files",
        "C:\\Program Files (x86)",
        "C:\\Users\\Public",
    ]

    for directory in search_dirs:
        exe_path = os.path.join(directory, app_name)
        if os.path.exists(exe_path):
            return exe_path

    # Search entire C: drive (last resort, slower)
    print(f"Scanning entire C: drive for {app_name} (this may take a while)...")
    for file in glob.glob(f"C:\\**\\{app_name}", recursive=True):
        return file  

    return None  # Not found

def get_exe_path(app_name):
    """Retrieve EXE path from file or search if not found."""
    stored_path_file = STORED_PATH_FILES[app_name]
    
    if os.path.exists(stored_path_file):
        with open(stored_path_file, "r") as f:
            exe_path = f.read().strip()
            if os.path.exists(exe_path):
                return exe_path  # Use stored path

    # If not stored, search and save it
    exe_path = find_exe(app_name)
    if exe_path:
        with open(stored_path_file, "w") as f:
            f.write(exe_path)  # Save for future use
    return exe_path

def is_running(process_name):
    """Check if the process is currently running."""
    for process in psutil.process_iter(['name']):
        if process.info['name'] and process.info['name'].lower() == process_name.lower():
            return True
    return False

def start_process(app_name):
    """Start the specified process."""
    exe_path = get_exe_path(app_name)
    if exe_path:
        print(f"Starting {exe_path}...")
        subprocess.Popen(exe_path, creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        print(f"Error: {app_name} not found!")

def restart_if_needed():
    """Monitor both processes and restart if needed."""
    while True:
        for app_name in APP_NAMES:
            if not is_running(app_name):
                print(f"{app_name} was closed! Restarting...")
                start_process(app_name)
        time.sleep(3)

if __name__ == "__main__":
    print("Checking if required applications are running...")
    restart_if_needed()
