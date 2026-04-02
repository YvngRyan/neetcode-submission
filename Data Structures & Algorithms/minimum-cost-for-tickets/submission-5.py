class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        passToDays = {0 : 1, 1 : 7, 2: 30}

        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(days):
                return 0
            
            cache[i] = float('inf')
            for j in range(len(costs)):
                cost = costs[j]
                newI = i

                while newI < len(days) and days[newI] < days[i] + passToDays[j]:
                    newI += 1
                totalCost = cost + dfs(newI)
                cache[i] = min(totalCost, cache[i])
            return cache[i]
        return dfs(0)