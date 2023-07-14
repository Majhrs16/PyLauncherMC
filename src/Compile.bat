@Echo OFF
pip install keyboard pyinstaller pillow
pyinstaller -i .ico --target-arch universal2 --onefile PyLauncherMC.py
pause