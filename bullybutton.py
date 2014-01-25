try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
import webbrowser

root = tk.Tk()
image = tk.PhotoImage(file='button.gif') # the button file itself, needs to be a gif (can be a static image, just save it as a .gif)

def web():
        url = 'websitehere' # insert a website to open upon button press here
        webbrowser.open(url, new=0, autoraise=True)
button = tk.Button(root, command=web, image=image, bd=0, height=62, width=117)
button.grid(row=2, column=2)

root.mainloop()
