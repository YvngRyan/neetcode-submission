class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in count:
                while s[l] != s[r]:
                    count.remove(s[l])
                    l += 1
                l += 1
            count.add(s[r])
            res = max(res, r - l + 1)
        return res