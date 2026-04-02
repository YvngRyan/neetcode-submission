class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = math.ceil(stoneSum / 2)
        

        # stoneSum = 23
        # target = 12
        # currTotal = 12
        # diff = 11
        # res = 1
        cache = {}
        def dfs(i, currTotal):
            if currTotal >= target or i == len(stones):
                return abs(currTotal - (stoneSum - currTotal))
            
            if (i, currTotal) in cache:
                return cache[(i, currTotal)]
            
            cache[(i, currTotal)] = min(dfs(i + 1, currTotal), dfs(i + 1, currTotal + stones[i]))

            return cache[(i, currTotal)]
        
        return dfs(0, 0)