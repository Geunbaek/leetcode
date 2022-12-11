# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            _max = max(max(left, right) + node.val, node.val)
            _path = left + right + node.val
            sum_set.add(_max)
            sum_set.add(_path)
            
            return _max
            
        sum_set = set()
        dfs(root)
        print(sum_set)
        return max(sum_set)