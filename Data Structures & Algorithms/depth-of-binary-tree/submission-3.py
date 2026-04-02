# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        res = 0
        q.append([root, 1])

        while q:
            node, level = q.popleft()

            if node:
                q.append([node.left, level + 1])
                q.append([node.right, level + 1])
                res = max(res, level)
        return res