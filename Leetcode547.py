from typing import List

class UnionFind:
    def __init__(self, n):
        self.id = {i: i for i in range(n)}

    def find(self, x):
        y = self.id.get(x, x)
        if y != x:
            self.id[x] = y = self.find(y)
        return y

    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for r in range(n):
            for c in range(n):
                if isConnected[r][c]:
                    uf.union(r, c)
        return len(set(uf.find(i) for i in uf.id.keys()))


solution = Solution()
print(solution.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))

class SolutionDFS:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(cities):
                if isConnected[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)

        cities = len(isConnected)
        visited = set()
        provinces = 0
        for i in range(cities):
            if i not in visited:
                dfs(i)
                provinces += 1
        return provinces


solution = SolutionDFS()
print(solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))

from collections import deque
class SolutionBFS:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        visited = set()
        provinces = 0

        for i in range(cities):
            if i not in visited:
                queue = deque([i])
                while queue:
                    j = queue.popleft()
                    for k in range(cities):
                        if isConnected[j][k] and k not in visited:
                            queue.append(k)
                            visited.add(k)
                provinces += 1
        return provinces


solution = SolutionBFS()
print(solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
