class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        dp = [[0] * (target + 1) for _ in range(len(stones) + 1)]
        
        for r in range(len(stones) - 1, -1, -1):
            for c in range(target, -1, -1):
                skip = dp[r + 1][c]
                include = dp[r + 1][c + stones[r]] + stones[r] if c + stones[r] <= target else skip
                dp[r][c] = max(skip, include)
        
        return total - 2 * dp[0][0]


        # # Top Down
        # total = sum(stones)
        # target = total // 2

        # cache = {}
        # def dfs(i, curr):
        #     if (i, curr) in cache:
        #         return cache[(i, curr)]
        #     if i == len(stones) or curr >= target:
        #         return abs(curr - (total - curr))
            
        #     cache[(i, curr)] = min(dfs(i + 1, curr + stones[i]), dfs(i + 1, curr))
        #     return cache[(i, curr)]
        # return dfs(0, 0)