from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        root.val = 1
        queue = deque([root])
        while queue:
            minId = maxId = -1
            for _ in range(len(queue)):
                node = queue.popleft()
                maxId = node.val
                if minId == -1:
                    minId = maxId
                if node.left:
                    node.left.val = maxId << 1
                    queue.append(node.left)
                if node.right:
                    node.right.val = maxId << 1 | 1
                    queue.append(node.right)
            res = max(res, maxId - minId + 1)
        return res