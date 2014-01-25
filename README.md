bullybutton
===========

A school project. A simple python script to create a button that opens a website when you click it. Other scripts to ensure the button runs continuously and a script to run files invisibly.

********
Installation

Place all files (scripts and image (must be saved as button.gif)) in C:\bullybutton. If you wish to place the files elsewhere, you will have to modify the code. If you desire, change the image and the website URL and use this as a quick link to any site you want.

********
Information About Files
* invisible.vbs: A VBScript that starts a file invisibly, from the command line. 
* Syntax: wscript.exe "C:\path\to\script\invisible.vbs" "C:\path\to\file\to\start\invisibly\file.suffix" 
* See start.bat for an example.

* check.bat: Checks if bullybutton.exe is already running. If it is, do nothing. If not, restart it invisibly (removes the background window, only the button displays). This check executes every four seconds.

* start.bat: runs check.bat invisibly

Once start.bat is run, check.bat will begin to execute (invisibly). If/when it detects that bullybutton.exe has been closed, it will restart it (again, invisibly, so that only the button displays).

********
Because check.bat runs invisibly, the only way to kill it is through Task Manager or by deleting check.bat. I suggest keeping a backup of check.bat in case the former method fails and you have to use the latter.

********
My Button

![](http://i.imgur.com/EABVpXK.gif)
