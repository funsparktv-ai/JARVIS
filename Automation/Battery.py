import psutil
import time
import threading
from TextToSpeech.Fast_DF_TTS import speak
from Alert import Alert

def battery_alert():
    while True:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        if percentage == 100:
            alert_message = "100% charge"
            speak_message = "100% charged. Please unplug it."
        elif percentage <= 5:
            alert_message = "Battery is going to die"
            speak_message = "This is your last chance sir, charge your system now."
        elif percentage <= 10:
            alert_message = "Battery is too low"
            speak_message = "We are running on very low battery power."
        elif percentage <= 20:
            alert_message = "Battery Low"
            speak_message = "Battery is low now."
        else:
            time.sleep(30)  # Avoid frequent checks if battery is not critically low
            continue

        # Start threads for alert and speech
        threading.Thread(target=Alert, args=(alert_message,)).start()
        threading.Thread(target=speak, args=(speak_message,)).start()
        time.sleep(10)  # Adjust sleep to prevent rapid firing of alerts

def check_plug():
    previous_state = psutil.sensors_battery().power_plugged
    while True:
        battery = psutil.sensors_battery()
        current_state = battery.power_plugged
        if current_state != previous_state:
            if current_state:
                alert_message = "Charging **STARTED**"
                speak_message = "Charging Started"
            else:
                alert_message = "Charging **STOP**"
                speak_message = "Charging Stopped"

            # Start threads for alert and speech
            threading.Thread(target=Alert, args=(alert_message,)).start()
            threading.Thread(target=speak, args=(speak_message,)).start()

            previous_state = current_state
        time.sleep(10)  # Check every 10 seconds

def check_percentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    alert_message = f"The device is running on {percent}% power"
    speak_message = alert_message

    # Start threads for alert and speech
    threading.Thread(target=Alert, args=(alert_message,)).start()
    threading.Thread(target=speak, args=(speak_message,)).start()

# Example usage
if __name__ == "__main__":
    # Start battery alert and plug check in separate threads
    threading.Thread(target=battery_alert, daemon=True).start()
    threading.Thread(target=check_plug, daemon=True).start()
    check_percentage()  # Check percentage immediately
