from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(dp)):
            for word in wordDict:
                if s[i:].startswith(word):
                    if i == 0:
                        dp[i] = True
                    elif i >= len(word):
                        dp[i] = dp[i-len(word)]
                if i == len(s)-1:
                    dp[i] = dp[i-len(word)+1]
        return dp[-1]


solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"]))
print(solution.wordBreak("applepenapple", ["apple","pen"]))
print(solution.wordBreak("cars", ["car", "ca", "rs"]))
