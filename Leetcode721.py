from typing import List


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

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
                self.rank[self.find(x)] += 1


from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find = UnionFind()
        parents = {}
        emailToName = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                emailToName[email] = name
                parents[email] = email

        for account in accounts:
            email1 = account[1]
            for email2 in account[2:]:
                union_find.union(email1, email2)

        groups = defaultdict(list)
        for email in parents:
            r = union_find.find(email)
            groups[r].append(email)
        ans = []
        for parent in groups:
            ans.append([emailToName[parent]] + sorted(groups[parent]))
        return ans


solution = Solution()
print(solution.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                              ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))
print(solution.accountsMerge(
    [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
     ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
     ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]))
