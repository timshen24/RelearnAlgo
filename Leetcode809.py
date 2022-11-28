from typing import List

s = "zzzzzyyyyy"


def expand(s: str, t: str) -> bool:
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            return False
        ch = s[i]
        cnti = 0
        while i < len(s) and s[i] == ch:
            cnti += 1
            i += 1
        cntj = 0
        while j < len(t) and t[j] == ch:
            cntj += 1
            j += 1

        if cnti < cntj:
            return False
        if cnti != cntj and cnti < 3:
            return False

    return i == len(s) and j == len(t)


# def expand(s: str, t: str) -> bool:
#     i = j = 0
#     while i < len(s) and j < len(t):
#         c1 = s[i]
#         c2 = t[j]
#         if c1 != c2:
#             return False
#         cnt1 = 0
#         while i < len(s) and s[i] == c1:
#             i += 1
#             cnt1 += 1
#         cnt2 = 0
#         while j < len(t) and t[j] == c2:
#             j += 1
#             cnt2 += 1
#         if cnt1 < cnt2:
#             return False
#         if 1 < cnt1 // cnt2 < 3:
#             return False
#     return i == len(s) and j == len(t)


print(expand(s, "zzyy"))
print(expand(s, "zy"))
print(expand(s, "zyy"))
class Solution:
    pass
    # def expressiveWords(self, s: str, words: List[str]) -> int:
    #
    #     return sum([ifexpressive(word) for word in words])


solution = Solution()

# print(solution.expressiveWords("heeellooo", ["hello", "hi", "helo"]))
