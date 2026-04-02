class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capProfits = defaultdict(list)

        for i in range(len(capital)):
            capProfits[capital[i]].append(-profits[i])

        currHeap = []
        res = 0
        capIndex = 0
        caps = sorted(capProfits.keys())

        for i in range(k):
            while capIndex < len(caps) and caps[capIndex] <= w:
                c = caps[capIndex]
                for j in range(len(capProfits[c])):
                    heapq.heappush(currHeap, capProfits[c][j])
                capIndex += 1
            if not currHeap:
                break
            profit = -heapq.heappop(currHeap)
            res += profit
            w += profit
        return w