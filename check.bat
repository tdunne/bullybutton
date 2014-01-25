@echo off
:start
tasklist /nh /fi "imagename eq bullybutton.exe" | find /i "bullybutton.exe" >nul && (
echo running
) || (
echo not running
cd C:\bullybutton\
wscript.exe "C:\bullybutton\invisible.vbs" "C:\bullybutton\dist\bullybutton.exe"
)
ping localhost -n 4 > Nul
goto start
