from heapq import *
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = list(range(n))
        used = []  # save (endTime, roomId) to heap
        res = [0] * n
        for s, e in sorted(meetings):
            while used and used[0][0] <= s:  # 如果最早的会议室已经结束
                endTime, roomId = heappop(used)  # 最早的会议室弹出
                heappush(available, roomId)  # 最早的会议室弹出，进入可选的room堆
            if available:  # 如果有会议室空闲
                roomId = heappop(available)  # 弹出那个空闲的会议室
                heappush(used, (e, roomId))  # 和会议的结束时间一起，压入在使用的会议室中
            else:
                end, roomId = heappop(used)  # 如果没有会议室可用，看看最早结束的会议是哪场
                heappush(used, (end + e - s, roomId))  # 把它无缝衔接到最早结束的会议室里
            res[roomId] += 1  # 该会议室使用次数+1
        return res.index(max(res))  # 返回使用最多的会议室


solution = Solution()
print(solution.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))
print(solution.mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]))
