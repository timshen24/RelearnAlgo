class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def add_level(self, tree, val, depth):
        def add_level_n(tree, val, depth, n):
            if n + 1 == depth:
                l = tree.left
                r = tree.right
                tree.left = TreeNode(val, l, None)
                tree.right = TreeNode(val, None, r)
                return
            else:
                n += 1
                add_level_n(tree.left, val, depth, n)
                add_level_n(tree.right, val, depth, n)
        return add_level_n(tree, val, depth, 0)

if __name__ == '__main__':
    r = TreeNode(0, None, None)
    l1 = TreeNode(1, None, None)
    l2 = TreeNode(2, None, None)
    l3 = TreeNode(3, None, None)
    l4 = TreeNode(4, None, None)
    l1.left = l3
    l1.right = l4
    r.left = l1
    r.right = l2
    solution = Solution()
    solution.add_level(r, 2, 1)
    print(r.left.val)
    print(r.right.val)
    print(r.left.left.val)
    print(r.left.left.left.val)
    print(r.left.left.right.val)
    print(r.right.right.val)

    print(r)