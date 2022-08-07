from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        # self.sumMat = [[0] * COLS] * ROWS
        for i in range(len(matrix)):
            rowSum = 0
            for j in range(len(matrix[0])):
                rowSum += matrix[i][j]
                self.sumMat[i+1][j+1] = self.sumMat[i][j+1] + rowSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumMat[row2 + 1][col2 + 1] - self.sumMat[row1][col2 + 1] - self.sumMat[row2 + 1][col1] + self.sumMat[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# [2,1,4,3],[1,1,2,2],[1,2,2,4]]
obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(obj.sumMat)