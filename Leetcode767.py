from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_heap = [(-cnt, c) for c, cnt in counter.items()]
        heapq.heapify(max_heap)
        max_cnt, _ = max_heap[0]
        if -max_cnt > (len(s) + 1) // 2:
            return ""
        ptr = 0
        res = [None for _ in range(len(s))]
        while max_heap:
            max_cnt, char = heapq.heappop(max_heap)
            for _ in range(-max_cnt):
                res[ptr] = char
                ptr += 2
                if ptr >= len(s):
                    ptr = 1
        return "".join(res)

solution = Solution()
print(solution.reorganizeString("aaab"))
