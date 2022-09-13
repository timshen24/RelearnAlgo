from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)):
            if i >= nums[i]:
                res = len(nums)-i-1
        return i if res == i else -1


solution = Solution()
print(solution.specialArray([3, 5]))