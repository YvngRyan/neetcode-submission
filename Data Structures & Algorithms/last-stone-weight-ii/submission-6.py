class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:


        # Top Down
        total = sum(stones)
        target = total // 2

        cache = {}
        def dfs(i, curr):
            if (i, curr) in cache:
                return cache[(i, curr)]
            if i == len(stones) or curr >= target:
                return abs(curr - (total - curr))
            
            cache[(i, curr)] = min(dfs(i + 1, curr + stones[i]), dfs(i + 1, curr))
            return cache[(i, curr)]
        return dfs(0, 0)