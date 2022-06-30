from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        col = max(col, 1)
        l, r = 0, row * col - 1
        while l <= r:
            mid = (l + r) // 2
            x = matrix[mid // row -1][mid % col]
            if x < target:
                l = mid + 1
            elif x > target:
                r = mid - 1
            else:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
    print(solution.searchMatrix([[1, 1]], 2))
    print(solution.searchMatrix([[1, 2]], 1))
    print(solution.searchMatrix([[1]], 1))
    print(solution.searchMatrix([[1, 3]], 3))
    print(solution.searchMatrix([[1], [3]], 1))
