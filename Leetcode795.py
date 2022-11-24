from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = 0
        start = end = -1
        for i in range(len(nums)):
            if nums[i] > right:
                start = end = i
                continue
            if nums[i] >= left:
                end = i
            res += end - start
        return res


solution = Solution()
print(solution.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))