from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], []

        def backtrack(l, r, path):
            if r == n:
                res.append(path[:])
                return
            if l < n:
                backtrack(l + 1, r, path + "(")
            if r < l:
                backtrack(l, r + 1, path + ")")

        backtrack(0, 0, "")
        return res


solution = Solution()
print(solution.generateParenthesis(3))