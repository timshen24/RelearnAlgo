from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # WRITE YOUR BRILLIANT CODE HERE
        res = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res


solution = Solution()
print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(solution.trap([4, 2, 0, 3, 2, 5]))
