class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}

        l = 0
        currLong = 0
        res = 0
        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r], 0) + 1

            currLong = max(currLong, charCount[s[r]])

            while (r - l + 1) - currLong > k:
                charCount[s[l]] -= 1
                l += 1
            
            if (r - l + 1) - currLong <= k:
                res = max(res, r - l + 1)
        return res
            