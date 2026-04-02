# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, highVal):
            if not node:
                return 0
            
            if node.val >= highVal:
                return 1 + (dfs(node.left, node.val) + dfs(node.right, node.val))
            else:
                return (dfs(node.left, highVal) + dfs(node.right, highVal))
        
        return dfs(root, root.val)