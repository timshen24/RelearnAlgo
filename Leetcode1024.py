from typing import List


# [[0, 2], [1, 5], [1, 9], [4, 6], [5, 9], [8, 10]]
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        maxn = [0] * time
        last = ret = pre = 0
        for a, b in clips:
            if a < time:
                maxn[a] = max(maxn[a], b)
        print(maxn)

        for i in range(time):
            last = max(last, maxn[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last

        return ret



solution = Solution()
print(solution.videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10))
assert solution.videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10) == 3