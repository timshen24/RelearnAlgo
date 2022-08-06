from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, curSum = 0, 0
        prefixSum = {0: 1}
        for num in nums:
            curSum += num
            res += prefixSum.get(curSum - k, 0)
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return res


solution = Solution()
print(solution.subarraySum([1, 1, 1], 2))
print(solution.subarraySum([1], 0))
