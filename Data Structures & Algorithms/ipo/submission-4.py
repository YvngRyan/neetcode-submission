class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if not capital or not profits:
            return 0

        projCaps = defaultdict(list)
        maxProj = []

        for i in range(len(capital)):
            projCaps[capital[i]].append(profits[i])

        sortedCaps = sorted(projCaps.keys())
        capIdx = 0

        for i in range(k):
            while capIdx < len(sortedCaps) and sortedCaps[capIdx] <= w:
                c  = sortedCaps[capIdx]
                for j in range(len(projCaps[c])):
                    heapq.heappush(maxProj, -projCaps[c][j])
                capIdx += 1
            if not maxProj:
                break
            profit = -heapq.heappop(maxProj)
            w += profit
        return w