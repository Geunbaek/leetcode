# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left and not right:
                return False
            if not left and right:
                return False
            
            if not left and not right:
                return True
           
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) & dfs(left.right, right.left)
                
        return dfs(root.left, root.right)
        