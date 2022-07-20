from typing import List


class Solution:
	def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
		m, n = len(grid), len(grid[0])
		for _ in range(k):
			for j in range(n):
				for i in range(m):
					
					grid[i][(j + 1) % n], grid[i][j] = grid[i][j], grid[i][(j + 1) % n]
		print(grid)
		return grid


k = 1
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution = Solution()
solution.shiftGrid(grid, 1)
