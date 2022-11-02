from typing import List
import math


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        def distance(x, y, i, j):
            dis = math.sqrt((x-i)*(x-i)+(y-j)*(y-j))
            return dis

        minX, maxX, minY, maxY = 51, -1, 51, -1
        for x, y, q in towers:
            minX = min(minX, x)
            maxX = max(maxX, x)
            minY = min(minY, y)
            maxY = max(maxY, y)
        print(minX, maxX, minY, maxY)
        res, total = 0, 0
        xy = [0, 0]
        for i in range(minX, maxX + 1):
            for j in range(minY, maxY + 1):
                total = 0
                for x, y, q in towers:
                    dis = distance(x, y, i, j)
                    total += math.floor(q / (1 + dis)) if dis <= radius else 0
                print(f"i={i}, j={j}, total={total}")
                if total > res:
                    res = total
                    xy = [i, j]
        return xy, res

solution = Solution()
print(solution.bestCoordinate([[1, 2, 5], [2, 1, 7], [3, 1, 9]], 2))