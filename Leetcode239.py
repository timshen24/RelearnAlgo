from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monotonic_stack = sorted(nums[:k])[::-1]
        res = [max(monotonic_stack)]
        for i in range(1, len(nums) - 2):
            monotonic_stack.remove(nums[i - 1])
            while monotonic_stack and monotonic_stack[-1] < nums[i+k-1]:
                monotonic_stack.pop()
            monotonic_stack.append(nums[i+k-1])
            res.append(monotonic_stack[0])
        return res


solution = Solution()
solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
