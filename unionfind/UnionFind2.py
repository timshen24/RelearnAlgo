from random import randint
import time

class UnionFind2(object):
    def __init__(self, n):
        self.__count = n
        self.__parent = [i for i in range(n)]

    def find(self, p):
        assert 0 <= p < self.__count
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot != qRoot:
            self.__parent[pRoot] = qRoot

if __name__ == '__main__':
    n = 100000
    uf = UnionFind2(n)
    T1 = time.time()
    for i in range(n):
        a = randint(0, n - 1)
        b = randint(0, n - 1)
        uf.union(a, b)
        if i % 100 == 0:
            print(f'finish a union batch(i={i})')
    print('finished union')
    for i in range(n):
        a = randint(0, n - 1)
        b = randint(0, n - 1)
        uf.isConnected(a, b)
        if i % 100 == 0:
            print(f'finish a connection batch(i={i})')
    T2 = time.time()
    print(f'Time elapsed: {((T2 - T1) * 1000)}ms')