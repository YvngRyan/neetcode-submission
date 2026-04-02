class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        def bitMask(num):
            count = 0
            while num:
                num = num & (num - 1)
                count += 1
            return count

        for i in range(n + 1):
            res.append(bitMask(i))
        return res