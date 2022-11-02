from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        curMax = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            curMax = max(curMax, arr[i + 1])
            res[i] = curMax
        return res


solution = Solution()
print(solution.replaceElements([17, 18, 5, 4, 6, 1])) # [18,6,6,6,1,-1]
print(solution.replaceElements([400])) # [-1]