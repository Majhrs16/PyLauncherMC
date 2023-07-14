@Echo OFF
pip install keyboard pyinstaller pillow
pyinstaller -i .ico --target-arch x86 --onefile PyLauncherMC.py
pause