# Implement anchors (^, $) to match the start and end of strings,
# and use word boundaries (\b) to find whole words.

import re

def search_pattern(text, pattern):
    results = {}

    start_match = re.search(f'^{pattern}', text)
    results['start_match'] = start_match.group() if start_match else None

    end_match = re.search(f'{pattern}$', text)
    results['end_match'] = end_match.group() if end_match else None

    whole_word_match = re.findall(rf'\b{pattern}\b', text)
    results['whole_word_match'] = whole_word_match if whole_word_match else None

    return results

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")

    text = "Python is great. Pythonic is also great."
    pattern = "Python"
    matches = search_pattern(text, pattern)
    print(matches)
