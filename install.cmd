set "currentDirectory=%cd%
pyinstaller --distpath %currentDirectory% -i favicon.ico --onefile Macro-Maker.py
pause