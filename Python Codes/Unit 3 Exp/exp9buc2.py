# Create a script that reads a JSON file containing product information
# and filters out products that are below a specified price,
# saving the results to a new JSON file.

import json

def filter_products(input_json_file_path, output_json_file_path, min_price):
    with open(input_json_file_path, 'r') as input_file:
        products = json.load(input_file)
    filtered_products = [product for product in products if product['price'] >= min_price]
    with open(output_json_file_path, 'w') as output_file:
        json.dump(filtered_products, output_file)
    print(f"Successfully filtered products and saved to {output_json_file_path}")

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    input_json_file_path = 'exp9buc2_input.json'
    output_json_file_path = 'exp9buc2_output.json'
    min_price = 5000

    filter_products(input_json_file_path, output_json_file_path, min_price)
