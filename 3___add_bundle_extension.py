import os

# Define the directory paths relative to the current script's location
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
modded_folder_path = os.path.join(current_dir, "Modded Bundles")
original_folder_path = os.path.join(current_dir, "Original Bundles")

# Function to process and rename files in a given folder
def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Check if the current file is named "__data"
            if filename == "__data":
                # New file name with .bundle extension
                new_file_name = filename + ".bundle"
                new_file_path = os.path.join(root, new_file_name)

                # Rename the file
                os.rename(file_path, new_file_path)
                print(f"Renamed {file_path} to {new_file_path}")

# Process both folders
process_folder(modded_folder_path)
process_folder(original_folder_path)
