from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        ptr = r
        res = [0] * len(nums)
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res[ptr] = nums[r] ** 2
            else:
                res[ptr] = nums[l] ** 2
            ptr -= 1
        return res


solution = Solution()
print(solution.sortedSquares([-4, -1, 0, 3, 10]))


