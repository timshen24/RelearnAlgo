from heapq import heappop, heappush
from typing import List, Dict


def count_parents(graph):
	counts = {node: 0 for node in graph}
	for parent in graph:
		for node in graph[parent]:
			counts[node] += 1
	return counts


def topo_sort(graph):
	res = []
	pq = []
	counts = count_parents(graph)
	for node in counts:
		if counts[node] == 0:
			heappush(pq, node)
	while len(pq) > 0:
		node = heappop(pq)
		res.append(node)
		for child in graph[node]:
			counts[child] -= 1
			if counts[child] == 0:
				heappush(pq, child)

	for count in counts.values():
		if count != 0:
			return None
	return res


def alien_order(words: List[str]) -> str:
	# init graph
	graph: Dict[str, List[str]] = dict()
	for word in words:
		for c in word:
			if not c in graph:
				graph[c] = list()

	prev = words[0]
	for i in range(1, len(words)):
		cur = words[i]
		j = 0
		while j < len(prev) and j < len(cur):
			# ignore duplicates
			if (prev[j] != cur[j]):
				if not cur[j] in graph[prev[j]]:
					graph[prev[j]].append(cur[j])
				break
			j += 1
		prev = cur

	s = topo_sort(graph)
	if s is None:
		return ""
	return "".join(s)


if __name__ == '__main__':
	words = ["wrt", "wrf", "er", "ett", "rftt"]
	res = alien_order(words)
	print(res)
