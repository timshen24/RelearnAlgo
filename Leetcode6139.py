from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        tree = {node: [] for node in range(n)}
        restricted = {*restricted, 0}
        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)
        ans = 0

        def dfs(node):
            nonlocal ans
            ans += 1
            restricted.add(node)
            for child in tree[node]:
                if child not in restricted:
                    dfs(child)

        dfs(0)
        return ans


solution = Solution()
print(solution.reachableNodes(7, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]))
