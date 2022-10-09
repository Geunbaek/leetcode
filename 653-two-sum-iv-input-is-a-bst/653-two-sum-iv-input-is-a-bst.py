# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        treeNodeValues = []
        def dfs(node):
            if node:
                treeNodeValues.append(node.val)
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
                    
        
        dfs(root)
        for i in range(len(treeNodeValues)):
            for j in range(len(treeNodeValues)):
                if i == j: continue
                if treeNodeValues[i] + treeNodeValues[j] == k:
                    return True
        return False
            