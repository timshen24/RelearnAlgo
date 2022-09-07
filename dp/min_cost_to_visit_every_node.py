from typing import List


def min_cost_to_visit_every_node(graph: List[List[int]]) -> int:
    dp = [[float("inf")] * (1 << len(graph)) for _ in range(len(graph))]

    def dfs(curNode: int, bitmask: int):
        if bitmask == (1 << len(graph)) - 1:
            return 0
        if dp[curNode][bitmask] != float("inf"):
            return dp[curNode][bitmask]
        for i in range(len(graph[curNode])):
            if graph[curNode][i] != 0 and (1 << i) & bitmask == 0:
                dp[curNode][bitmask] = min(dp[curNode][bitmask], graph[curNode][i] + dfs(i, (1 << i) | bitmask))
        return dp[curNode][bitmask]
    ans = dfs(0, 1)
    return -1 if ans == float("inf") else ans


if __name__ == '__main__':
    graph = [[0, 0, 1], [0, 0, 0], [0, 2, 0]]
    res = min_cost_to_visit_every_node(graph)
    print(res)
