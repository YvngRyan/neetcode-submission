# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            leftM = l + (r - l) // 3
            rightM = r - (r - l) // 3

            if guess(leftM) == 0:
                return leftM
            if guess(rightM) == 0:
                return rightM

            if guess(leftM) + guess(rightM) == 0:
                l = leftM + 1
                r = rightM - 1 
            elif guess(leftM) == -1:
                r = leftM - 1
            else:
                l = rightM + 1