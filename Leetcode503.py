from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mono_stack, res = [], {}
        for i in range(len(nums)):
            while mono_stack and nums[mono_stack[-1]] < nums[i]:
                id = mono_stack.pop()
                res[id] = nums[i]
            mono_stack.append(i)
        # print(mono_stack)
        for i in range(len(mono_stack) - 1, 0, -1):
            if nums[mono_stack[i]] > nums[mono_stack[i-1]]:
                res[mono_stack[i]] = nums[mono_stack[0]]
        return [res.get(i, -1) for i in range(len(nums))]


solution = Solution()
print(solution.nextGreaterElements([1, 2, 1]))  # [2,-1,2]
print(solution.nextGreaterElements([1, 2, 3, 4, 3]))  # [2,3,4,-1,4]
print(solution.nextGreaterElements([5, 4, 3, 2, 1]))  # [-1,5,5,5,5]
print(solution.nextGreaterElements([1, 5, 3, 6, 8]))  # [5,6,6,8,-1]
print(solution.nextGreaterElements([1, 1, 1, 1, 1]))  # [-1,-1,-1,-1,-1]
