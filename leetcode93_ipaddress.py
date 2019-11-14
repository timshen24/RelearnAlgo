from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        def backtrack(index):
            if len(path) == 4 and index == len(s):
                res.append(".".join(path.copy()))
                return
            elif len(path) == 4 or index >= len(s):
                return
            for i in range(1, 4):
                if i > 1 and s[index] == '0':
                    continue
                if 0 <= int(s[index:index + i]) <= 255:
                    path.append(s[index:index + i])
                    backtrack(index + i)
                    path.pop()
            return
        backtrack(0)
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.restoreIpAddresses("1111"))