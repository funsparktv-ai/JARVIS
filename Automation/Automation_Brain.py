from Automation.open_App import open_App
from Automation.Web_Open import openweb
import pyautogui as gui
from Automation.Play_Music_YT import play_song
from TextToSpeech import Fast_DF_TTS
from Automation.Battery import check_percentage
from os import getcwd
import time
from Automation.tab_automation import perform_browser_action
from Automation.Youtube_play_back import perform_media_action
import pywhatkit
from Automation.scrool_system import perform_scroll_action
import threading
from TextToSpeech.Fast_DF_TTS import speak


# Function to handle playing/pausing media
def play() :
    gui.press("space")


# Function to handle Google search via pywhatkit
def search_google(text) :
    pywhatkit.search(text)


# Function to close the current window
def close() :
    gui.hotkey('alt', 'f4')


# Function to search text within an application or browser
def search(text) :
    gui.press("/")
    time.sleep(0.3)
    gui.write(text)


# Function to handle opening websites or apps
def Open_Brain(text) :
    if "website" in text or "open website named" in text :
        text = text.replace("open", "").strip()
        text = text.replace("website", "").strip()
        text = text.replace("open website named", "").strip()
        t1 = threading.Thread(target=speak, args=(f"Navigating {text} website",))
        t2 = threading.Thread(target=openweb, args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    else :
        text = text.replace("open", "").strip()
        text = text.replace("app", "").strip()
        t1 = threading.Thread(target=speak, args=(f"Opening {text} application",))
        t2 = threading.Thread(target=open_App, args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()


# Function to clear the content of input.txt
def clear_file() :
    with open(f"{getcwd()}\\input.txt", "w") as file :
        file.truncate(0)


# Core function to handle automation tasks
def Auto_main_brain(text) :
    try :
        # Opening applications or websites
        if text.startswith("open") :
            Open_Brain(text)

        # Closing applications
        elif "close" in text :
            close()

        # Playing music on YouTube
        elif "play music" in text or "play music on youtube" in text :
            speak("Which song do you want to play?")
            clear_file()
            output_text = ""
            while True :
                with open("input.txt", "r") as file :
                    input_text = file.read().lower()
                if input_text != output_text :
                    output_text = input_text
                    if output_text.endswith("song") :
                        play_song(output_text)
                        break

        # Checking battery status
        elif "check battery percentage" in text or "check battery level" in text :
            check_percentage()

        # Searching within an application
        elif text.startswith("search") :
            text = text.replace("search", "").strip()
            t1 = threading.Thread(target=speak, args=(f"Searching for {text}",))
            t2 = threading.Thread(target=search, args=(text,))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
            time.sleep(0.5)
            gui.press("enter")

        # Searching in Google
        elif "search in google" in text :
            text = text.replace("search in google", "").strip()
            t1 = threading.Thread(target=speak, args=(f"Searching for {text} in Google",))
            t2 = threading.Thread(target=search_google, args=(text,))
            t1.start()
            t2.start()
            t1.join()
            t2.join()

        # Play, stop, or pause media
        elif "play" in text or "stop" in text or "pause" in text :
            play()

        # Performing browser, media, or scroll actions
        else :
            perform_browser_action(text)
            perform_media_action(text)
            perform_scroll_action(text)

    except Exception as e :
        print(f"Error: {str(e)}")


# Example: Test the automation brain functionality
if __name__ == "__main__" :
    while True :
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"] :
            break
        Auto_main_brain(user_input)
