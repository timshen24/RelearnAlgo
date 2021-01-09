from random import randint
import time

class UnionFind1(object):
    def __init__(self, n):
        self.__count = n
        self.__id = [i for i in range(n)]

    def find(self, p):
        assert 0 <= p < self.__count
        return self.__id[p]

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId != qId:
            for i in range(self.__count):
                if self.__id[i] == pId:
                    self.__id[i] = qId

if __name__ == '__main__':
    n = 1000
    uf = UnionFind1(n)
    T1 = time.time()
    for i in range(n):
        a = randint(0, n - 1)
        b = randint(0, n - 1)
        uf.union(a, b)
    for i in range(n):
        a = randint(0, n - 1)
        b = randint(0, n - 1)
        uf.isConnected(a, b)
    T2 = time.time()
    print(f'Time elapsed: {((T2 - T1) * 1000)}ms')