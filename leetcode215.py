from typing import List
from random import randint

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = randint(0, len(nums) - 1)
        pivot = nums[index]
        left = [i for i in nums if i > pivot]
        right = [i for i in nums if i <= pivot]
        if k <= len(left):
            return self.findKthLargest(left, k)
        elif k == len(left) + 1:
            return pivot
        else:
            return self.findKthLargest(right, k - len(left) - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
