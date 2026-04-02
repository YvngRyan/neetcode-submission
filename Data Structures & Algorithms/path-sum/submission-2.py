# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtrack(node, currSum):
            if not node:
                return False
            
            currSum += node.val
            
            if currSum == targetSum:
                if not node.left and not node.right:
                    return True
            
            return backtrack(node.left, currSum) or backtrack(node.right, currSum)
        
        return backtrack(root, 0)
