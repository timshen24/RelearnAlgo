from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        path = []
        def backtrack(flag):
            if len(path) == n:
                res.append(int("".join([str(i) for i in path[:]]), 2))
                return
            if flag:
                path.append(0)
                backtrack(flag)
                path.pop()
                path.append(1)
                backtrack(not flag)
                path.pop()
            else:
                path.append(1)
                backtrack(not flag)
                path.pop()
                path.append(0)
                backtrack(flag)
                path.pop()
        backtrack(True)
        return res


solution = Solution()
print(solution.grayCode(2))