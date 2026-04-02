class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        cnt = set()
        res = 0
        for r in range(len(s)):
            while s[r] in cnt:
                cnt.remove(s[l])
                l += 1
            
            res = max(r - l + 1, res)
            cnt.add(s[r])
            r += 1
        return res