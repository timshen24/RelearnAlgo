from collections import deque


def count_graph(graph):
	counts = {node: 0 for node in graph}
	for parent in graph:
		for child in graph[parent]:
			counts[child] += 1
	return counts


def topo_sort(graph):
	queue = deque()
	res = []
	counts = count_graph(graph)
	for parent, count in counts.items():
		if count == 0:
			queue.append(parent)
	while queue:
		node = queue.popleft()
		res.append(node)
		for child in graph[node]:
			counts[child] -= 1
			if counts[child] == 0:
				queue.append(child)
	return res if len(res) == len(graph) else None


graph = {4: [2], 5: [2], 6: [3], 2: [1], 3: [1], 1: []}
print(count_graph(graph))
print(topo_sort({4: [2], 5: [2], 6: [3], 2: [1], 3: [1], 1: []}))
