from typing import List
import bisect


class Solution0:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = bisect.bisect_left(arr, x)
        left = right - 1
        for _ in range(k):
            if left < 0:
                right += 1
            elif right >= len(arr) - 1 or (x - arr[left - 1]) <= arr[right + 1] - x:
                left -= 1
            else:
                right += 1
        return arr[left + 1: right]


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            mid = (l + r) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                # One thing need to be notice is, right = mid will not exclude the current answer, but just set the lower bound, this ensures us we can achieve the best answer while exploring.
                r = mid
            else:
                l = mid + 1
        return arr[l:l + k]


solution = Solution()
print(solution.findClosestElements([1, 2, 3, 4, 5], 4, 3))
print(solution.findClosestElements([1, 2, 3, 4, 5], 4, -1))
print(solution.findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], k=3, x=5))
print(solution.findClosestElements([0, 2, 2, 3, 4, 6, 7, 8, 9, 9], k=4, x=5))
