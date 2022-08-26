from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        maxSize, maxVal = -1, -1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i]= max(dp[i], dp[j] + 1)
            if dp[i] > maxSize:
                maxSize = dp[i]
                maxVal = nums[i]
        # dp=[1, 2, 3, 3, 4, 4, 5, 5, 6],maxsize=6, maxVal=720
        print(f"maxsize={maxSize}, maxVal={maxVal}")
        res = []
        for i in range(len(dp)-1, -1, -1):
            if dp[i] == maxSize and maxVal % nums[i] == 0:
                res.append(nums[i])
                maxSize -= 1
                maxVal = nums[i]
        return res

solution = Solution()
print(solution.largestDivisibleSubset([9, 18, 54, 90, 108, 180, 360, 540, 720]))