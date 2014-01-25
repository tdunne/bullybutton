try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
import os

root = tk.Tk()
image = tk.PhotoImage(file='button.gif') # the button file itself, needs to be a gif (can be a static image, just save it as a .gif)

def button():
    os.startfile("mail.exe")
button = tk.Button(root, command=button, image=image, bd=0, height=62, width=117)
button.grid(row=2, column=2)

root.mainloop()
