@Echo OFF
python -m pip install keyboard pyinstaller
pyinstaller -i src\icon.ico --onefile src\PyLauncherMC.py
pause