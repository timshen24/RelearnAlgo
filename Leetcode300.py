from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


solution = Solution()
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        greedy = []
        for num in nums:
            if not greedy or greedy[-1] < num:
                greedy.append(num)
            else:
                loc = bisect.bisect_left(greedy, num)
                greedy[loc] = num
        return len(greedy)