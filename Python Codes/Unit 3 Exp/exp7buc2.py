# Utilize parentheses to create capturing groups and
# learn to extract or manipulate parts of your matches.

import re

def extract_info(text):
    pattern = r'(\b\w+\b) (\b\w+\b)'
    matches = re.findall(pattern, text)
    manipulated_results = [(first.capitalize(), last.upper()) for first, last in matches]
    return matches, manipulated_results

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")

    text = "hello world welcome to python programming"
    matches, manipulated_results = extract_info(text)

    print("Matches:", matches)
    print("Manipulated Results:", manipulated_results)
