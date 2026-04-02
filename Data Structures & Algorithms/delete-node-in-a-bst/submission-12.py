# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node):
            if not node:
                return
            
            if node.val > key:
                node.left = delete(node.left)
            elif node.val < key:
                node.right = delete(node.right)
            else:
                if not node.right:
                    return node.left
                if not node.left:
                    return node.right
                
                curr = node.right
                while curr.left:
                    curr = curr.left
                
                node.val = curr.val
                node.right = self.deleteNode(node.right, node.val)
            return node
        
        return delete(root)