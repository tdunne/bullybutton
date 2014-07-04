"""Copyright 2014 Tim Dunne

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License."""
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
