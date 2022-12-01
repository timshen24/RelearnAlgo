from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        leftCount = rightCount = leftCost = rightCost = 0
        for i in range(1, len(ans)):
            if boxes[i-1] == '1':
                leftCount += 1
            leftCost += leftCount
            ans[i] += leftCost
        for i in range(len(ans)-2, -1, -1):
            if boxes[i+1] == '1':
                rightCount += 1
            rightCost += rightCount
            ans[i] += rightCost
        return ans


solution = Solution()
print(solution.minOperations("110"))