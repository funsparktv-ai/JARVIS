import os
import time
import threading
from Alert import Alert
from TextToSpeech.Fast_DF_TTS import speak

def load_schedule(file_path):
    """Load schedule from the given file path."""
    schedule = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    line_time, activity = line.strip().split(' = ')
                    schedule[line_time.strip()] = activity.strip()
    except Exception as e:
        print(f"Error loading schedule: {e}")
    return schedule

def check_schedule(file_path):
    """Monitor and execute scheduled activities."""
    last_modified = 0
    schedule = load_schedule(file_path)
    while True:
        current_time = time.strftime("%I:%M%p")
        try:
            # Check file modification time
            modified = os.path.getmtime(file_path)
            if modified != last_modified:
                last_modified = modified
                schedule = load_schedule(file_path)

            if current_time in schedule:
                text = schedule[current_time]
                execute_alert_and_speech(text)

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(60)

def load_alarm_time(file_path):
    """Load alarm data from the given file path."""
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except Exception as e:
        print(f"Error loading alarm data: {e}")
        return ""

def check_alarm(file_path):
    """Monitor and trigger alarm based on file changes."""
    last_modified = 0
    alarm_message = "This is Alarm"
    while True:
        current_time = time.strftime("%I:%M%p")
        try:
            # Check file modification time
            modified = os.path.getmtime(file_path)
            if modified != last_modified:
                last_modified = modified
                alarm_data = load_alarm_time(file_path)

            if current_time in alarm_data:
                execute_alert_and_speech(alarm_message)

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(10)

def execute_alert_and_speech(text):
    """Helper function to execute alert and speech."""
    threading.Thread(target=Alert, args=(text,)).start()
    threading.Thread(target=speak, args=(text,)).start()

# File paths (relative to the script location)
base_dir = os.path.dirname(__file__)
schedule_path = os.path.join(base_dir, 'Data', 'Schedule_data.txt')
alarm_path = os.path.join(base_dir, 'Data', 'Alam_data.txt')

if __name__ == "__main__":
    # Start schedule and alarm check in separate threads
    threading.Thread(target=check_schedule, args=(schedule_path,), daemon=True).start()
    threading.Thread(target=check_alarm, args=(alarm_path,), daemon=True).start()
