from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col, dia1, dia2 = [False for i in range(n)], [False for i in range(2 * n - 1)], [False for i in
                                                                                         range(2 * n - 1)]

        def putQueen(index, row):
            if index == n:
                res.append(row.copy())
                return
            for i in range(n):
                if not col[i] and not dia1[index + i] and not dia2[index - i + n - 1]:
                    row.append(i)
                    col[i] = True
                    dia1[index + i] = True
                    dia2[index - i + n - 1] = True
                    putQueen(index + 1, row)
                    col[i] = False
                    dia1[index + i] = False
                    dia2[index - i + n - 1] = False
                    row.pop()
            return

        putQueen(0, [])
        # <class 'list'>: [[1, 3, 0, 2], [2, 0, 3, 1]]
        res = map(lambda line: list(map(lambda num: '.' *  num + 'Q' + '.' * (n - num - 1), line)), res)
        return list(res)

if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(4))