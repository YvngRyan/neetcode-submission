class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        idxToDays = { 0 : 1, 1 : 7, 2 : 30}

        dp = [0] * (len(days) + 1)

        for i in range(len(days) -1, -1, -1):
            dp[i] = float("inf")
            for c in range(len(costs)):
                cost = costs[c]
                duration = idxToDays[c]
                j = i
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                dp[i] = min(dp[i], cost + dp[j])
        return dp[0]