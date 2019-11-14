import sys
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1 for i in range(amount + 1)]
        memo[0] = 0
        for i in range(1, amount + 1):
            res = sys.maxsize
            for coin in coins:
                if i - coin < 0 or memo[i - coin] == -1:
                    continue
                res = min(res, 1 + memo[i - coin])
            if res == sys.maxsize:
                memo[i] = -1
            else:
                memo[i] = res
        return memo[amount]

solution = Solution()
print(solution.coinChange([2], 3))
print(solution.coinChange([1,2,5], 11))
print(solution.coinChange([186,419,83,408], 6249))
