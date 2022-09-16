from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 1
        for i in range(n):
            d = {}
            for j in range(i + 1, n):
                xi, yi, xj, yj = poinπts[i][0], points[i][1], points[j][0], points[j][1]
                deltaX, deltaY = xj - xi, yj - yi
                g = self.gcd(deltaX, deltaY)
                k = str(deltaX // g) + "/" + str(deltaY // g)
                d[k] = d.get(k, 1) + 1
                res = max(res, d[k])
        return res

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)


solution = Solution()
print(solution.maxPoints([[1, 1], [2, 2], [3, 3]]))
print(solution.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
