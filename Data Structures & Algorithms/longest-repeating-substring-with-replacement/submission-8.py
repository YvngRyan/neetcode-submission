class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        mp = {}
        res = 0

        longestCount = 0
        while r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            longestCount = max(mp[s[r]], longestCount)

            while (r - l + 1) - longestCount > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res