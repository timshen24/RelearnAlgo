class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if (s[i] in s2t and s2t[s[i]] != t[i]) or (t[i] in t2s and t2s[t[i]] != s[i]):
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True

solution = Solution()
print(solution.isIsomorphic("ab", "ca")) # True
print(solution.isIsomorphic("ab", "aa")) # False