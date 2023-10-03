import pyautogui
import time
import random
import sys


while True:
    # Start curdor position.
    x, y = pyautogui.position()
    # Post button, used to post the item on aucution.
    post_button = pyautogui.locateOnScreen("img/post.png", confidence=0.9)
    # Target to stop the script.
    finish_target = pyautogui.locateOnScreen("img/post_finished.png", confidence=0.9)
    if post_button != None and finish_target == None:
        # Click on post button.
        pyautogui.click(post_button)
        # move cursor to the start position.
        pyautogui.moveTo(x, y)
        # Simulate human click timeout.
        time.sleep(random.uniform(0.2, 0.25))
    # Condition to stop the loop.
    # See image 'img/post_finished.png'.
    elif finish_target != None:
        sys.exit()