from typing import List


# dp[i][j] 表示当数组剩下的部分为下标 i 到下标 j 时，即在下标范围[i,j] 中，能拿到的分数最大值。
#
# 只有当 i≤j 时，数组剩下的部分才有意义，因此当 i>j 时，dp[i][j]=0。
#
def coin_game(coins: List[int]) -> int:
    n = len(coins)
    prefix_sum = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + coins[i - 1]

    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for size in range(0, n):
        for l in range(1, n - size + 1):
            r = l + size
            if l == r:
                dp[l][r] = prefix_sum[r] - prefix_sum[l - 1]
            else:
                dp[l][r] = prefix_sum[r] - prefix_sum[l - 1] - min(dp[l + 1][r], dp[l][r - 1])
    return dp[1][n]


if __name__ == '__main__':
    coins = [4, 4, 9, 4]
    res = coin_game(coins)
    print(res)
    coins = [1, 2, 9999, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    res = coin_game(coins)
    print(res)
