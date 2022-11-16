from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        minSuffix = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if nums[i - 1] > minSuffix:
                return False
            minSuffix = min(minSuffix, nums[i])
        return True


solution = Solution()
print(solution.isIdealPermutation([1, 0, 2]))  # True
print(solution.isIdealPermutation([1, 2, 0]))  # False
print(solution.isIdealPermutation([2, 0, 3, 1]))
print(solution.isIdealPermutation([2, 0, 1]))
