import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths to parent folders
modded_bundles_path = os.path.join(script_dir, "Modded Bundles")
backup_path = os.path.join(script_dir, "Backup")
original_bundles_path = os.path.join(script_dir, "Original Bundles")

# List of parent folders to process
parent_folders = [modded_bundles_path, backup_path, original_bundles_path]

def delete_unwanted_files(folder_path):
    """Iterate through folders and delete files named '__info' or '__lock'."""
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name in ["__info", "__lock"]:
                file_path = os.path.join(root, file_name)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

def main():
    for parent_folder in parent_folders:
        if os.path.exists(parent_folder):
            print(f"Processing folder: {parent_folder}")
            delete_unwanted_files(parent_folder)
        else:
            print(f"Folder does not exist: {parent_folder}")

if __name__ == "__main__":
    main()
