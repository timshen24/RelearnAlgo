from typing import List


class Solution:
    def videoStitching(self, clips: List[List], time: int) -> int:
        clips.sort(key=lambda clip: (clip[0], clip[1]))
        # [[0, 2], [1, 5], [1, 9], [4, 6], [5, 9], [8, 10]]
        dp = [float("inf")] * 101
        dp[0] = 0
        for start, end in clips:
            for i in range(start, end + 1):
                dp[i] = min(dp[i], dp[start] + 1)
        return dp[time] if dp[time] != float("inf") else -1



solution = Solution()
print(solution.videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10))
assert solution.videoStitching([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10) == 3