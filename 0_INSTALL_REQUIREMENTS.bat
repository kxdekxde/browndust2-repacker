@echo off
setlocal

REM Check if Python 3.13 is installed
python --version 2>nul | findstr /i "3.13" >nul
if %errorlevel% neq 0 (
    echo Python 3.13 is not installed. Downloading and installing Python 3.13...

    REM Download Python 3.13 installer
    echo Downloading Python 3.13 installer...
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe -OutFile python-3.13.3-amd64.exe"

    REM Run the Python installer silently
    echo Installing Python 3.13...
    python-3.13.3-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

    REM Check if installation was successful
    python --version 2>nul | findstr /i "3.13" >nul
    if %errorlevel% neq 0 (
        echo Python 3.13 installation failed. Please install it manually.
        exit /b
    )

    REM Delete the installer after installation
    del python-3.13.3-amd64.exe
    echo Python 3.13 installation completed successfully.
) else (
    echo Python 3.13 is already installed.
)

REM Install dependencies from requirements.txt
if exist requirements.txt (
    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo An error occurred during pip installation.
        exit /b
    )
) else (
    echo requirements.txt not found. Skipping dependency installation.
)

pause
