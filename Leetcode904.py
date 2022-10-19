from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        d = {}
        res = -1
        while r < len(fruits):
            d[fruits[r]] = d.get(fruits[r], 0) + 1
            while len(d) > 2:
                d[fruits[l]] -= 1
                if not d[fruits[l]]:
                    del d[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res


solution = Solution()
print(solution.totalFruit([1, 2, 1]))  # 3
print(solution.totalFruit([0, 1, 2, 2]))  # 3
print(solution.totalFruit([1, 2, 3, 2, 2]))  # 4
print(solution.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))  # 5
print(solution.totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]))  # 5
