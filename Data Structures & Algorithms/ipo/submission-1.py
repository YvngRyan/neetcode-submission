class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capProfits = defaultdict(list)

        for i in range(len(capital)):
            heapq.heappush(capProfits[capital[i]], -profits[i])

        currHeap = []
        res = 0

        capIndex = 0
        caps = sorted(capProfits.keys())
        for i in range(k):
            while capIndex < len(caps) and caps[capIndex] <= w:
                c = caps[capIndex]
                while capProfits[c]:
                    heapq.heappush(currHeap, heapq.heappop(capProfits[c]))
                capIndex += 1
            if not currHeap:
                break
            profit = -heapq.heappop(currHeap)
            res += profit
            w += profit
        return w