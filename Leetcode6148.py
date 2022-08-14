from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * (n - 2) for _ in range(m - 2)]
        for i in range(m - 2):
            for j in range(n - 2):
                localMax = 0
                for l in range(3):
                    for k in range(3):
                        localMax = max(localMax, grid[i + l][j + k])
                        print(f"l = {l}, k = {k}, localMax = {localMax}")
                res[i][j] = localMax
                print(f"i={i}, j={j}, res[i][j] = {res[i][j]}")
        return res


solution = Solution()
print(solution.largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
print(solution.largestLocal([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
