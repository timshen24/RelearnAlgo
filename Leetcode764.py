from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[n for _ in range(n)] for _ in range(n)]
        banned = set(map(tuple, mines))
        for i in range(n):
            count = 0
            for j in range(n):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
            count = 0
            for j in range(n-1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
        for j in range(n):
            count = 0
            for i in range(n):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
            count = 0
            for i in range(n-1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
        return max(map(max, dp))


solution = Solution()
print(solution.orderOfLargestPlusSign(5, [[4, 2]]))
print(solution.orderOfLargestPlusSign(1, [[0, 0]]))