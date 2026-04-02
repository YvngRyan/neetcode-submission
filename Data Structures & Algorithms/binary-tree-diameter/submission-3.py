# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            leftDepth = 0
            rightDepth = 0
            if node.left:
                leftDepth = 1 + dfs(node.left)
            if node.right:
                rightDepth = 1 + dfs(node.right)
            res = max(res, leftDepth + rightDepth)

            return max(leftDepth, rightDepth)
        dfs(root)
        return res