class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1
        s = [''] * n
        s[:3] = '122'
        res = 1
        i, j = 2, 3
        while j < n:
            size = int(s[i])
            num = 3 - int(s[j - 1])
            k = 0
            while k < size and j < n:
                s[j] = str(num)
                if num == 1:
                    res += 1
                j += 1
            i += 1
        return res


solution = Solution()
print(solution.magicalString(6))