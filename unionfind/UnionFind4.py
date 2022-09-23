from random import randint
import time

class UnionFind4(object):
    def __init__(self, n):
        self.__count = n
        self.__parent = [i for i in range(n)]
        self.__rank = [1 for i in range(n)] # numbers of level in the set with i as root

    def find(self, p):
        assert 0 <= p < self.__count
        if p != self.__parent[p]:
            self.__parent[p] = self.find(self.__parent[p])
        return self.__parent[p]

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot != qRoot:
            if self.__rank[pRoot] < self.__rank[qRoot]:
                self.__parent[pRoot] = qRoot
            elif self.__rank[qRoot] < self.__rank[pRoot]:
                self.__parent[qRoot] = pRoot
            else:
                self.__parent[pRoot] = qRoot
                self.__rank[qRoot] += 1

if __name__ == '__main__':
    n = 1000000
    uf = UnionFind4(n)
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