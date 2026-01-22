import keyboard
import time

def send_message():
    keyboard.press_and_release("backspace")
    keyboard.write("@")
    time.sleep(0.2)
    keyboard.write("o")
    time.sleep(0.2)
    keyboard.press_and_release("tab")
    time.sleep(0.2)
    keyboard.press_and_release("enter")

keyboard.add_hotkey("/", send_message)

keyboard.wait()
