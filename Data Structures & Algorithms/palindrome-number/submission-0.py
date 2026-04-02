class Solution:
    def isPalindrome(self, x: int) -> bool:
        sX = str(x)

        l, r = 0, len(sX) - 1

        while l < r:
            if sX[l] != sX[r]:
                return False
            l += 1
            r -= 1
        return True