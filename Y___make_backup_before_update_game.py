import os
import json
import shutil
import urllib.request
import hashlib

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to the current directory
json_file_path = os.path.join(script_dir, "AddressablesJSON", "GeneratedJSON", "characters.json")
gamfs_path = os.path.join(os.path.expanduser("~"), "AppData", "LocalLow", "Unity", "Gamfs_BrownDust II")
backup_path = os.path.join(script_dir, "Backup")
github_json_url = "https://raw.githubusercontent.com/kxdekxde/browndust2-repacker/refs/heads/main/AddressablesJSON/GeneratedJSON/characters.json"

# Ensure the backup directory exists
os.makedirs(backup_path, exist_ok=True)

def check_and_update_json():
    """Check for updates to the JSON file on GitHub and update if needed."""
    try:
        # Download the GitHub version
        with urllib.request.urlopen(github_json_url) as response:
            github_json = response.read().decode('utf-8')
            github_data = json.loads(github_json)
        
        # Check if local file exists
        local_exists = os.path.exists(json_file_path)
        
        if local_exists:
            # Load local version
            with open(json_file_path, 'r', encoding='utf-8') as f:
                local_data = json.load(f)
            
            # Compare by converting to JSON strings
            if json.dumps(local_data, sort_keys=True) == json.dumps(github_data, sort_keys=True):
                print("Local JSON file is up to date.")
                return False
            else:
                print("Local JSON file is outdated.")
        else:
            print("Local JSON file not found. Downloading from GitHub.")
        
        # Update local file
        os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(github_data, f, indent=2)
        print("Local JSON file has been updated from GitHub.")
        return True
        
    except Exception as e:
        print(f"Error checking/updating JSON file: {e}")
        return False

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
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

def find_matching_folders(hashed_names, source_path, dest_path):
    """Find and copy folders matching hashed names."""
    copied_folders = set()

    for folder_name in os.listdir(source_path):
        folder_path = os.path.join(source_path, folder_name)

        if os.path.isdir(folder_path) and folder_name in hashed_names:
            dest_folder = os.path.join(dest_path, folder_name)

            # Skip if the folder already exists in the destination and the user doesn't want to overwrite
            if omit_existing_folder(dest_folder):
                continue

            try:
                shutil.copytree(folder_path, dest_folder)
                print(f"Copied folder: {folder_name} to {dest_folder}")
                copied_folders.add(folder_name)
            except shutil.Error as e:
                print(f"Error copying folder {folder_name}: {e}")
            except PermissionError as e:
                print(f"Permission error while copying folder {folder_name}: {e}")

    print("Copy process completed.")

def main():
    # Check and update JSON file from GitHub
    check_and_update_json()
    
    # Load JSON data
    json_data = load_json(json_file_path)

    if not json_data:
        return

    # Extract 'hashed_name' values
    hashed_names = {entry.get('hashed_name') for entry in json_data if 'hashed_name' in entry}

    if not hashed_names:
        print("No valid 'hashed_name' entries found in the JSON file.")
        return

    # Find and copy matching folders
    find_matching_folders(hashed_names, gamfs_path, backup_path)

if __name__ == "__main__":
    main()