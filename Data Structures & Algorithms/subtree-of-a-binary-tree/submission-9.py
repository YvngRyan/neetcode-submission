# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return False
            
            if self.checkSub(node, subRoot): return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
        
    def checkSub(self, n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2 or n1.val != n2.val:
            return False
        
        return self.checkSub(n1.left, n2.left) and self.checkSub(n1.right, n2.right)
            