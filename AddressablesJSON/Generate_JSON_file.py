import csv
import json
import hashlib
import os

# Function to hash a name
def hash_name(name):
    return hashlib.md5(name.encode('utf-8')).hexdigest()

# Function to load the CSV file and process its data
def process_csv_to_json(csv_file, json_folder):
    result = []
    
    # Ensure the output folder exists
    os.makedirs(json_folder, exist_ok=True)

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))
    print(f"Script directory: {script_dir}")

    # Construct the path to the CSV file relative to the script's directory
    csv_file_path = os.path.join(script_dir, csv_file)

    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            current_character = None
            
            for row in csv_reader:
                # Handle rows with a valid character name
                if row['CHARACTER']:
                    current_character = row['CHARACTER']
                
                # Process each row with file_id, costume, idle, cutscene data
                if row['ID'] and row['COSTUME']:
                    file_id = row['ID']
                    costume = row['COSTUME']
                    
                    # Add entry for 'idle' type (if present)
                    if row['IDLE']:
                        result.append({
                            "character": current_character,
                            "file_id": file_id,
                            "costume": costume,
                            "type": "idle",
                            "hashed_name": row['IDLE']
                        })
                    else:
                        result.append({
                            "character": current_character,
                            "file_id": file_id,
                            "costume": costume,
                            "type": "idle",
                            "hashed_name": ""  # Empty hashed_name if no idle value
                        })
                    
                    # Add entry for 'cutscene' type (if present)
                    if row['CUTSCENE']:
                        result.append({
                            "character": current_character,
                            "file_id": file_id,
                            "costume": costume,
                            "type": "cutscene",
                            "hashed_name": row['CUTSCENE']
                        })
                    else:
                        result.append({
                            "character": current_character,
                            "file_id": file_id,
                            "costume": costume,
                            "type": "cutscene",
                            "hashed_name": ""  # Empty hashed_name if no cutscene value
                        })

        # Define the relative output JSON file path
        json_file_path = os.path.join(script_dir, json_folder, 'characters.json')
        
        # Write the processed data to a JSON file
        with open(json_file_path, mode='w', encoding='utf-8') as json_out:
            json.dump(result, json_out, indent=4)

        print(f"JSON file has been saved to '{json_file_path}'.")

    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found in the directory '{script_dir}'.")

# Set the file paths
csv_file_name = 'BD2 Characters - Characters.csv'
json_folder_name = 'GeneratedJSON'

# Process the CSV and generate the JSON
process_csv_to_json(csv_file_name, json_folder_name)
