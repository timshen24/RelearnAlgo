from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        # print(rows, cols)
        # print([(row + col) for row in rows for col in cols])
        return sum((row + col) % 2 for row in rows for col in cols)

solution = Solution()
print(solution.oddCells(2, 3, [[0, 1], [1, 1]]))
print(solution.oddCells(2, 2, [[1, 1], [0, 0]]))
