import re
from tkinter import *
from tkinter import ttk
import time
import pyautogui


def post():
    actions(action="post", freq=0.5)


def cancel():
    actions(action="cancel", freq=0.5)


def destroy():
    actions(action="destroy", freq=2)


def button_timeout_timer():
    value = entry.get()
    try:
        value = float(value)
        print(value)
        print(type(value))
        if 0.0 < value < 10.0:
            return value
        else:
            entry.delete(0, END)
    except ValueError:
        print(value)
        print(type(value))
        entry.delete(0, END)


def stop():
    pass


def actions(action, freq):
    counter = 0
    image = "img/" + action + ".png"
    timer = button_timeout_timer()
    print(timer)
    if timer is not None:
        time.sleep(3)
        while counter < 5:
            x, y = pyautogui.position()
            button = pyautogui.locateOnScreen(image, confidence=0.8)
            if button is not None:
                pyautogui.click(button)
                pyautogui.moveTo(x, y)
                time.sleep(timer)
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
ttk.Button(window, text="Cancel", command=cancel).pack(expand=True, fill=BOTH)
ttk.Button(window, text="Destroy", command=destroy).pack(expand=True, fill=BOTH)
entry = ttk.Entry()
entry.insert(0, "5")
entry.pack(anchor=N, padx=8, pady=8)

window.mainloop()
