class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = 0
        e = len(s) - 1

        while b < e:
            while b < e and not self.alphaNum(s[b]):
                b += 1
            while e > b and not self.alphaNum(s[e]):
                e -= 1
            if s[b].lower() == s[e].lower():
                b += 1
                e -= 1
            else:
                return False
        return True


    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        