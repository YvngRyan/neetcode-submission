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
        q = collections.deque([node])
        adjList[node] = Node(node.val)

        while q:
            currNode = q.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in adjList:
                    adjList[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                adjList[currNode].neighbors.append(adjList[neighbor])
        return adjList[node]