class Solution:
    def maxScore(self, s: str) -> int:
        score = int(s[0] == '0') + s[1:].count('1')
        ans = score
        for num in s[1:-1]:
            if num == '0':
                score += 1
            else:
                score -= 1
            ans = max(ans, score)
        return ans

solution = Solution()
print(solution.maxScore("011101"))
print(solution.maxScore("00111"))
print(solution.maxScore("1111"))