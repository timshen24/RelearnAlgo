from typing import List


class Solution:
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
    res = []

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        self.findCombination(digits, 0, "")
        return self.res

    def findCombination(self, digits, index, s):
        print(f"{index}:{s}")
        if index == len(digits):
            self.res.append(s)
            print(f"get {s}, return")
            return
        c = digits[index]
        letters = self.m[c]
        for i in range(len(letters)):
            print(f"digits[{index}]={c}, use {letters[i]}")
            self.findCombination(digits, index + 1, s + letters[i])
        print(f"digits[{index}]={c} complete, return")

if __name__ == '__main__':
    solution = Solution()
    solution.letterCombinations("234")
    print(solution.res)