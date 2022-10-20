class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k > 1 << n - 2:
            return 1 ^ self.kthGrammar(n - 1, k - (1 << n - 2))
        return self.kthGrammar(n-1, k)

solution = Solution()
print(solution.kthGrammar(1, 1))
print(solution.kthGrammar(2, 1))
print(solution.kthGrammar(2, 2))
print(solution.kthGrammar(3, 1))  # 0
