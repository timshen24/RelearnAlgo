from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            curNode = TreeNode(num)
            while stack and stack[-1].val < num:
                node = stack.pop()
                curNode.left = node
            if stack and num < stack[-1].val:
                stack[-1].right = curNode
            stack.append(curNode)
        return stack[0]


solution = Solution()
print(solution.constructMaximumBinaryTree([3, 2, 1, 6]))