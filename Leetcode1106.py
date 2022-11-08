class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for i, c in enumerate(expression):
            if c == ',':
                continue
            if c != ')':
                stack.append(c)
                continue
            t = f = 0
            if c == ')':
                while stack and stack[-1] != '(':
                    if stack.pop() == 't':
                        t += 1
                    else:
                        f += 1
                stack.pop()
                op = stack.pop()
                if op == '!':
                    stack.append('t' if f == 1 else 'f')
                elif op == '|':
                    stack.append('f' if t == 0 else 't')
                else:
                    stack.append('t' if f == 0 else 'f')
        return stack[-1] == 't'

solution = Solution()
print(solution.parseBoolExpr("!(f)"))
print(solution.parseBoolExpr("|(f,t)"))
print(solution.parseBoolExpr("&(t,f)"))
print(solution.parseBoolExpr("|(&(t,f,t),!(t))"))
print(solution.parseBoolExpr("&(|(f))"))