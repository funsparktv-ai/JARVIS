from Automation.Automation_Brain import Auto_main_brain, clear_file
from NetHyTechSTT.listen import listen
from TextToSpeech.Fast_DF_TTS import speak
import threading
from Data.DLG_Data import online_dlg, offline_dlg
import random
from Automation.Battery import battery_alert  # Updated import statement
from Time_Operations.brain import input_manage, input_manage_Alam
from Features.check_internet_speed import get_internet_speed
from Brain.brain import Main_Brain
from Features.create_file import create_file
import time
import os

# Predefined values
numbers = ["1:", "2:", "3:", "4:", "5:", "6:", "7:", "8:", "9:"]
spl_numbers = ["11:", "12:"]

# Random dialog choices
ran_online_dlg = random.choice(online_dlg)
ran_offline_dlg = random.choice(offline_dlg)

# Define a cooldown to debounce input handling (avoid processing too frequently)
last_processed_time = 0
COOLDOWN = 2  # seconds

# Process time-specific input and handle alarms
def process_time_input(output_text):
    output_text = output_text.replace(" p.m.", "PM").replace(" a.m.", "AM")
    if any(sn in output_text for sn in spl_numbers):
        input_manage_Alam(output_text)
    else:
        for number in numbers:
            if number in output_text:
                output_text = output_text.replace(number, f"0{number}")
        input_manage(output_text)
    clear_file()

# Command dictionary mapping
COMMANDS = {
    "check internet speed": lambda: check_internet_speed(),
    "jarvis": lambda text: speak(Main_Brain(text)),
    "create file": lambda text: create_file(text),
    "set alarm": lambda text: process_time_input(text),
    "tell me": lambda text: process_time_input(text)
}

def check_internet_speed():
    speak("Checking your internet speed")
    speed = get_internet_speed()
    speak(f"The device is running on {speed} Mbps internet speed")

# Process input from file and route to appropriate functions
def process_input(output_text):
    # Check if it's a pre-defined command
    for command, action in COMMANDS.items():
        if output_text.startswith(command):
            action(output_text)
            return

    # Default fallback to Automation brain
    Auto_main_brain(output_text)

# Optimized input checker that debounces input and checks for file changes
def check_inputs():
    global last_processed_time
    last_output_text = ""

    while True:
        try:
            # Only check for new input at regular intervals
            if time.time() - last_processed_time < COOLDOWN:
                time.sleep(0.1)
                continue

            if not os.path.exists("input.txt"):
                continue

            with open("input.txt", "r") as file:
                input_text = file.read().strip().lower()

            if input_text and input_text != last_output_text:
                last_output_text = input_text
                process_input(last_output_text)
                last_processed_time = time.time()

        except Exception as e:
            print(f"Error in input processing: {e}")

# Main Jarvis thread initialization
def Jarvis():
    clear_file()
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=check_inputs)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# Example: Test the Jarvis functionality
if __name__ == "__main__":
    Jarvis()
