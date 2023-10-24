# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        cache = dict()
        
        def dfs(node, depth):
            if node is None:
                return
            
            if depth in cache:
                cache[depth] = max(cache[depth], node.val)
            else:
                cache[depth] = node.val
                
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return cache.values()
                
            
        