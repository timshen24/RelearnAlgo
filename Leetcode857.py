from typing import List
from heapq import heappush, heappop


# class Solution0:
#     def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
#         pairs = sorted(zip(quality, wage), key=lambda p: p[1] / p[0])
#         print(pairs)
#         ans = float("inf")
#         totalq = 0
#         h = []
#         for q, w in pairs[:k - 1]:
#             totalq += q
#             heappush(h, -q)
#         print(totalq)
#         print(h)
#         for q, w in pairs[k - 1:]:
#             totalq += q
#             heappush(h, -q)
#             ans = min(ans, w / q * totalq)
#             totalq += heappop(h)
#         return ans

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ans, total, pq = float("inf"), 0, []
        for q, w in sorted(zip(quality, wage), key=lambda x: (x[1] / x[0])):
            total += q
            heappush(pq, -q)
            if len(pq) > k:
                total += heappop(pq)
            if len(pq) == k:
                ans = min(ans, total * w / q)
        return ans


solution = Solution()
print(solution.mincostToHireWorkers([10, 20, 5], wage=[70, 50, 30], k=2))
print(solution.mincostToHireWorkers([3, 1, 10, 10, 1, 100], wage=[4, 8, 2, 2, 7, 100000], k=3))
