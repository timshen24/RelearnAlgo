class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        cur, nextBegin = 0, 0
        res = []
        for i, num in enumerate(s):
            cur += 1 if num == "1" else -1
            if cur == 0:
                res.append("1" + self.makeLargestSpecial(s[nextBegin+1:i]) + "0")
                nextBegin = i + 1
        return "".join(sorted(res, reverse=True))


# Thanks for amazing idea:
# here is the process of 11011000:
# level 1 : 1 + makeLargestSpecial( 101100) + 0,
# level 2 : 10 + 1100.we need to makeLargestSpecial(10) and makeLargestSpecial(1100)
# level 3 : makeLargestSpecial(10) will just return 10, and makeLargestSpecial(1100) will return 1100
# go back to level 2, we need to sort 10 and 1100, it will be 1100, 10, now we swap once,
# go back to level 1, we join them together : 1 1100 10 0, end .

solution = Solution()
print(solution.makeLargestSpecial("11011000"))
print(solution.makeLargestSpecial("10"))