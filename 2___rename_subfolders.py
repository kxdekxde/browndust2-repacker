import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths for the directories
original_bundles_path = os.path.join(script_dir, "Original Bundles")
modded_bundles_path = os.path.join(script_dir, "Modded Bundles")

# Get all folder names from the specified directory
def get_all_folder_names(path):
    folder_names = []
    for root, dirs, _ in os.walk(path):
        for folder in dirs:
            # Only take the top-level folders
            if root == path:
                folder_names.append(folder)
    return folder_names

# Get all subfolder names from the specified directory
def get_all_subfolder_names(path):
    subfolder_names = []
    for root, dirs, _ in os.walk(path):
        for folder in dirs:
            # Only take the immediate subfolders
            if os.path.dirname(os.path.join(root, folder)) == path:
                subfolder_names.append(folder)
    return subfolder_names

# Compare top-level folders and rename subfolders if needed
def compare_and_rename_folders():
    # Get all top-level folder names from Original Bundles and Modded Bundles
    original_folder_names = get_all_folder_names(original_bundles_path)
    modded_folder_names = get_all_folder_names(modded_bundles_path)

    # Print the folder names for debugging
    print("Original Bundles Top-Level Folder Names:", original_folder_names)
    print("Modded Bundles Top-Level Folder Names:", modded_folder_names)

    # Compare top-level folder names
    for original_folder in original_folder_names:
        print(f"\nProcessing top-level folder: '{original_folder}'")

        # Check if the top-level folder exists in Modded Bundles
        if original_folder in modded_folder_names:
            print(f"Top-level folder '{original_folder}' matches. Now checking subfolders...")

            # Get subfolder paths
            original_subfolder_path = os.path.join(original_bundles_path, original_folder)
            modded_subfolder_path = os.path.join(modded_bundles_path, original_folder)

            # Get subfolder names from both directories
            original_subfolders = get_all_subfolder_names(original_subfolder_path)
            modded_subfolders = get_all_subfolder_names(modded_subfolder_path)

            print("Original Subfolders:", original_subfolders)
            print("Modded Subfolders:", modded_subfolders)

            # Rename subfolders in Modded Bundles to match those in Original Bundles
            for original_subfolder in original_subfolders:
                if original_subfolder in modded_subfolders:
                    original_full_path = os.path.join(original_subfolder_path, original_subfolder)
                    modded_full_path = os.path.join(modded_subfolder_path, original_subfolder)

                    print(f"Subfolder '{modded_full_path}' matches. No renaming needed.")
                else:
                    print(f"Renaming subfolder in Modded Bundles to match Original Bundles...")

                    # Renaming the subfolder in Modded Bundles to match the one in Original Bundles
                    for modded_subfolder in modded_subfolders:
                        modded_subfolder_full_path = os.path.join(modded_subfolder_path, modded_subfolder)
                        new_subfolder_full_path = os.path.join(modded_subfolder_path, original_subfolder)

                        print(f"Attempting to rename '{modded_subfolder_full_path}' to '{new_subfolder_full_path}'...")

                        if not os.path.exists(new_subfolder_full_path):
                            print(f"Renaming '{modded_subfolder_full_path}' to '{new_subfolder_full_path}'")
                            os.rename(modded_subfolder_full_path, new_subfolder_full_path)
                        else:
                            print(f"Cannot rename '{modded_subfolder_full_path}' to '{new_subfolder_full_path}': Target already exists.")
        else:
            print(f"No match found for top-level folder '{original_folder}' in Modded Bundles.")

def main():
    compare_and_rename_folders()

if __name__ == "__main__":
    main()
