# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        ans = False
        
        def dfs(node, result):
            nonlocal ans
            flag = False
            if node.left:
                flag = True
                dfs(node.left, result + node.val)
            if node.right:
                flag = True
                dfs(node.right, result + node.val)
            if not flag and result + node.val == targetSum:
                ans = True
        dfs(root, 0)
        return ans
        