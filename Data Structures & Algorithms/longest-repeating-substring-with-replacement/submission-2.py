class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {}
        longest = 0
        l = 0

        for r in range(len(s)):
            letters[s[r]]= letters.get(s[r], 0) + 1

            if (r - l + 1) - max(letters.values()) > k:
                letters[s[l]] = letters.get(s[l]) - 1
                l += 1
            
            longest = max(longest, r - l + 1)

        return longest
        