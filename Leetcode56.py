from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(intervals[i][1], res[-1][1])
        return res

solution = Solution()
print(solution.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))