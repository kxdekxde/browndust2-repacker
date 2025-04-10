import os
import json
import shutil

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to the current directory
json_file_path = os.path.join(script_dir, "AddressablesJSON", "GeneratedJSON", "characters.json")
gamfs_path = os.path.join(os.path.expanduser("~"), "AppData", "LocalLow", "Unity", "Gamfs_BrownDust II")
modded_bundles_path = os.path.join(script_dir, "Modded Bundles")
original_bundles_path = os.path.join(script_dir, "Original Bundles")

# Ensure the original bundles directory exists
os.makedirs(original_bundles_path, exist_ok=True)

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: JSON file not found at {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON: {e}")
        return None

def get_user_input(prompt):
    """Function to get case-insensitive user input."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ["yes", "no"]:
            return user_input
        else:
            print("Invalid input. Please respond with 'Yes' or 'No'.")

def omit_existing_folder(dest_folder):
    """Ask the user if they want to overwrite an existing folder."""
    if os.path.exists(dest_folder):
        user_input = get_user_input(f"The folder '{dest_folder}' already exists in the destination folder, do you wish to overwrite it? (Yes/No): ")
        if user_input == "yes":
            # Remove the existing folder before copying
            try:
                shutil.rmtree(dest_folder)  # Remove the folder and its contents
                print(f"Existing folder '{dest_folder}' has been removed.")
                return False  # Proceed with overwriting
            except Exception as e:
                print(f"Error removing existing folder '{dest_folder}': {e}")
                return True  # Skip if we can't remove the folder
        else:
            print(f"Skipping folder: {dest_folder}.")
            return True  # Skip if no overwrite
    return False

def find_and_copy_matching_folders(source_path, target_path, dest_path):
    """Find and copy folders from source_path to dest_path if they exist in target_path."""
    target_folders = set(os.listdir(target_path))

    for folder_name in os.listdir(source_path):
        folder_path = os.path.join(source_path, folder_name)

        if os.path.isdir(folder_path) and folder_name in target_folders:
            dest_folder = os.path.join(dest_path, folder_name)

            # Skip if the folder already exists in the destination and the user doesn't want to overwrite
            if omit_existing_folder(dest_folder):
                continue

            try:
                shutil.copytree(os.path.join(target_path, folder_name), dest_folder)
                print(f"Copied folder: {folder_name} from {target_path} to {dest_folder}")
            except shutil.Error as e:
                print(f"Error copying folder {folder_name}: {e}")
            except PermissionError as e:
                print(f"Permission error while copying folder {folder_name}: {e}")

    print("Copy process completed.")

def main():
    # Load JSON data
    json_data = load_json(json_file_path)

    if not json_data:
        return

    # Perform folder comparison and copying
    find_and_copy_matching_folders(modded_bundles_path, gamfs_path, original_bundles_path)

if __name__ == "__main__":
    main()
