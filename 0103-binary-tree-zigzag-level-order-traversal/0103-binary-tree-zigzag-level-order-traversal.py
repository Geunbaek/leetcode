# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        answer = [[] for _ in range(2001)]
        max_depth = 0
        
        def dfs(node, depth):
            nonlocal max_depth
            if node is None:
                return
            
            max_depth = max(max_depth, depth)
            answer[depth].append(node.val)
           
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1) 
                
        dfs(root, 0)
        
        for i in range(max_depth + 1):
            if i % 2 != 0:
                answer[i] = answer[i][::-1]
                
        return answer[:max_depth + 1]