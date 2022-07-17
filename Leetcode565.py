from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        maxLen = -1
        visited = [False for _ in range(len(nums))]
        for i in range(len(nums)):
            num = nums[i]
            length = 0
            while not visited[num]:
                visited[num] = True
                num = nums[num]
                length += 1
                maxLen = max(maxLen, length)
        return maxLen


solution = Solution()
print(solution.arrayNesting([5, 4, 0, 3, 1, 6, 2]))
