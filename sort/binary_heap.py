class BinaryHeap:
    def __init__(self, heapList):
        self.heapList = heapList
        # self.currentSize = 0

    def upAdjust(self):  # i就是最后一个元素的位置
        child_index = len(self.heapList) - 1
        parent_index = (child_index - 1) // 2
        tmp = self.heapList[child_index]
        while child_index > 0 and tmp < self.heapList[parent_index]:
            self.heapList[child_index] = self.heapList[parent_index]
            child_index = parent_index
            parent_index = (parent_index - 1) // 2
        self.heapList[child_index] = tmp

    def downAdjust(self, parentIndex, length):
        temp = self.heapList[parentIndex]
        childIndex = 2 * parentIndex + 1
        while childIndex < length:
            if childIndex + 1 < length and self.heapList[childIndex + 1] < self.heapList[childIndex]:
                childIndex += 1
            if temp <= self.heapList[childIndex]:
                break
            self.heapList[parentIndex] = self.heapList[childIndex]
            parentIndex = childIndex
            childIndex = 2 * childIndex + 1
        self.heapList[parentIndex] = temp

    def buildHeap(self):
        for i in range(len(self.heapList) // 2, -1, -1):
            self.downAdjust(i, len(self.heapList))


if __name__ == '__main__':
    heapsort = BinaryHeap([1, 3, 2, 6, 5, 7, 8, 9, 10, 0])
    heapsort.upAdjust()
    print(heapsort.heapList)
    heapsort = BinaryHeap([7, 1, 3, 10, 5, 2, 8, 9, 6])
    heapsort.buildHeap()
    print(heapsort.heapList)
