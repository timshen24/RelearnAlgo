from typing import List
import bisect


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = bisect.bisect_left(arr, x)
        left = right - 1
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr) - 1 or (x - arr[left-1]) <= arr[right+1] - x:
                left -= 1
            else:
                right += 1
        return arr[left+1: right]



solution = Solution()
print(solution.findClosestElements([1, 2, 3, 4, 5], 4, 3))
print(solution.findClosestElements([1, 2, 3, 4, 5], 4, -1))
print(solution.findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], k=3, x=5))
