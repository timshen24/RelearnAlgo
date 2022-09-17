from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        record = {0: 1}
        prefixSum, ans = 0, 0
        for num in nums:
            prefixSum += num
            modulus = prefixSum % k
            same = record.get(modulus, 0)
            record[modulus] = same + 1
            ans += same
        return ans


solution = Solution()
print(solution.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))