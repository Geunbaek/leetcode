# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        _sum = 0
        
        def dfs(node):
            nonlocal _sum
            if low <= node.val <= high:
                _sum += node.val
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            
        dfs(root)
        return _sum
        