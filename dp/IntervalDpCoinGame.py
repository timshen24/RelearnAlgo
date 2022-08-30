from typing import List


def max_score(curSum, l, r) -> int:
    if l == r:
        return coins[r]
    total = curSum[r+1]-curSum[l]
    left = max_score(curSum, l+1, r)
    right = max_score(curSum, l, r-1)
    return total-min(left,right)


def coin_game(coins: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    prefixSum = [0] * (len(coins) + 1)
    for i in range(1, len(prefixSum)):
        prefixSum[i] = prefixSum[i - 1] + coins[i - 1]
    print(prefixSum)
    return max_score(prefixSum, 0, len(coins)-1)

if __name__ == '__main__':
    coins = [4, 4, 9, 4]
    coins = [1, 2, 9999, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    res = coin_game(coins)
    print(res)
