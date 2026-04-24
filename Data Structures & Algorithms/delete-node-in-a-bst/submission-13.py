# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(node):
            curr = node
            while curr and curr.left:
                curr = curr.left
            return curr
            
        
        def remove(node):
            if not node:
                return None
            
            if node.val > key:
                node.left = remove(node.left)
            elif node.val < key:
                node.right = remove(node.right)
            else:
                if not node.right:
                    return node.left
                if not node.left:
                    return node.right
                
                minRight = findMin(node.right)
                node.val = minRight.val
                node.right = self.deleteNode(node.right, minRight.val)

            return node
        return remove(root)
                
