from queue import Queue

class TreeNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'(\'{self.key}\',\'{self.value}\')'

class BST(object):
    def __init__(self):
        self.__root = None
        self.__count = 0

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    # if key exists, overwrite with new value
    def insert(self, key, value):
        self.__root = self.__insert(self.__root, key, value)
        return self.__root

    # a helper function. insert ``k``, ``v`` into a BST with ``node`` as its root
    # return the root of this newly inserted BST
    def __insert(self, node: TreeNode, key, value) -> TreeNode:
        if not node:
            self.__count += 1
            return TreeNode(key, value)
        if key == node.key:
            node.value = value
        elif key < node.key:
            node.left = self.__insert(node.left, key, value)
        elif key > node.key:
            node.right =  self.__insert(node.right, key, value)
        return node

    def contain(self, key):
        return self.__contain(self.__root, key)

    # search if ``key`` exists in the BST with ``node`` as its root
    def __contain(self, node: TreeNode, key) -> bool:
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self.__contain(node.left, key)
        elif key > node.key:
            return self.__contain(node.right, key)

    # search and return the node in the BST with ``node`` as its root
    def search(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self.search(node.left, key)
        elif key > node.key:
            return self.search(node.right, key)

    def depthFirstTraverse(self):
        self.__depthFirstTraverse(self.__root)

    def __depthFirstTraverse(self, node):
        if not node:
            return
        print(f'(\'{node.key}\',\'{node.value}\')', end=' -> ')
        self.__depthFirstTraverse(node.left)
        self.__depthFirstTraverse(node.right)

    def widthFirstTraverse(self):
        q = Queue()
        q.put(self.__root)
        while not q.empty():
            node = q.get()
            print(f'(\'{node.key}\',\'{node.value}\')', end=' -> ')
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    def __minimum(self, node):
        if not node.left:
            return node
        return self.__minimum(node.left)

    def minimum(self):
         return self.__minimum(self.__root)

    def __maximum(self, node):
        if not node.right:
            return node
        return self.__maximum(node.right)

    def maximum(self):
        return self.__maximum(self.__root)

    # return new BST's root
    def __removeMin(self, node):
        if not node.left:
            rightNode = node.right
            self.__count -= 1
            return rightNode
        node.left = self.__removeMin(node.left)
        return node

    def removeMin(self):
        if self.__root:
            self.__root = self.__removeMin(self.__root)

    # return new BST's root
    def __removeMax(self, node):
        if not node.right:
            leftNode = node.left
            self.__count -= 1
            return leftNode
        node.right = self.__removeMax(node.right)
        return node

    def removeMax(self):
        if self.__root:
            self.__root = self.__removeMax(self.__root)

    # return value is the new BST's root
    def __remove(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self.__remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self.__remove(node.right, key)
            return node
        else:
            if not node.left:
                self.__count -= 1
                return node.right
            if not node.right:
                self.__count -= 1
                return node.left

            successorNode = self.__minimum(node.right)
            successorNode.right = self.__removeMin(node.right)
            successorNode.left = node.left
            return successorNode

    def remove(self, key):
        self.__remove(self.__root, key)

# https://github.com/liuyubobobo/Play-with-Algorithms/blob/20ee257e3ff83f30631f55720e857e2f0d409957/05-Binary-Search-Tree/Course%20Code%20(Java)/Optional-06-Predecessor-and-Successor-in-BST/src/bobo/algo/BST.java


if __name__ == '__main__':
    sentence = "your God is God of God bribes"
    bst = BST()
    root = None
    for word in sentence.split(" "):
        if not bst.contain(word):
            root = bst.insert(word, 1)
        else:
            node = bst.search(root, word)
            if node:
                node.value += 1
    bst.depthFirstTraverse()
    print()
    bst.widthFirstTraverse()
    print()
    # bst.remove("is")
    print(bst.minimum())
    print(bst.maximum())
    print("end")