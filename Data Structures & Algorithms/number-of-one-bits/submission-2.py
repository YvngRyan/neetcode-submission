class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            mask = n & 1
            if mask == 1:
                count += 1
            n >>= 1
        return count