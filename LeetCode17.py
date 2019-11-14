from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        s = []
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def findCombinations(index):
            if index == len(digits):
                res.append("".join(s))
                return

            for letter in m[digits[index]]:
                s.append(letter)
                findCombinations(index + 1)
                s.pop()
            return
        findCombinations(0)
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations("23"))
