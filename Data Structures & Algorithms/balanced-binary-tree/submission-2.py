# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (0, True)
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            if not leftHeight[1] or not rightHeight[1] or abs(leftHeight[0] - rightHeight[0]) > 1:
                return (1 + max(leftHeight[0], rightHeight[0]), False)

            return (1 + max(leftHeight[0], rightHeight[0]), True)
        return dfs(root)[1]