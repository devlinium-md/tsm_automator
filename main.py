from tkinter import *
from tkinter import ttk
import actions

root = Tk()
root.title("TSM Clicke")
root.geometry("300x250+800+400")
root.resizable(False,False)
root.attributes("-alpha", 0.5)

destroy = ttk.Button(text="Destroy", command=actions.post_or_destroy(action="destroy", freq=2))
destroy.pack()
post = ttk.Button(text="Post", command=actions.post_or_destroy(action="post", freq=0.5))
post.pack()


root.mainloop()