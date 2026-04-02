class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        def dfs(node, par):
            if node in visit:
                return True

            visit.add(node)

            for neighbor in adjList[node]:
                if neighbor == par:
                    continue
                if dfs(neighbor, node):
                    return True
            return False


        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
            visit = set()
            if dfs(v1, -1):
                return [v1, v2]
        return []