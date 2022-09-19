from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def find_neighbor(row, col):
            res = []
            delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for deltaRow, deltaCol in delta:
                newRow, newCol = row + deltaRow, col + deltaCol
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                    if grid[newRow][newCol] == '1':
                        res.append((newRow, newCol))
            return res

        def bfs(row, col):
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                grid[r][c] = '0'
                for neighbor in find_neighbor(r, c):
                    queue.append(neighbor)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    bfs(r, c)
                    res += 1
        return res


solution = Solution()
print(solution.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
print(solution.numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
