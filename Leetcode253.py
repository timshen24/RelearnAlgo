from heapq import heappush, heappop
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])
        i = j = count = res = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                count += 1
                i += 1
            else:
                j += 1
                count -= 1
            res = max(res, count)
        return res


solution = Solution()
print(solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))