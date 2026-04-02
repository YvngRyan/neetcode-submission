class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            count = 0
            tmpNum = num
            while tmpNum > 0:
                tmpNum = tmpNum & (tmpNum - 1)
                count += 1
            res.append(count)
        return res