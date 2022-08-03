from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, len(res)):
            res[i] = res[i >> 1] + int(i & 1)
        return res


solution = Solution()
print(solution.countBits(5))
