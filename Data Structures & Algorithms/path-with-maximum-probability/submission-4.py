class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = { node : [] for node in range(n) }
        for i in range(len(edges)):
            n1, n2 = edges[i]
            prob = succProb[i]
            adjList[n1].append((prob, n2))
            adjList[n2].append((prob, n1))
        
        maxHeap = [(-1, start_node)]
        visit = set()

        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            visit.add(node)
            if node == end_node:
                return -prob
            
            for nProb, n in adjList[node]:
                if n not in visit:
                    heapq.heappush(maxHeap, (prob * nProb, n))
        
        return 0