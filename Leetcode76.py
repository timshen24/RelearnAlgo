class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = {}, {}
        left, right, start, valid = 0, 0, 0, 0
        length = len(s) + 1
        for c in t:
            need[c] = need.get(c, 0) + 1
        while right < len(s):
            c = s[right]
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            right += 1
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if length == len(s) + 1 else s[start:start + length]

solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))
