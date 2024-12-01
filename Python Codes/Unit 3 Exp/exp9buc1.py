# Develop a script that reads a JSON file, modifies its content,
# and writes the updated data back to a new JSON file.

import json

def modify_json(input_json_file_path, output_json_file_path):
    with open(input_json_file_path, 'r') as input_file:
        data = json.load(input_file)
    for item in data:
        if isinstance(item, dict):
            item['new_key'] = 'new_value'
    with open(output_json_file_path, 'w') as output_file:
        json.dump(data, output_file)
    print(f"Successfully modified and saved data to {output_json_file_path}")

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    input_json_file_path = 'exp9buc1_input.json'
    output_json_file_path = 'exp9buc1_output.json'
    modify_json(input_json_file_path, output_json_file_path)
