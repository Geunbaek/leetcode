# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeafs(self, node):
        leaf = []
        flag = False
        if node.left:
            flag = True
            leaf.extend(self.getLeafs(node.left))
        if node.right:
            flag = True
            leaf.extend(self.getLeafs(node.right))
        if not flag:
            return [node.val]
        return leaf
        

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeafs(root1) == self.getLeafs(root2)
            
            
        
        