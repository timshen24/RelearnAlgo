import time
from random import randint


class UnionFind5:
    def __init__(self):
        self.parent = {}
        self.rank = {} # rank[i]表示根节点为i的树的高度

    def find(self, x):
        y = self.parent.get(x, x)
        if y != x:
            self.parent[x] = y = self.find(y)
        return y

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        if self.find(x) not in self.rank:
            self.rank[self.find(x)] = 0
        if self.find(y) not in self.rank:
            self.rank[self.find(y)] = 0
        if self.rank[self.find(x)] < self.rank[self.find(y)]:
            self.parent[self.find(x)] = self.find(y)
        else:
            self.parent[self.find(y)] = self.find(x)
            if self.rank[self.find(x)] == self.rank[self.find(y)]:
                self.rank[self.find(x)] = self.rank[self.find(x)] + 1


if __name__ == '__main__':
    n = 1000000
    uf = UnionFind5(n)
    T1 = time.time()
    for i in range(n):
        a = randint(0, n - 1)
        b = randint(0, n - 1)
        uf.union(a, b)
        # if i % 100 == 0:
        #     print(f'finish a union batch(i={i})')
    print('finished union')
    for i in range(n):
        a = randint(0, n - 1)
        b = randint(0, n - 1)
        uf.isConnected(a, b)
        # if i % 100 == 0:
        #     print(f'finish a connection batch(i={i})')
    T2 = time.time()
    print(f'Time elapsed: {((T2 - T1) * 1000)}ms')