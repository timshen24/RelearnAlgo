from typing import List
from collections import deque


def get_graph(original: List[int], seqs: List[List[int]]) -> dict:
	n = len(original)
	graph = {node: set() for node in range(1, n + 1)}
	for seq in seqs:
		for i in range(1, len(seq)):
			graph[seq[i - 1]].add(seq[i])
	return graph


def get_parent_counts(graph: dict) -> dict:
	counts = {node: 0 for node in graph}
	for parent in graph:
		for child in graph[parent]:
			counts[child] += 1
	return counts


def sequence_reconstruction(original: List[int], seqs: List[List[int]]) -> bool:
	# WRITE YOUR BRILLIANT CODE HERE
	graph = get_graph(original, seqs)
	#     print(f"graph = {graph}")
	counts = get_parent_counts(graph)
	#     print(f"counts = {counts}")
	res = []
	queue = deque()
	for node in counts:
		if counts[node] == 0:
			queue.append(node)
	while queue:
		if len(queue) > 1:
			return False
		node = queue.popleft()
		res.append(node)
		for son in graph[node]:
			counts[son] -= 1
			if counts[son] == 0:
				queue.append(son)
	#     print(f"res = {res}")
	return res == original


if __name__ == '__main__':
	original = [int(x) for x in input().split()]
	seqs = [[int(x) for x in input().split()] for _ in range(int(input()))]
	res = sequence_reconstruction(original, seqs)
	print('true' if res else 'false')
