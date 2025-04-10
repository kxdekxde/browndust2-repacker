import os

# Define the list of folders to create
folders = [
    "Backup",
    "Extracted Assets",
    "Modded Bundles",
    "Original Bundles",
    "Repacked"
]

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Loop through each folder and create it in the script's directory if it doesn't exist
for folder in folders:
    folder_path = os.path.join(script_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder}")
    else:
        print(f"Folder already exists: {folder}")

print("All specified folders have been created or already exist.")
