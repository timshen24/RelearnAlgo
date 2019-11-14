import sys
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [0 for i in range(amount + 1)]
        memo[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                memo[i] += memo[i - coin]
        return memo[amount]

solution = Solution()
print(solution.change(5,[1,2,5]))