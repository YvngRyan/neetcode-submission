# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def search(node):
            nonlocal k
            if not node:
                return None
            
            res = search(node.left)
            if res:
                return res
            k -= 1
            if k == 0:
                return node.val
            res = search(node.right)
            if res:
                return res
        
        return search(root)