from tkinter import *
from tkinter import ttk
import time
import pyautogui


def post():
    actions(action="test", freq=0.5)


def destroy():
    actions(action="test", freq=2)


def stop():
    pass


def actions(action, freq):
    counter = 0
    image = "img/" + action + ".png"
    time.sleep(3)
    while counter < 5:
        x, y = pyautogui.position()
        button = pyautogui.locateOnScreen(image, confidence=0.8)
        if button is not None:
            pyautogui.click(button)
            pyautogui.moveTo(x, y)
            time.sleep(freq)
            button = None
            counter = 0
        else:
            counter += 1
            time.sleep(1)


window = Tk()
window.title("TSM Clicke Beta")
window.geometry("300x250+800+400")
window.resizable(False, False)
window.attributes("-alpha", 0.6)
window.attributes('-topmost', True)

ttk.Button(window, text="Post", command=post).pack(expand=True, fill=BOTH)
ttk.Button(window, text="Destroy", command=destroy).pack(expand=True, fill=BOTH)
# ttk.Button(window, text='STOP', command=stop).pack(expand=True, fill=BOTH)

window.mainloop()
