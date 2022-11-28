from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        s = sum(nums)
        for i, v in enumerate(nums):
            nums[i] = v * n - s
        m = n >> 1
        vis = set()
        for i in range(1, 1 << m):
            t = 0
            for j, v in enumerate(nums[:m]):
                print(f"i={i}, j={j}, nums={nums}, v={v}, answer={i >> j & 1}")
                if i >> j & 1:
                    t += v
            # t = sum(v for j, v in enumerate(nums[:m]) if i >> j & 1)
            if t == 0:
                return True
            vis.add(t)
        for i in range(1, 1 << (n - m)):
            t = sum(v for j, v in enumerate(nums[m:]) if i >> j & 1)
            # if t == 0 or (i != (1 << (n - m)) - 1 and -t in vis):
            if t == 0 or -t in vis:
                return True
        return False


solution = Solution()
# print(solution.splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8]))
print(solution.splitArraySameAverage([3, 1]))
