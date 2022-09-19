from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        maxRow, maxCol = len(grid), len(grid[0])

        def dfs(grid, r, c, island):
            if not inArea(r, c):
                return 0
            if grid[r][c] != 1:
                return 0
            grid[r][c] = island
            return 1 + dfs(grid, r + 1, c, island) + dfs(grid, r - 1, c, island) + dfs(grid, r, c + 1, island) + dfs(
                grid, r, c - 1, island)

        def inArea(r, c):
            return 0 <= r < maxRow and 0 <= c < maxCol

        islands = {}
        islandId = 2
        for r in range(maxRow):
            for c in range(maxCol):
                if grid[r][c] == 1:
                    islands[islandId] = dfs(grid, r, c, islandId)
                    islandId += 1

        def getIslands(grid, r, c):
            islands = set()
            if inArea(r + 1, c) and grid[r+1][c] != 0:
                islands.add(grid[r+1][c])
            if inArea(r - 1, c) and grid[r - 1][c] != 0:
                islands.add(grid[r - 1][c])
            if inArea(r, c + 1) and grid[r][c + 1] != 0:
                islands.add(grid[r][c + 1])
            if inArea(r, c - 1) and grid[r][c - 1] != 0:
                islands.add(grid[r][c - 1])
            return islands

        maxArea = 0
        for r in range(maxRow):
            for c in range(maxCol):
                if grid[r][c] == 0:
                    maxArea = max(maxArea, sum(map(lambda x: islands[x], getIslands(grid, r, c))) + 1)
        return maxArea if maxArea != 0 else islands.get(2)


solution = Solution()
print(solution.largestIsland(grid=[[1, 0], [0, 1]]))
