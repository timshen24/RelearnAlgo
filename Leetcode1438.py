from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        left = 0
        min_deque, max_deque = deque(), deque()
        for right in range(len(nums)):
            while min_deque and nums[right] < nums[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(right)
            while max_deque and nums[right] > nums[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                left += 1
            res = max(res, right - left + 1)
        return res

solution = Solution()
print(solution.longestSubarray([8, 2, 4, 7], 4))
