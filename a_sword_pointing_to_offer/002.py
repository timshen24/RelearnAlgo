class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rev_a, rev_b = a[::-1], b[::-1]
        i, carry, temp = 0, 0, 0
        res = ""
        while i < len(rev_a) or i < len(rev_b):
            if i < len(rev_a) and i < len(rev_b):
                temp = int(rev_a[i]) + int(rev_b[i]) + carry
            elif len(rev_a) <= i < len(rev_b):
                temp = int(rev_b[i]) + carry
            elif len(rev_b) <= i < len(rev_a):
                temp = int(rev_a[i]) + carry
            if temp >= 2:
                temp -= 2
                carry = 1
            else:
                carry = 0
            res += str(temp)
            i += 1
        return res[::-1] if carry == 0 else "1" + res[::-1]


solution = Solution()
print(solution.addBinary("11", "10"))
print(solution.addBinary("1010", "1011"))
print(solution.addBinary("1", "111"))
print(solution.addBinary("100", "110010"))
print(solution.addBinary("110010", "10111"))