import time
import pyautogui


while True:
    x, y = pyautogui.position()
    button = pyautogui.locateOnScreen("img/destroy.png", confidence=0.5)
    pyautogui.click(button)
    pyautogui.moveTo(x, y)
    time.sleep(2)