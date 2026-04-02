# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def search(node, lvl):
            if not node:
                return
            if len(res) <= lvl:
                res.append([])
            
            res[lvl].append(node.val)
            search(node.left, lvl + 1)
            search(node.right, lvl + 1)
        
        search(root, 0)
        return res