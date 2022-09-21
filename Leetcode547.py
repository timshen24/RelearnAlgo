from typing import List


class UnionFind:
    def __init__(self):
        self.id = {}

    def find(self, x):
        y = self.id.get(x, x)
        if y != x:
            self.id[x] = y = self.find(y)
        return y

    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind()
        uf.id = {i: i for i in range(len(isConnected[0]))}
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c]:
                    uf.union(r, c)
        print(uf.id)
        return len(set(uf.find(i) for i, _ in uf.id.items()))


# solution = Solution()
# print(solution.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))

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
