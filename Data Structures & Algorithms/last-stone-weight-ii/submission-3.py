class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = math.ceil(stoneSum / 2)

        dp = set()

        dp.add(0)

        for i in range(len(stones)):
            newDp = set()
            for currTotal in dp:
                newDp.add(currTotal)
                newDp.add(currTotal + stones[i])
            dp = newDp
        
        res = stoneSum
        for currTotal in dp:
            res = min(res, abs(currTotal - (stoneSum - currTotal)))
        return res