class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, res = 0, 0, 0
        st = set()
        while right < len(s):
            if s[right] not in st:
                st.add(s[right])
                right += 1
            else:
                st.remove(s[left])
                left += 1
            res = max(res, right-left)
        return res