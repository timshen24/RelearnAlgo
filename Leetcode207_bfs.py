from typing import List
from collections import deque


class Solution:
	def getCounts(self, graph):
		counts = { node: 0 for node in graph }
		for parent in graph:
			for son in graph[parent]:
				counts[son] += 1
		return counts

	def topoSort(self, graph) -> bool:
		visited = 0
		q = deque()
		counts = self.getCounts(graph)
		for node in counts:
			if counts[node] == 0:
				q.append(node)
		while q:
			node = q.popleft()
			visited += 1
			for son in graph[node]:
				counts[son] -= 1
				if counts[son] == 0:
					q.append(son)
		return visited == len(graph)

	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		graph = { i: [] for i in range(numCourses)}
		for prereq in prerequisites:
			parent, son = prereq[1], prereq[0]
			graph[parent].append(son)
		print(self.getCounts(graph))
		return self.topoSort(graph)


solution = Solution()
print(solution.canFinish(2, [[1, 0]]))
print(solution.canFinish(2, [[1, 0], [0, 1]]))
