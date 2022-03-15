from ast import While
import pyautogui,pyperclip,keyboard,time


while True:
    try:
        if keyboard.is_pressed(")"):
            pyperclip.copy(";")
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.1)
    except:
        pass