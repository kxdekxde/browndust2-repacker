import os

# Define the directory path relative to the current script's location
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
main_folder_path = os.path.join(current_dir, "Repacked")

# Iterate through all files in the main folder and its subfolders
for root, dirs, files in os.walk(main_folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)

        # Check if the current file has a .bundle extension
        if filename.endswith(".bundle"):
            # New file name by removing the .bundle extension
            new_file_name = filename[:-7]  # Remove the last 7 characters (".bundle")
            new_file_path = os.path.join(root, new_file_name)

            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed {file_path} to {new_file_path}")
