class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = {}

        mostF = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            mostF = max(count[s[r]], mostF)
            
            while (r - l + 1) - mostF > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res