class Solution:
    def reachNumber(self, target: int) -> int:
        step, curLen = 0, 0
        while curLen < target:
            step += 1
            curLen += step
        if curLen == target:
            return step
        distance = target - (curLen - step)
        step -= 1
        return step + distance * 2


solution = Solution()
print(solution.reachNumber(2))