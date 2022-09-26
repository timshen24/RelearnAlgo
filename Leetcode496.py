from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)
        return [res[num] for num in nums1]


class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)

        dct = dict()
        stack = []
        for i in range(n):
            while stack and stack[-1] < nums2[i]:
                dct[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        return [dct.get(num, -1) for num in nums1]


class MySolution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = {}
        for num in nums2:
            while stack and stack[-1] < num:
                smaller = stack.pop()
                res[smaller] = num
            stack.append(num)
        return [res.get(num, -1) for num in nums1]


solution = MySolution()
print(solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
