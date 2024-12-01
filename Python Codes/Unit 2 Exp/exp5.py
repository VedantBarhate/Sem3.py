# Python implementation of Top-Down DP of LCS problem

def lcs(S1, S2, m, n, memo):
    # Base Case
    if m == 0 or n == 0:
        return 0
    # Already exists in the memo table
    if memo[m][n] != -1:
        return memo[m][n]
    # Match
    if S1[m-1] == S2[n-1]:
        memo[m][n] = 1 + lcs(S1, S2, m-1, n-1, memo)
        return memo[m][n]
    # No match: take the maximum of excluding one character from either S1 or S2
    memo[m][n] = max(lcs(S1, S2, m, n-1, memo),
                     lcs(S1, S2, m-1, n, memo))
    return memo[m][n]

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    S1 = "AGGTAB"
    S2 = "GXTXAYB"
    m = len(S1)
    n = len(S2)
    memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    print("Length of LCS is", lcs(S1, S2, m, n, memo))
