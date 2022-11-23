from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        leftMost = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    leftMost = mid
                right = mid - 1
            else:
                left = mid + 1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[right] == target:
            return [leftMost, right]
        return [leftMost, -1]


solution = Solution()
print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))
print(solution.searchRange([1], 1))
print(solution.searchRange([], 0))