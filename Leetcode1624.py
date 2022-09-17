class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
            else:
                res = max(res, i - d[c] - 1)
        return res
π
solution = Solution()
print(solution.maxLengthBetweenEqualCharacters("aa"))
print(solution.maxLengthBetweenEqualCharacters("abca"))
print(solution.maxLengthBetweenEqualCharacters("cbzxy"))
