class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        adjList = defaultdict(list)

        for src, tgt in tickets:
            adjList[src].append(tgt)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adjList:
                return False
            
            tmp = list(adjList[src])
            for i, tgt in enumerate(tmp):
                adjList[src].pop(i)
                res.append(tgt)
                if dfs(tgt): return True

                adjList[src].insert(i, tgt)
                res.pop()
            
            return False
        
        dfs("JFK")
        return res