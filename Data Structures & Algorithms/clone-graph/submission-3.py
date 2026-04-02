"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        adjList = {}
        def dfs(node):
            copy = Node(node.val)
            adjList[node] = copy
            for neighbor in node.neighbors:
                if neighbor in adjList:
                    copy.neighbors.append(adjList[neighbor])
                else:
                    copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)