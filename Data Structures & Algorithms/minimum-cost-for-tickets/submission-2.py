class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        idxToDays = { 0 : 1, 1 : 7, 2 : 30}
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(days):
                return 0
            
            cache[i] = float("inf")
            for c in range(len(costs)):
                cost = costs[c]
                duration = idxToDays[c]
                j = i
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                cache[i] = min(cache[i], dfs(j) + cost)
            return cache[i]
        return dfs(0)