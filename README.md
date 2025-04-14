# Brown Dust 2 Repacker
A simple tool useful to mod [Brown Dust 2](https://www.browndust2.com/en-us/) bundles. Thanks to Bingle for the help with this repacker.


#### NOTE: This tool only works with .skel files, not with .json files. To use mods with .json files you can use BrownDustX by Synae.

## Before to use this tool:

  - Download and install [.NET SDK 8](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/sdk-8.0.404-windows-x64-installer).
  - Download and install [Python](https://www.python.org/downloads/), along with all of the addons included (pip, etc).
  - Download and install [Microsoft C++ Build Tools](https://aka.ms/vs/17/release/vs_BuildTools.exe), and after that install the necessary libraries following [this video](https://files.catbox.moe/vqsuix.mp4).

  - Open CMD and type: 
    ```
	pip install UnityPy
	```
	And hit enter to install UnityPy for Python.



## Usage for repack:

1. Run the script _0___CREATE_MISSING_FOLDERS.py_ to get the needed folders.
2. Run the script _Y___make_backup_before_update_game.py_ before to update your game if you already have mods located in the game folder. The script will make a backup of your mods to the folder "Backup" so you will not lose your mods when you update your game.
3. Update your game with no worries.
4. Go to the folder "Backup" and copy the folders there to "Modded Bundles".
5. Run _A___GET_RAW_FILES.bat_, the .bat file will run the scripts to get the raw files from the game folders and it will make a copy to the folder "Original Bundles".
6. Run _1___REPACKER.bat_ to start the repacking process. And now just wait, the Terminal window will close when the repacking is done.
7. If everything worked with no issues you will see your repacked files saved in the folder "Repacked".
8. Copy those folders from "Repacked" and paste them in your game folder  "Gamfs_BrownDust II" manually, located in %USERPROFILE%\AppData\LocalLow\Unity\Gamfs_BrownDust II.
9. Replace the files and that's it.

NOTE: The script _Z___clean_folders.py_ is just to clean the folders used by the tool when you finished to repack your mods, so you can just ignore this script and delete the files or folders you don't need anymore manually. This script doesn't clean the folder "Repacked".


## Usage to install mods:

1. Run _D___copy_raw_data_files_2.py_ to copy the raw files from the game folder directly to the folders "Original Bundles" and "Modded Bundles", and run _C___delete_unnecessary_files.py_ to remove any not necessary file inside these folders.
2. Run _3___add_bundle_extension.py_.
3. Run _4___extract_assets.py_ and wait until the process finishes.
4. Here I got [some modded assets](https://mega.nz/folder/kDsGiCDC#aTgZj_2lQJ4Qxj4NI-duYg) to use as sample. Or you can download any other mod where the creator provided the .atlas/.skel/.png assets.
5. Go to the folder "Extracted Assets" and you will see some folders that contain the raw assets We extracted previously on step 3 (various files .atlas / .skel / .png).
6. Copy the modded assets you downloaded and paste them in their corresponding locations replacing the raw assets.
7. Run _5___bingle_kxde_repacker_LZ4_compressor___auto-RGBA32.py_ and the tool will start to repack the files using the modded assets you replaced in "Extracted Assets". The Terminal window should close when the repacking is done.
8. Run _6___remove_bundle_extension.py_.
9. If everything worked with no issues you will see your repacked files saved in the folder "Repacked".
10. Copy those folders from "Repacked" and paste them in your game folder  "Gamfs_BrownDust II" manually, located in `%USERPROFILE%\AppData\LocalLow\Unity\Gamfs_BrownDust II`.
11. Replace the files and that's it.


## Usage to install your own mods:

If you make your own mods you can use this tool to save some time too. You can use this tool to extract/export the assets to "Extracted Assets" and then you can start to work with the assets from there, save the changes to the assets and when you're ready to import the assets back to the bundles you can run _5___bingle_kxde_repacker_LZ4_compressor___auto-RGBA32.py_ and _6___remove_bundle_extension.py_ and your modified files will be saved to "Repacked". Then just move them to your game folder and that's it.


Happy modding! ^‿^
