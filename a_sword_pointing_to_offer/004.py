from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum([(num >> i) & 1 for num in nums])
            if total % 3:
                ans |= (1 << i)
        return ans


solution = Solution()
print(solution.singleNumber([2, 2, 3, 2]))
print(solution.singleNumber([0, 1, 0, 1, 0, 1, 100]))