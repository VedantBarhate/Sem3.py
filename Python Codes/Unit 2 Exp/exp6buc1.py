
def min_coins(denominations, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in denominations:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    denominations = [1, 2, 5]
    amount = 11
    print(min_coins(denominations, amount))  # Output: 3 (5 + 5 + 1)
