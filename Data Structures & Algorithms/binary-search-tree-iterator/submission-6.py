# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iterator = []
        self.i = 0
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            self.iterator.append(node.val)
            inorder(node.right)
        inorder(root)

    def next(self) -> int:
        val = self.iterator[self.i]
        self.i += 1
        return val
        

    def hasNext(self) -> bool:
        return self.i < len(self.iterator)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()