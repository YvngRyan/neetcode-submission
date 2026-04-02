class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = math.ceil(stoneSum / 2)

        dp = [ set() for _ in range(len(stones) + 1)]

        dp[0].add(0)

        for i in range(len(stones)):
            for currTotal in dp[i]:
                dp[i + 1].add(currTotal)
                dp[i + 1].add(currTotal + stones[i])
        
        res = stoneSum
        for currTotal in dp[len(stones)]:
            res = min(res, abs(currTotal - (stoneSum - currTotal)))
        return res