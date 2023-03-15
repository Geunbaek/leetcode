# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        def bfs():
            q = deque([(root, 0)])
            cur = 0
            
            while q:
                node, val = q.popleft()
                if cur != val:
                    return False
                cur = val + 1
                if node.left:
                    q.append((node.left, val * 2 + 1))
                if node.right:
                    q.append((node.right, val * 2 + 2))
            return True
        
        return bfs()
            
        