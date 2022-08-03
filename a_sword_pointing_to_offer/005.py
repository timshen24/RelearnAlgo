from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask = [0] * len(words)
        for i in range(len(words)):
            for j in range(len(words[i])):
                mask[i] |= 1 << (ord(words[i][j]) - ord('a'))

        res = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if mask[i] & mask[j] == 0:
                    res = max(res, len(words[i] * len(words[j])))
        return res