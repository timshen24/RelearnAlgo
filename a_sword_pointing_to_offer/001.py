class Solution:
    def divide(self, a: int, b: int) -> int:
        flag = False if (a > 0 and b > 0) or (a < 0 and b < 0) else True
        a, b = abs(a), abs(b)

        def calc(a, b):
            n = 1
            while a > b << 1:
                b <<= 1
                n <<= 1
            return n, b

        ret = 0
        while a >= b:
            cnt, val = calc(a, b)
            ret += cnt
            a -= val
        ret = -ret if flag else ret
        ret = ret - 1 if ret == 2 ** 31 else ret
        return ret


solution = Solution()
print(solution.divide(15, 2))