from typing import List
from typing import Dict
from collections import deque


def count_parents(graph) -> dict:
    counts = {node: 0 for node in graph}
    for parent in graph:
        for son in graph[parent]:
            counts[son] += 1
    return counts


def task_scheduling_2(tasks: List[str], times: List[int], requirements: List[List[str]]) -> int:
    # init graph and task_times
    graph = {node: [] for node in tasks}
    task_times: Dict[str, int] = dict(zip(tasks, times))
    for a, b in requirements:
        graph[a].append(b)
    counts = count_parents(graph)
    ans = 0
    q = deque()
    dis: Dict[str, int] = dict()
    for node in graph:
        dis[node] = 0
    for node in counts:
        if counts[node] == 0:
            q.append(node)
            dis[node] = task_times[node]
            ans = max(ans, dis[node])
    while q:
        node = q.popleft()
        for child in graph[node]:
            counts[child] -= 1
            dis[child] = max(dis[child], dis[node] + task_times[child])
            ans = max(ans, dis[child])
            if counts[child] == 0:
                q.append(child)
    return ans


tasks = ["a", "b", "c", "d"]
times = [1, 1, 2, 1]
requirements = [["a", "b"], ["c", "b"], ["b", "d"]]
print(task_scheduling_2(tasks, times, requirements))