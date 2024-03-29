"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque([root])
        while q:
            prev = q[0]
            for _ in range(len(q)):
                node = q.popleft()
                if node != prev:
                    prev.next = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                prev = node
        return root