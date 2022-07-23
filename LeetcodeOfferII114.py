from collections import defaultdict, deque
from typing import List


class Solution:
	def get_counts(self, graph):
		counts = {node: 0 for node in graph}
		for parent in graph:
			for son in graph[parent]:
				counts[son] += 1
		return counts

	def alienOrder(self, words: List[str]) -> str:
		graph = defaultdict(set)
		for word in words:
			for c in word:
				graph[c] = set()
		for i in range(1, len(words)):
			prev, cur = words[i - 1], words[i]
			if prev.startswith(cur) and len(prev) > len(cur):
				return ""
			for j in range(min(len(prev), len(cur))):
				if prev[j] == cur[j]:
					continue
				graph[prev[j]].add(cur[j])
				break
		q = deque()
		counts = self.get_counts(graph)
		print(f"counts={counts}, graph = {graph}")
		res = []
		for node in graph:
			if counts[node] == 0:
				q.append(node)
		while q:
			node = q.popleft()
			res.append(node)
			for son in graph[node]:
				counts[son] -= 1
				if counts[son] == 0:
					q.append(son)
		return "".join(res) if len(res) == len(graph) else ""


solution = Solution()
print(solution.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
print(solution.alienOrder(["ac", "ab", "zc", "zb"]))
print(solution.alienOrder(["abc", "ab"]))
