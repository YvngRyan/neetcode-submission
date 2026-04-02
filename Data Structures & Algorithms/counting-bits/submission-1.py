class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            currOnes = 0
            tempNum = num
            while tempNum:
                tempNum = tempNum & (tempNum - 1)
                currOnes += 1
            res.append(currOnes)
        return res