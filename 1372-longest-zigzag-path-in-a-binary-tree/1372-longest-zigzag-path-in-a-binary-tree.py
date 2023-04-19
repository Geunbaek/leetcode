# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        
        def dfs(node, prev, depth):
            nonlocal answer
            answer = max(answer, depth)
            
            if node.left:
                if prev == 0:
                    dfs(node.left, 0, 1)
                else:
                    dfs(node.left, 0, depth + 1)
            if node.right:
                if prev == 1:
                    dfs(node.right, 1, 1)
                else:
                    dfs(node.right, 1, depth + 1)
          
        answer = 0
        if root.left:
            dfs(root.left, 0, 1)
        if root.right:
            dfs(root.right, 1, 1)
            
        return answer
        