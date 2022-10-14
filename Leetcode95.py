from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(start, end):
            if start > end:
                return [None, ]
            allTrees = []
            for i in range(start, end + 1):
                leftTrees = generate(start, i - 1)
                rightTrees = generate(i + 1, end)
                for l in leftTrees:
                    for r in rightTrees:
                        tree = TreeNode(i)
                        tree.left = l
                        tree.right = r
                        allTrees.append(tree)
            return allTrees

        return generate(1, n)

solution = Solution()
print(list(map(lambda x: x.val, solution.generateTrees(3))))