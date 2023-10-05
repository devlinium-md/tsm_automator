import time
import pyautogui

counter = 0
time.sleep(5)
while counter < 10:
    x, y = pyautogui.position()
    button = pyautogui.locateOnScreen("img/destroy.png", confidence=0.5)
    if button is not None:
        pyautogui.click(button)
        pyautogui.moveTo(x, y)
        time.sleep(2)
        button = None
        counter = 0
    else:
        counter += 1
        time.sleep(1)
