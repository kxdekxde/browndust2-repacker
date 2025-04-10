@echo off
echo Running Python Scripts...



REM Run B___copy_raw_data_files.py
python B___copy_raw_data_files.py
if %errorlevel% neq 0 (
    echo B___copy_raw_data_files.py failed
    pause
    exit /b %errorlevel%
)
echo B___copy_raw_data_files.py ran successfully



REM Run C___delete_unnecessary_files.py
python C___delete_unnecessary_files.py
if %errorlevel% neq 0 (
    echo C___delete_unnecessary_files.py failed
    pause
    exit /b %errorlevel%
)
echo C___delete_unnecessary_files.py ran successfully



echo All scripts ran successfully.
exit
