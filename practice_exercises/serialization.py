import json

def process_json(data: dict, filename: str) -> dict:
    # Step 1: Serialize the dictionary to a JSON file
    with open(filename, 'w') as file:
        json.dump(data, file)

    # Step 2: Deserialize the JSON file back into a dictionary
    with open(filename, 'r') as file:
        loaded_data = json.load(file)

    # Step 3: Return the deserialized dictionary
    return loaded_data
