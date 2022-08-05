from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l, r = 0, 0
        total = 1
        while r < len(nums):
            total *= nums[r]
            while total >= k:
                total /= nums[l]
                l += 1
            print(f"nums[l] = {nums[l]}, nums[r] = {nums[r]}, r-l+1={r - l + 1}")
            res += r - l + 1
            r += 1
        return res


solution = Solution()
print(solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
