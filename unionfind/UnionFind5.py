class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {} # rank[i]表示根节点为i的树的高度

    def find(self, x):
        y = self.parent.get(x, x)
        if y != x:
            self.parent[x] = y = self.find(y)
        return y

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