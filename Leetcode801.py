from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[float('inf'), float('inf')] for _ in range(len(nums1))]
        dp[0] = [0, 1]
        for i in range(1, len(nums1)):
            if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1] + 1
            if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
                dp[i][0] = min(dp[i][0], dp[i-1][1])
                dp[i][1] = min(dp[i][1], dp[i-1][0] + 1)
        return int(min(dp[-1]))


solution = Solution()
print(solution.minSwap(nums1=[1, 3, 5, 4], nums2=[1, 2, 3, 7]))
print(solution.minSwap(nums1=[0, 3, 5, 8, 9], nums2=[2, 1, 4, 6, 9]))
print(solution.minSwap(nums1=[0, 4, 4, 5, 9], nums2=[0, 1, 6, 8, 10]))
print(solution.minSwap(nums1=[3, 3, 8, 9, 10], nums2=[1, 7, 4, 6, 8]))
