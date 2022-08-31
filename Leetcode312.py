from typing import List

class Solution0:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def dp(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            memo[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dp(l, i-1) + dp(i+1, r)
                memo[(l, r)] = max(memo[(l, r)], coins)
            return memo[(l, r)]
        return dp(1, len(nums)-2)

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        dp = [[0 for r  in range(len(nums))] for l in range(len(nums))]
        for l in range(len(nums)-2,0,-1):
            for r in range(1,len(nums)-1):
                for i in range(l,r+1):
                    if l<=r:
                        dp[l][r] = max(dp[l][r], nums[l-1]*nums[i]*nums[r+1]+dp[l][i-1]+dp[i+1][r])
        return dp[1][-2]