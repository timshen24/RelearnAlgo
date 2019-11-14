from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(index):
            if len(path) == k:
                res.append(path.copy())
                return
            for i in range(index, n -k + len(path) + 2):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
