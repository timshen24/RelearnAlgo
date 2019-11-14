from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalindrome(s: str) -> bool:
            if not s: return False
            return ("".join(filter(str.isalnum, s)).lower()[::-1]) == ("".join(filter(str.isalnum, s)).lower())

        def backtrack(start):
            if start == len(s):
                res.append(path.copy())
                return res
            for i in range(1, len(s) - start + 1):
                if isPalindrome(''.join(s[start:start + i])):
                    path.append(''.join(s[start:start + i]))
                    backtrack(start + i)
                    path.pop()
            return

        backtrack(0)
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.partition("aab"))