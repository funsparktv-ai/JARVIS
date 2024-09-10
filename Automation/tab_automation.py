import pyautogui


# Define functions for browser actions
def open_new_tab() :
    pyautogui.hotkey('ctrl', 't')


def close_tab() :
    pyautogui.hotkey('ctrl', 'w')


def open_browser_menu() :
    pyautogui.hotkey('alt', 'f')


def zoom_in() :
    pyautogui.hotkey('ctrl', '+')


def zoom_out() :
    pyautogui.hotkey('ctrl', '-')


def refresh_page() :
    pyautogui.hotkey('ctrl', 'r')


def switch_to_next_tab() :
    pyautogui.hotkey('ctrl', 'tab')


def switch_to_previous_tab() :
    pyautogui.hotkey('ctrl', 'shift', 'tab')


def open_history() :
    pyautogui.hotkey('ctrl', 'h')


def open_bookmarks() :
    pyautogui.hotkey('ctrl', 'b')


def go_back() :
    pyautogui.hotkey('alt', 'left')


def go_forward() :
    pyautogui.hotkey('alt', 'right')


def open_dev_tools() :
    pyautogui.hotkey('ctrl', 'shift', 'i')


def toggle_full_screen() :
    pyautogui.hotkey('f11')


def open_private_window() :
    pyautogui.hotkey('ctrl', 'shift', 'n')


# Map commands to functions
ACTION_MAP = {
    "open new tab" : open_new_tab,
    "new tab kholo" : open_new_tab,
    "close tab" : close_tab,
    "tab band karo" : close_tab,
    "open browser menu" : open_browser_menu,
    "browser menu kholo" : open_browser_menu,
    "zoom in" : zoom_in,
    "zoom in karo" : zoom_in,
    "zoom out" : zoom_out,
    "zoom out karo" : zoom_out,
    "refresh page" : refresh_page,
    "page refresh karo" : refresh_page,
    "switch to next tab" : switch_to_next_tab,
    "next tab par jao" : switch_to_next_tab,
    "switch to previous tab" : switch_to_previous_tab,
    "previous tab par jao" : switch_to_previous_tab,
    "open history" : open_history,
    "history kholo" : open_history,
    "open bookmarks" : open_bookmarks,
    "bookmarks kholo" : open_bookmarks,
    "go back" : go_back,
    "peeche jao" : go_back,
    "go forward" : go_forward,
    "aage jao" : go_forward,
    "open dev tools" : open_dev_tools,
    "dev tools kholo" : open_dev_tools,
    "toggle full screen" : toggle_full_screen,
    "full screen karo" : toggle_full_screen,
    "open private window" : open_private_window,
    "private window kholo" : open_private_window
}


def perform_browser_action(text: str) :
    action = ACTION_MAP.get(text)
    if action :
        action()
    else :
        print(f"Unknown command: {text}")


# Example usage
if __name__ == "__main__" :
    perform_browser_action("open new tab")  # Test command
