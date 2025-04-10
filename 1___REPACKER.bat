@echo off
echo Running Python Scripts...



REM Run 2___rename_subfolders.py
python 2___rename_subfolders.py
if %errorlevel% neq 0 (
    echo 2___rename_subfolders.py failed
    pause
    exit /b %errorlevel%
)
echo 2___rename_subfolders.py ran successfully



REM Run 3___add_bundle_extension.py
python 3___add_bundle_extension.py
if %errorlevel% neq 0 (
    echo 3___add_bundle_extension.py failed
    pause
    exit /b %errorlevel%
)
echo 3___add_bundle_extension.py ran successfully



REM Run 4___extract_assets.py
python 4___extract_assets.py
if %errorlevel% neq 0 (
    echo 4___extract_assets.py failed
    pause
    exit /b %errorlevel%
)
echo 4___extract_assets.py ran successfully



REM Run 5___bingle_kxde_repacker_LZ4_compressor___auto-RGBA32.py
python 5___bingle_kxde_repacker_LZ4_compressor___auto-RGBA32.py
if %errorlevel% neq 0 (
    echo 5___bingle_kxde_repacker_LZ4_compressor___auto-RGBA32.py failed
    pause
    exit /b %errorlevel%
)
echo 5___bingle_kxde_repacker_LZ4_compressor___auto-RGBA32.py ran successfully



REM Run 6___remove_bundle_extension.py
python 6___remove_bundle_extension.py
if %errorlevel% neq 0 (
    echo 6___remove_bundle_extension.py failed
    pause
    exit /b %errorlevel%
)
echo 6___remove_bundle_extension.py ran successfully



echo All scripts ran successfully.
exit
