class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        res = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] in substring:
                while s[l] != s[r]:
                    substring.remove(s[l])
                    l += 1
                l += 1
            else:
                substring.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res