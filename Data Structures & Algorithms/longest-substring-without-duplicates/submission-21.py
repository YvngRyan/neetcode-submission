class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()

        l, r = 0, 0

        res = 0
        while r < len(s):
            while s[r] in count:
                count.remove(s[l])
                l += 1
            count.add(s[r])
            res = max(r - l + 1, res)
            r += 1
        return res