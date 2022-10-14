class Solution:
    def distinctSubseqII(self, s: str) -> int:
        res, n, MOD = 0, len(s), 10 ** 9 + 7

        dp = [0] * 26
        for i in range(len(s)):
            i = ord(s[i]) - ord('a')
            prev = dp[i]
            dp[i] = (1 + res) % MOD
            res = (res + dp[i] - prev) % MOD
        return res


solution = Solution()
print(solution.distinctSubseqII("abc"))
print(solution.distinctSubseqII("aaa"))