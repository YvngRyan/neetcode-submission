class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l = 0

        longest = 0
        res = 0
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            longest = max(mp[s[r]], longest)

            if (r - l + 1) - longest > k:
                mp[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res
            

            
