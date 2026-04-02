# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder: tells you what the root node is
        # Inorder: tells you how many nodes are to the left, and how many are to the right
        mp = {}
        for i in range(len(inorder)):
            mp[inorder[i]] = i

        preInd = 0

        def dfs(l, r):
            nonlocal preInd
            if l > r:
                return None
            
            nodeVal = preorder[preInd]
            node = TreeNode(nodeVal)
            preInd += 1
            node.left = dfs(l, mp[nodeVal] - 1)
            node.right = dfs(mp[nodeVal] + 1, r)

            return node
        return dfs(0, len(preorder) - 1)