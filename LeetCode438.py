from collections import Counter
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start, end = 0, 0
        ans = []
        c_counter, p_counter = Counter(), Counter(p)
        while start < len(s):
            if len(p) > end - start and end < len(s):
                c_counter[s[end]] += 1
                end += 1
            else:
                if c_counter == p_counter:
                    ans.append(start)
                c_counter[s[start]] -= 1
                if c_counter[s[start]] == 0:
                    del c_counter[s[start]]
                start += 1
        return ans

solution = Solution()
print(solution.findAnagrams("cbaebabacd", "abc"))