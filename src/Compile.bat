@Echo OFF
pip install keyboard pyinstaller
pyinstaller -i .ico --onefile PyLauncherMC.py
pause