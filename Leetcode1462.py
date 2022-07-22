from typing import List
from collections import deque, defaultdict


class Solution:
	def getCounts(self, graph):
		counts = {node: 0 for node in graph}
		for parent in graph:
			for son in graph[parent]:
				counts[son] += 1
		return counts

	def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
		bool]:
		graph = {node: [] for node in range(numCourses)}
		for prereq in prerequisites:
			parent, son = prereq[0], prereq[1]
			graph[parent].append(son)
		counts = self.getCounts(graph)
		q = deque()
		ancestor = defaultdict(set)
		for node in counts:
			if counts[node] == 0:
				q.append(node)
		while q:
			node = q.popleft()
			for son in graph[node]:
				ancestor[son].add(node)
				ancestor[son].update(ancestor[node])
				counts[son] -= 1
				if counts[son] == 0:
					q.append(son)

		print(ancestor)
		return [query[0] in ancestor[query[1]] for query in queries]


solution = Solution()
print(list(solution.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]])))
print(list(solution.checkIfPrerequisite(2, [], [[1, 0], [0, 1]])))
print(list(solution.checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]])))
print(list(solution.checkIfPrerequisite(5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[0, 4], [4, 0], [1, 3], [3, 0]]))) # [true,false,true,false]
print(list(solution.checkIfPrerequisite(4, [[2, 3], [2, 1], [0, 3], [0, 1]], [[0, 1], [0, 3], [2, 3], [3, 0], [2, 0], [0, 2]])))
