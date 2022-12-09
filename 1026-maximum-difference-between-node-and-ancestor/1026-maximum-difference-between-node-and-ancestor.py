# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, _max, _min):
            nonlocal answer

            if _max != -1 and _min != float('inf'):
                answer = max(answer, abs(_max - _min), abs(_max - node.val), abs(_min - node.val))
            if node.left:
                dfs(node.left, max(_max, node.val), min(_min, node.val))
            if node.right:
                dfs(node.right, max(_max, node.val), min(_min, node.val))
         
            
        answer = 0
        dfs(root, -1, float('inf'))
        return answer