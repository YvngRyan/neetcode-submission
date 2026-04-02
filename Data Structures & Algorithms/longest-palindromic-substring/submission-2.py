class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        def helper(l, r):
            nonlocal longest
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if not longest or r - l + 1 > len(longest):
                        longest = s[l:r + 1]
                else:
                    break
                l -= 1
                r += 1

        for i in range(len(s)):
            helper(i, i)
        

        for i in range(len(s)):
            helper(i, i + 1)
        return longest


