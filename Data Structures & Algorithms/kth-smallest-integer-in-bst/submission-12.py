# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt, res = k, root.val
        def search(node):
            nonlocal cnt, res
            if not node:
                return None
            
            search(node.left)
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            search(node.right)
        
        search(root)
        return res