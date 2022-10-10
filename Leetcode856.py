class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i, e in enumerate(s):
            if e == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack[-1]



solution = Solution()
print(solution.scoreOfParentheses("()"))
print(solution.scoreOfParentheses("(())"))
print(solution.scoreOfParentheses("()()"))
print(solution.scoreOfParentheses("(()(()))"))
print(solution.scoreOfParentheses("(())()"))
