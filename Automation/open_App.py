import pyautogui as gui
import subprocess
import time
import platform


def open_App(app_name: str) :
    try :
        # First attempt to open the application using subprocess
        result = subprocess.run(app_name, check=True, shell=True)

        # If the application was successfully opened, no need for fallback
        if result.returncode == 0 :
            return
    except subprocess.CalledProcessError :
        # Fallback mechanism using pyautogui (in case subprocess fails)
        try :
            print(f"Failed to open '{app_name}' using subprocess. Trying alternative method...")
            gui.press("win")
            time.sleep(0.5)
            gui.write(app_name)
            time.sleep(0.5)
            gui.press("enter")
        except Exception as e :
            print(f"Error opening application '{app_name}': {e}")


# Optional check for Windows platform before running
if platform.system() == "Windows" :
    open_App("notepad")  # Example usage for Windows
else :
    print("This script is intended to run on Windows.")
