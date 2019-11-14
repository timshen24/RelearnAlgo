from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[0]
        left = [i for i in nums[1:] if i > pivot]
        right = [i for i in nums[1:] if i <= pivot]
        if len(nums) == 1:
            return nums[0]
        elif len(left) >= k:
            return self.findKthLargest(left, k)
        else:
            if len(left) + 1 == k:
                return pivot
            return self.findKthLargest(right, k - len(left) - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthLargest([2, 1], 2))
