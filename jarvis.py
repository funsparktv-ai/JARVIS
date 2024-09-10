import threading
import random
import os
import logging
from internet_check import is_Online
from Alert import Alert
from Data.DLG_Data import online_dlg, offline_dlg
from co_brain import Jarvis
from TextToSpeech.Fast_DF_TTS import speak
from Automation.Battery import battery_alert
from Time_Operations.throw_alert import check_schedule, check_alarm  # Corrected import

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# File paths (adjusted for relative paths)
base_dir = os.path.dirname(__file__)
ALARM_PATH = os.path.join(base_dir, 'Data', 'Alam_data.txt')
SCHEDULE_PATH = os.path.join(base_dir, 'Data', 'Schedule_data.txt')

# Configure pydub with ffmpeg
from pydub import AudioSegment

AudioSegment.converter = r'F:\Python\ffmpeg-7.0.2-full_build\bin\ffmpeg.exe'

# Random dialog selection
random_online_dlg = random.choice(online_dlg)
random_offline_dlg = random.choice(offline_dlg)


def wish_online() :
    """Simulates a greeting action when online using threading."""
    try :
        threads = [
            threading.Thread(target=speak, args=(random_online_dlg,)),
            threading.Thread(target=Alert, args=(random_online_dlg,))
        ]
        for thread in threads :
            thread.start()
        for thread in threads :
            thread.join()
    except Exception as e :
        logging.error(f"Error during online wish: {e}")


def run_tasks_online() :
    """Runs scheduled tasks when the system is online."""
    try :
        tasks = [
            threading.Thread(target=battery_alert),
            threading.Thread(target=check_schedule, args=(SCHEDULE_PATH,)),
            threading.Thread(target=Jarvis),
            threading.Thread(target=check_alarm, args=(ALARM_PATH,))
        ]
        for task in tasks :
            task.start()
        for task in tasks :
            task.join()
    except FileNotFoundError as e :
        logging.error(f"File not found: {e}")
    except Exception as e :
        logging.error(f"Unexpected error during online tasks: {e}")


def process_command(user_input) :
    """Process the user command and handle known commands."""
    commands = {
        'hello jarvis' : 'Hello! How can I assist you today?',
        'what is your name' : 'I am Jarvis, your virtual assistant.',
    }

    # Normalize the user input to lowercase
    user_input = user_input.lower().strip()

    # Find the response based on the command
    response = commands.get(user_input, f"Unknown command: '{user_input}'")

    return response


def main() :
    """Main function to determine if the system is online or offline and execute tasks accordingly."""
    try :
        if is_Online() :
            wish_online()
            run_tasks_online()
        else :
            Alert(random_offline_dlg)

        # Example command processing (replace this with actual input handling logic)
        user_input = 'hello Jarvis'  # Example input
        response = process_command(user_input)
        logging.info(f"Command response: {response}")

    except Exception as e :
        logging.error(f"Error in main function: {e}")


if __name__ == "__main__" :
    main()
