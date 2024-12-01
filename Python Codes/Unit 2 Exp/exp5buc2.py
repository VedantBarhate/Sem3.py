# Develop a program to find the most efficient way to multiply a chain of matrices.



import sys

def matrix_chain_memo(p, i, j, memo):
    if i == j:
        return 0
    if memo[i][j] != -1:
        return memo[i][j]
    min_operations = sys.maxsize
    for k in range(i, j):
        count = (
            matrix_chain_memo(p, i, k, memo) +
            matrix_chain_memo(p, k + 1, j, memo) +
            p[i - 1] * p[k] * p[j]
        )
        if count < min_operations:
            min_operations = count
    memo[i][j] = min_operations
    return memo[i][j]

def matrix_chain_order_memo(p):
    n = len(p) - 1
    memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    return matrix_chain_memo(p, 1, n, memo)

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    dimensions = [30, 35, 15, 5, 10, 20, 25]
    min_ops = matrix_chain_order_memo(dimensions)
    print(f"Minimum number of multiplications: {min_ops}")
