from typing import List


def max_score(dp, curSum, l, r) -> int:
    if dp[l][r]:
        return dp[l][r]
    total = curSum[r+1]-curSum[l]
    if l == r:
        dp[l][r] = total
    else:
        left = max_score(dp, curSum, l + 1, r)
        right = max_score(dp, curSum, l, r - 1)
        dp[l][r] = total - min(left, right)
    return dp[l][r]


def coin_game(coins: List[int]) -> int:
    n = len(coins) + 1
    dp = [[0] * n for _ in range(n)]
    prefixSum = [0] * (len(coins) + 1)
    for i in range(1, len(prefixSum)):
        prefixSum[i] = prefixSum[i - 1] + coins[i - 1]
    print(prefixSum)
    return max_score(dp, prefixSum, 0, len(coins)-1)

if __name__ == '__main__':
    coins = [4, 4, 9, 4]
    res = coin_game(coins)
    print(res)
    coins = [1, 2, 9999, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    res = coin_game(coins)
    print(res)
