class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        mostFreq = 0
        res = 0
        l = 0
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            mostFreq = max(mostFreq, mp[s[r]])

            if (r - l + 1) - mostFreq <= k:
                res = max(res, r - l + 1)
            else:
                mp[s[l]] -= 1
                l += 1
        return res