from typing import List


# class Solution:
#     def goodIndices(self, nums: List[int], k: int) -> List[int]:
#         def isNonIncreasing(nums) -> bool:
#             nums = [float('inf')] + nums
#             for i in range(1, len(nums)):
#                 if nums[i - 1] < nums[i]:
#                     return False
#             return True
#
#         def isNonDecreasing(nums) -> bool:
#             nums = [0] + nums
#             for i in range(1, len(nums)):
#                 if nums[i - 1] > nums[i]:
#                     return False
#             return True
#
#         n = len(nums)
#         res = []
#         # k <= i < n - k
#         for i in range(k, n - k):
#             # 下标 i 之前 的 k 个元素是 非递增的
#             print(nums[i - k: i])
#             # 下标 i 之后 的 k 个元素是 非递减的
#             print(nums[i + 1: i + k + 1])
#             if not res:
#                 if (isNonIncreasing(nums[i - k: i]) and isNonDecreasing(nums[i + 1: i + k + 1])):
#                     res.append(i)
#             elif k == 1:
#                 res.append(i)
#             else:
#                 if nums[i - 1] <= nums[i - 2] and nums[i + k - 1] <= nums[i + k]:
#                     res.append(i)
#         return res
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        dec = [1] * n
        for i in range(n - 2, k, -1):
            if nums[i] <= nums[i + 1]:
                dec[i] = dec[i + 1] + 1  # 递推
        inc = 1
        for i in range(1, n - 1):
            if inc >= k and dec[i + 1] >= k:
                ans.append(i)
            if nums[i - 1] >= nums[i]:
                inc += 1  # 递推
            else:
                inc = 1
        return ans

class Solution1:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        nonDec, nonInc = [1] * n, [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                nonDec[i] = nonDec[i + 1] + 1
        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                nonInc[i] = nonInc[i-1]+1
        for i in range(k, n - k):
            if nonInc[i-1] >= k and nonDec[i+1] >= k:
                res.append(i)
        return res

solution = Solution()
print(solution.goodIndices([2, 1, 1, 1, 3, 4, 1], k=2))
print(solution.goodIndices([2, 1, 1, 2], k=2))
print(solution.goodIndices([878724, 201541, 179099, 98437, 35765, 327555, 475851, 598885, 849470, 943442], 4))
print(solution.goodIndices([478184, 863008, 716977, 921182, 182844, 350527, 541165, 881224], 1))
print(solution.goodIndices([878724, 201541, 179099, 98437, 35765, 327555, 475851, 598885, 849470, 943442], 4))
