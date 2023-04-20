# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import defaultdict
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node, index, depth):
            depth_info[depth].append(index)
            if node.left:
                dfs(node.left, index * 2, depth + 1)
            if node.right:
                dfs(node.right, index * 2 + 1, depth + 1)
        
        depth_info = defaultdict(list)
        dfs(root, 1, 0)
        answer = 0
        for key, val in depth_info.items():
            sorted_value = sorted(val)
            answer = max(answer, sorted_value[-1] - sorted_value[0] + 1)
            
        return answer
                    
                
            
            
        