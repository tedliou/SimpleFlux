@echo off
WHERE uv
IF %ERRORLEVEL% NEQ 0 CALL "tools\install-uv.bat"
call "tools\install-python.bat"

WHERE scoop
IF %ERRORLEVEL% NEQ 0 call "tools\install-scoop.bat"

WHERE ffmpeg
IF %ERRORLEVEL% NEQ 0 call "tools\install-ffmpeg.bat"

WHERE go
IF %ERRORLEVEL% NEQ 0 call "tools\install-go.bat"

WHERE lux
IF %ERRORLEVEL% NEQ 0 call "tools\install-lux.bat"

uv sync
uv run pyinstaller -w -F main.py

move "dist\main.exe" "SimpleLux.exe"

powershell -ExecutionPolicy Bypass -File "%~dp0\tools\create-shortcut.ps1"

start %CD%\SimpleLux.exe
