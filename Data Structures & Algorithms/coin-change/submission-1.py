class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i, currAmount):
            if (i, currAmount) in cache:
                return cache[(i, currAmount)]
            if currAmount == 0:
                return 0
            if i == len(coins) or currAmount < 0:
                return -1
            
            minAmount = dfs(i + 1, currAmount)
            minAmount = minAmount if minAmount != -1 else amount + 1

            minAmount2 = dfs(i, currAmount - coins[i])
            minAmount2 = minAmount2 if minAmount2 != -1 else amount + 1

            trueMin = min(minAmount, minAmount2 + 1)

            cache[(i, currAmount)] =  trueMin if trueMin != amount + 1 else -1
            return cache[(i, currAmount)]

        return dfs(0, amount)