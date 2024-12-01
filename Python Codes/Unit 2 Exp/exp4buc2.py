# Develop a program to calculate the nth Catalan number,
# which appears in various combinatorial problems.

def catalan_number(n, memo=None):
    if memo is None:
        memo = {}
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    catalan_n = 0
    for i in range(n):
        catalan_n += catalan_number(i, memo) * catalan_number(n - i - 1, memo)
    memo[n] = catalan_n
    return catalan_n

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    n = 3
    print(f"The {n}th Catalan number is: {catalan_number(n)}")
