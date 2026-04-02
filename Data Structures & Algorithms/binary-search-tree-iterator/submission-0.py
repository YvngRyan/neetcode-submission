# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.curr = root
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left
        

    def next(self) -> int:
        self.curr = self.stack.pop()
        if self.curr.right:
            temp = self.curr.right
            while temp:
                self.stack.append(temp)
                temp = temp.left
        return self.curr.val
        

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()