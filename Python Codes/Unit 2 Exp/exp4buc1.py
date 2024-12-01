# Create a program to calculate the number of unique paths 
# from the top-left corner to the bottom-right corner of a grid, moving only right or down

def unique_paths(m, n, memo=None):
    if memo is None:
        memo = {}
    if m == 1 and n == 1:
        return 1
    if m < 1 or n < 1:
        return 0
    if (m, n) in memo:
        return memo[(m, n)]
    memo[(m, n)] = unique_paths(m - 1, n, memo) + unique_paths(m, n - 1, memo)
    return memo[(m, n)]

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    result = unique_paths(3,3)
    print("Number of unique paths:", result)
