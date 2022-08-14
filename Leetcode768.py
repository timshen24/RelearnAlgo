class Solution:
    def maxChunksToSorted(self, arr: [int]) -> int:
        stack = []
        for a in arr:
            if len(stack) == 0 or a >= stack[-1]:
                stack.append(a)
            else:
                mx = stack.pop()
                while stack and stack[-1] > a:
                    stack.pop()
                stack.append(mx)
        return len(stack)


solution = Solution()
print(solution.maxChunksToSorted([5, 4, 3, 2, 1]))
print(solution.maxChunksToSorted([3, 2, 1, 5, 4]))
print(solution.maxChunksToSorted([3, 2, 1, 2, 5]))
print(solution.maxChunksToSorted([2, 1, 3, 4, 4]))
