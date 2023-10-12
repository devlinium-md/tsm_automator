import time
import pyautogui


def post_or_destroy(action, freq):
    counter = 0
    time.sleep(5)
    while counter < 10:
        x, y = pyautogui.position()
        button = pyautogui.locateOnScreen("img/" + action + ".png", confidence=0.8)
        if button is not None:
            pyautogui.click(button)
            pyautogui.moveTo(x, y)
            time.sleep(freq)
            button = None
            counter = 0
        else:
            counter += 1
            time.sleep(1)
