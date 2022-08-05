from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        q = deque([root])
        level = 0
        while q:
            qLen = len(q)
            level += 1
            for _ in range(qLen):
                curNode = q.popleft()
                if level == depth - 1:
                    curNode.left = TreeNode(val, curNode.left, None)
                    curNode.right = TreeNode(val, None, curNode.right)
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
        return root


solution = Solution()
tree = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
root = solution.addOneRow(tree, 1, 2)
