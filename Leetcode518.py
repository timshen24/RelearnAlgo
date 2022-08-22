from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(1, len(dp)):
                if i - coin >= 0:
                    dp[i] += dp[i-coin]
        print(dp)
        return dp[-1]


solution = Solution()
print(solution.change(5, [1, 2, 5]))