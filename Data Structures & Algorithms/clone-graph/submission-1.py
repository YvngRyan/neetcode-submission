"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adjList = {}

        def dfs(node):
            if node in adjList:
                return adjList[node]

            adjList[node] = Node(node.val)
            for neighbor in node.neighbors:
                adjList[node].neighbors.append(dfs(neighbor))
            return adjList[node]
        
        return dfs(node) if node else None
