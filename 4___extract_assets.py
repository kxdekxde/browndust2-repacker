import os
import shutil
import UnityPy

UnityPy.config.FALLBACK_UNITY_VERSION = '2022.2.17f1'
ADD_PADDING = False

# Define the paths relative to the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
bundles_folder = os.path.join(current_dir, "Modded Bundles")  # Path to the "Modded Bundles" folder
export_folder = os.path.join(current_dir, "Extracted Assets")  # Path to the "Extracted Assets" folder

# Ensure the export folder exists
if not os.path.exists(export_folder):
    os.makedirs(export_folder)

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
    # Skip if it's the '.' folder or other invalid folder names
    if dest_folder == '.' or dest_folder == '..' or dest_folder == '':
        return True

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

# Traverse "Modded Bundles" recursively to maintain folder structure
for root, dirs, files in os.walk(bundles_folder):
    # Calculate the relative path from "Modded Bundles" to the current directory
    relative_path = os.path.relpath(root, bundles_folder)

    # Skip the '.' (current directory) entry if it's incorrectly interpreted
    if relative_path == ".":
        continue

    # Define the corresponding export path in "Extracted Assets"
    export_path = os.path.join(export_folder, relative_path)

    # Skip if the folder already exists in the destination and the user doesn't want to overwrite
    if omit_existing_folder(export_path):
        continue

    # Ensure the export path exists
    if not os.path.exists(export_path):
        os.makedirs(export_path)

    # Process each .bundle file in the current folder
    for bundle_filename in files:
        bundle_path = os.path.join(root, bundle_filename)

        # Check if the file is a Unity bundle
        if os.path.isfile(bundle_path) and bundle_filename.endswith(".bundle"):
            print(f"Processing {bundle_filename}")

            try:
                # Load the Unity bundle file
                env = UnityPy.load(bundle_path)

                # Iterate through the objects in the bundle
                for obj in env.objects:
                    try:
                        if obj.type.name == "Texture2D":
                            # Export Texture2D assets
                            data = obj.read()
                            texture_name = f"{data.m_Name}.png"  # Use the texture's m_Name
                            texture_path = os.path.join(export_path, texture_name)

                            # Save the texture as a PNG
                            data.image.save(texture_path)
                            print(f"Exported Texture2D: {texture_name} to {export_path}")

                        elif obj.type.name == "TextAsset":
                            # Export TextAsset files
                            data = obj.read()
                            text_name = data.m_Name  # Use the asset's name without .txt extension
                            text_path = os.path.join(export_path, text_name)  # No extension

                            # Save the text file, handling surrogate characters
                            with open(text_path, "wb") as f:
                                # Encode the script with surrogateescape to handle invalid characters
                                f.write(data.m_Script.encode("utf-8", "surrogateescape"))
                            print(f"Exported TextAsset: {text_name} to {export_path}")

                    except Exception as e:
                        print(f"Error exporting object: {e}")

            except Exception as e:
                print(f"Error processing bundle {bundle_filename}: {e}")
