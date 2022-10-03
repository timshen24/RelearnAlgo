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


class Solution1:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key = lambda x: (x[0], x[1]))
        dp = [float('inf')]*101
        dp[0] = 0
        for s, e in clips:
            for i in range(s, e+1):
                dp[i] = min(dp[i], dp[s]+1)
        print(dp)
        return dp[time] if dp[time]!=float('inf') else -1


solution = Solution1()
print(solution.videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10))
assert solution.videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10) == 3