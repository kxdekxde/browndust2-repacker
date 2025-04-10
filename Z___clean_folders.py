import os
import shutil

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory

# Define the folder paths relative to the current script's directory
extracted_assets_folder = os.path.join(script_dir, "Extracted Assets")  # "Extracted Assets"
modded_bundles_folder = os.path.join(script_dir, "Modded Bundles")      # "Modded Bundles"
original_bundles_folder = os.path.join(script_dir, "Original Bundles")  # "Original Bundles"

# Function to delete files inside a folder
def delete_files_in_folder(folder_path):
    if os.path.exists(folder_path):
        print(f"Deleting files in {folder_path}...")
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Optionally delete subfolders too
                    print(f"Deleted directory: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        print(f"{folder_path} does not exist.")

# Delete files in each folder
delete_files_in_folder(extracted_assets_folder)
delete_files_in_folder(modded_bundles_folder)
delete_files_in_folder(original_bundles_folder)

print("All specified files have been deleted.")
