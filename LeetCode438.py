from collections import Counter
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, 0
        res = []
        window, need = {}, {}
        for c in p:
            need[c] = need.get(c, 0) + 1
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
            while right - left == len(p):
                d = c[left]
                if window == need:
                    res.append(left)
                if d in need:
                    window[d] -= 1
                    if not window[d]:
                        del window[d]
                left += 1
        return res

solution = Solution()
print(solution.findAnagrams("cbaebabacd", "abc"))