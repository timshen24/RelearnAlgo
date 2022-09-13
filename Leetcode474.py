from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(length+1)]
        for i in range(1, length + 1):
            mCount, nCount = strs[i-1].count('0'), strs[i-1].count('1')
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= mCount and k >= nCount:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - mCount][k - nCount] + 1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
        print(dp)
        return dp[length][m][n]


solution = Solution()
print(solution.findMaxForm(["10", "0", "1"], 1, 1))