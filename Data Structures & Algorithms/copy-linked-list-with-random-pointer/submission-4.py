"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}

        def dfs(node):
            if not node:
                return None
            if node in copy:
                return copy[node]
            
            copyNode = Node(node.val)

            copy[node] = copyNode
            copyNode.next = dfs(node.next)
            copyNode.random = dfs(node.random)

            return copyNode
        
        return dfs(head)