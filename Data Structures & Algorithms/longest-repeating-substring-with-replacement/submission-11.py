class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        mp = {}
        longestChar = 0
        res = 0

        while r < len(s):
            mp[s[r]] = mp.get(s[r], 0) + 1
            longestChar = max(mp[s[r]], longestChar)

            while (r - l + 1)  - k > longestChar:
                mp[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
            r += 1
        return res