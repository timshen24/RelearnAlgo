from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxRow, maxCol = len(grid), len(grid[0])

        def find_neighbor(row, col):
            delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for deltaRow, deltaCol in delta:
                newRow, newCol = row + deltaRow, col + deltaCol
                if 0 <= newRow < maxRow and 0 <= newCol < maxCol:
                    if grid[newRow][newCol] == 1:
                        yield [newRow, newCol]

        def bfs(row, col):
            queue = deque([(row, col)])
            area = 0
            while queue:
                r, c = queue.popleft()
                grid[r][c] = 2
                area += 1
                for neighborRow, neighborCol in find_neighbor(r, c):
                    grid[neighborRow][neighborCol] = 2
                    queue.append((neighborRow, neighborCol))
            return area

        maxArea = 0
        for r in range(maxRow):
            for c in range(maxCol):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)
        return maxArea

solution = Solution()
print(solution.maxAreaOfIsland([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))