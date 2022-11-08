class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        if n < m:
            return 0

        f = [0] * n
        for i in range(m - 1, n):
            valid = True
            if sequence[i: ] != word[j]:
                    valid = False
                    break
            if valid:
                f[i] = (0 if i == m - 1 else f[i - m]) + 1

        return max(f)


solution = Solution()
print(solution.maxRepeating(sequence="ababc", word="ab"))
print(solution.maxRepeating(sequence="aaabaaaabaaabaaaabaaaabaaaabaaaaba", word="aaaba"))
