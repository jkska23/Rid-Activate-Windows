import os

os.system("start /wait cmd /c {slmgr.vbs /rearm}")
os.system("shutdown /r /t 1")