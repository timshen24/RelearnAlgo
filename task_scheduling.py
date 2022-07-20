from typing import List
from collections import deque


def task_scheduling(tasks: List[str], requirements: List[List[str]]) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    graph = {task: [] for task in tasks}
    for a, b in requirements:
        graph[a].append(b)  # Notice! Notice! Notice!

    def count_parents():
        counts = {node: 0 for node in graph}
        for parent in graph:
            for node in graph[parent]:
                counts[node] += 1
        return counts

    def topo_sort():
        res = []
        queue = deque()
        counts = count_parents()
        for node in counts:
            if counts[node] == 0:
                queue.append(node)
        while queue:
            node = queue.popleft()
            res.append(node)
            for child in graph[node]:
                counts[child] -= 1
                if counts[child] == 0:
                    queue.append(child)
        return res
    return topo_sort()


if __name__ == '__main__':
    tasks = ["a", "b", "c", "d"]
    requirements = [["a", "b"], ["c", "b"], ["b", "d"]]
    res = task_scheduling(tasks, requirements)
    print(res)
    tasks = ["brad", "cad", "dag", "ethereum", "forget", "aggregate"]
    requirements = [["forget", "ethereum"], ["ethereum", "dag"], ["dag", "cad"], ["cad", "brad"], ["brad", "aggregate"]]
    res = task_scheduling(tasks, requirements)
    print(res)

