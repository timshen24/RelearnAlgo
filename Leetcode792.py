from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)
        res = len(words)
        for word in words:
            if len(word) > len(s):
                res -= 1
                continue
            p = -1
            for c in word:
                ps = pos[c]
                j = bisect_right(ps, p)
                if j == len(ps):
                    res -= 1
                    break
                p = ps[j]
        return res

solution = Solution()
print(solution.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))
print(solution.numMatchingSubseq(s="dsahjpjauf", words=["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))
