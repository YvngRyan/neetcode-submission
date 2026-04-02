# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue = deque([p])
        qQueue = deque([q])

        while pQueue and qQueue:
            for i in range(len(pQueue)):
                nodeP = pQueue.popleft()
                nodeQ = qQueue.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False
                pQueue.append(nodeP.left)
                pQueue.append(nodeP.right)
                qQueue.append(nodeQ.left)
                qQueue.append(nodeQ.right)
        return True