
import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Successfully converted {csv_file_path} to {json_file_path}")

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    csv_file_path = 'exp9_input.csv'
    json_file_path = 'exp9_output.json'
    csv_to_json(csv_file_path, json_file_path)
