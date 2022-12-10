# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            _sum = node.val + dfs(node.left) + dfs(node.right)
            sum_set.add(_sum)

            
            return _sum
        
        sum_set = set()
        _sum = dfs(root)
        left = max(sum_set, key=lambda x: x * abs(_sum - x))
        return (left * abs(_sum - left)) % (1_000_000_007)
        
        
            
            
            
        