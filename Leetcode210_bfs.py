from typing import List
from collections import deque


class Solution:
	def getCounts(self, graph):
		counts = {node: 0 for node in graph}
		for parent in graph:
			for son in graph[parent]:
				counts[son] += 1
		return counts

	def topoSort(self, graph):
		res = []
		counts = self.getCounts(graph)
		q = deque()
		for node in counts:
			if counts[node] == 0:
				q.append(node)
		while q:
			node = q.popleft()
			res.append(node)
			for son in graph[node]:
				counts[son] -= 1
				if counts[son] == 0:
					q.append(son)
		return res if len(res) == len(graph) else []

	def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
		graph = {courseNum: [] for courseNum in range(numCourses)}
		for prereq in prerequisites:
			parent, son = prereq[1], prereq[0]
			graph[parent].append(son)
		return self.topoSort(graph)


solution = Solution()
print(solution.findOrder(2, [[1, 0]]))
print(solution.findOrder(2, [[1, 0], [0, 1]]))