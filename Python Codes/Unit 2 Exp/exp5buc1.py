# Implement a program to calculate the minimum number of operations
# (insertions, deletions, substitutions) required to convert one string into another

def levenshtein_distance(str1, str2, i, j, memo):
    if i == 0:
        return j
    if j == 0:
        return i
    if (i, j) in memo:
        return memo[(i, j)]
    if str1[i - 1] == str2[j - 1]:
        memo[(i, j)] = levenshtein_distance(str1, str2, i - 1, j - 1, memo)
    else:
        insert = levenshtein_distance(str1, str2, i, j - 1, memo)
        delete = levenshtein_distance(str1, str2, i - 1, j, memo)
        substitute = levenshtein_distance(str1, str2, i - 1, j - 1, memo)
        memo[(i, j)] = 1 + min(insert, delete, substitute)
    return memo[(i, j)]

def min_operations(str1, str2):
    memo = {}
    return levenshtein_distance(str1, str2, len(str1), len(str2), memo)

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    str1 = "kitten"
    str2 = "sitting"
    print(f"Minimum number of operations to convert '{str1}' to '{str2}': {min_operations(str1, str2)}")
