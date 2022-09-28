from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        print(c1, c2)
        diff = 0
        for word, cnt in c1.items():
            if word not in c2:
                diff += c1[word]
            elif c1[word] > c2[word]:
                diff += c1[word] - c2[word]
        return diff


solution = Solution()
print(Counter("leetcode") - Counter("practice"))
print(solution.minSteps("leetcode", "practice"))