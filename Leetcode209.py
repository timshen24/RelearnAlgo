from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start, end = 0, 0
        ans = len(nums)
        total = 0
        while start < len(nums):
            if end < len(nums) and total < s:
                total += nums[end]
                end += 1
            else:
                total -= nums[start]
                start += 1
            if total >= s:
                ans = min(ans, end - start)

        return ans

solution = Solution()
print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))