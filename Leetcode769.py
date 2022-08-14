class Solution(object):
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i:
                ans += 1
        return ans


solution = Solution()
print(solution.maxChunksToSorted([4, 3, 2, 1, 0]))
print(solution.maxChunksToSorted([4, 1, 2, 3, 0]))
print(solution.maxChunksToSorted([1, 0, 2, 3, 4]))
