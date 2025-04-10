from PIL import Image
import os
import UnityPy
import gc

# Configure UnityPy fallback version
UnityPy.config.FALLBACK_UNITY_VERSION = '2022.3.22f1'
ADD_PADDING = False

# Change the working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Paths for various folders
modded_assets_base_folder = os.path.join(script_dir, "Extracted Assets")
original_bundles_folder = os.path.join(script_dir, "Original Bundles")
repacked_base_folder = os.path.join(script_dir, "Repacked")

# Step 1: Check if the "Original Bundles" folder exists. If not, create it and exit.
if not os.path.exists(original_bundles_folder):
    os.makedirs(original_bundles_folder)
    print(f"Created {original_bundles_folder} folder. Add original bundles and rerun.")
    exit()

# Function to find modded assets corresponding to __data files
def get_modded_asset_path(data_file):
    for sub_root, sub_dirs, sub_files in os.walk(modded_assets_base_folder):
        for file in sub_files:
            if file == data_file:  # Match by file name
                return os.path.join(sub_root, file)
    return None  # Return None if no matching asset is found

# Function to free up system resources
def free_system_resources():
    print("Freeing up system resources...")
    gc.collect()
    try:
        with open("/proc/self/statm") as f:
            mem_usage = int(f.readline().split()[1]) * 4096 / (1024 * 1024)
            print(f"Memory usage reduced to: {mem_usage:.2f} MB")
    except FileNotFoundError:
        pass  # Skip if the system doesn't support this method
    print("System resources have been freed.")

# Step 2: Load one Unity bundle at a time and process assets
for root, dirs, files in os.walk(original_bundles_folder):
    for bundle_file in files:
        bundle_path = os.path.join(root, bundle_file)

        # Process only __data files
        if "__data" not in bundle_file:
            continue

        try:
            # Load the Unity bundle
            env = UnityPy.load(bundle_path)

            # A flag to check if the bundle was edited
            edited = False

            # Iterate through the objects (assets) in the loaded Unity bundle
            for obj in env.objects:
                try:
                    # Handling Texture2D (Images)
                    if obj.type.name == "Texture2D":
                        data = obj.read()
                        file_name = data.m_Name + ".png"

                        modded_file_path = get_modded_asset_path(file_name)

                        if modded_file_path:
                            print(f"Replacing {file_name} in {bundle_path} with {modded_file_path}")

                            # Load the modified image
                            pil_img = Image.open(modded_file_path).convert("RGBA")
                            new_width, new_height = pil_img.size

                            # Determine texture format based on aspect ratio
                            if new_width == new_height:
                                # Square image: use DXT5
                                texture_format = 12  # DXT5
                            else:
                                # Non-square image: use RGBA32
                                texture_format = 4  # RGBA32

                            # Update texture properties
                            data.m_Width = new_width
                            data.m_Height = new_height
                            data.m_TextureFormat = texture_format
                            data.image = pil_img
                            data.save()
                            edited = True

                    # Handling TextAsset (Text Files)
                    elif obj.type.name == "TextAsset":
                        data = obj.read()
                        file_name = data.m_Name

                        modded_file_path = get_modded_asset_path(file_name)

                        if modded_file_path:
                            print(f"Replacing {file_name} in {bundle_path} with {modded_file_path}")

                            with open(modded_file_path, "rb") as f:
                                data.m_Script = f.read().decode("utf-8", "surrogateescape")
                            data.save()
                            edited = True

                except Exception as e:
                    print(f"Error processing asset in {bundle_file}: {e}")

            # Step 3: If the bundle was edited, save it
            if edited:
                # Create the directory for repacked bundles if it doesn't exist
                relative_bundle_path = os.path.relpath(bundle_path, original_bundles_folder)
                repacked_bundle_path = os.path.join(repacked_base_folder, relative_bundle_path)

                os.makedirs(os.path.dirname(repacked_bundle_path), exist_ok=True)

                try:
                    with open(repacked_bundle_path, "wb") as f:
                        bundle_data = env.file.save(packer="lz4")
                        f.write(bundle_data)

                        if ADD_PADDING:
                            current_size = f.tell()
                            padding_needed = (0x10 - (current_size % 0x10)) % 0x10
                            if padding_needed:
                                f.write(b'\x00' * padding_needed)

                    print(f"Saved modified bundle to {repacked_bundle_path}")

                except Exception as e:
                    print(f"Error saving repacked bundle {bundle_file}: {e}")

        except Exception as e:
            print(f"Error processing bundle {bundle_file}: {e}")

# Free system resources after processing and saving all bundles
free_system_resources()
