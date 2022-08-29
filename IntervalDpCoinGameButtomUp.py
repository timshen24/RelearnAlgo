from typing import List


# dp[i][j] 表示当数组剩下的部分为下标 i 到下标 j 时，即在下标范围[i,j] 中，能拿到的分数最大值。
#
# 只有当 i≤j 时，数组剩下的部分才有意义，因此当 i>j 时，dp[i][j]=0。
#
def coin_game(coins: List[int]) -> int:
    n = len(coins)
    curSums = [0] * n
    for i in range(len(curSums)):
        curSums[i] = curSums[i-1] + coins[i] if i > 0 else coins[0]
    dp = [[0] * n for _ in range(n)]
    for size in range(n):
        for l in range(n-size):
            r = l + size
            if l == r:
                dp[l][r] = curSums[r] - (curSums[l-1] if l > 0 else 0)
            else:
                dp[l][r] = curSums[r] - (curSums[l-1] if l > 0 else 0) - min(dp[l+1][r], dp[l][r-1])
    return dp[0][n-1]



if __name__ == '__main__':
    coins = [4, 4, 9, 4]
    res = coin_game(coins)
    print(res)
    coins = [1, 2, 9999, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    res = coin_game(coins)
    print(res)
