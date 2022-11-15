# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            count = 0
            if node:
                if node.left:
                    count += dfs(node.left)
                if node.right:
                    count += dfs(node.right)
                return count + 1
            else:
                return 0
        return dfs(root)
        