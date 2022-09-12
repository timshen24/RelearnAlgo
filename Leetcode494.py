# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total, cur = 0, 0
        def backtrack(index: int):
            nonlocal cur
            nonlocal total
            if index == len(nums):
                if cur == target:
                    total += 1
                return
            cur += nums[index]
            backtrack(index + 1)
            cur -= nums[index]
            cur -= nums[index]
            backtrack(index + 1)
            cur += nums[index]
        backtrack(0)
        return total

solution = Solution()
print(solution.findTargetSumWays([1, 1, 1, 1, 1], target=3))
print(solution.findTargetSumWays([1], target=1))
print(solution.findTargetSumWays([1, 0], 1))
print(solution.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1))
print(solution.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1))
print(solution.findTargetSumWays([1, 2, 1], 0))
