class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(c):
            return (ord('a') <= ord(c) <= ord('z') or 
                    ord('A') <= ord(c) <= ord('Z') or 
                    ord('0') <= ord(c) <= ord('9'))
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not isAlphaNum(s[r]):
                r -= 1
            while l < r and not isAlphaNum(s[l]):
                l += 1

            if s[l].upper() != s[r].upper():
                return False
            r -= 1
            l += 1
        return True