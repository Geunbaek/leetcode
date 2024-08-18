# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node):
            nonlocal answer
            if not node:
                return 0
            
            ret = 0
            left = 0
            right = 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            answer += abs(left - right)
            
            return left + right + node.val
        dfs(root)
        return answer
            
        