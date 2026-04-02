class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        maxHeap = []
        adjList = defaultdict(list)
        visit = set()

        for i in range(len(edges)):
            src, tgt = edges[i]
            adjList[src].append((succProb[i], tgt))
            adjList[tgt].append((succProb[i], src))
        
        heapq.heappush(maxHeap, (-1, start_node))
        
        while maxHeap:
            currSucc, currTgt = heapq.heappop(maxHeap)
            visit.add(currTgt)

            if currTgt == end_node:
                return currSucc * -1

            for nSucc, nTgt in adjList[currTgt]:
                if nTgt not in visit:
                    heapq.heappush(maxHeap, (currSucc * nSucc, nTgt))
        
        return 0