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

solution = Solution()
print(solution.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))