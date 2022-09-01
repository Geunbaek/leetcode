# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path = []
        self.goodNodesCount = 0
    
    def goodNodes(self, root: TreeNode) -> int:
        _max = max(self.path) if self.path else -10001
        if _max <= root.val: self.goodNodesCount += 1
        self.path.append(root.val)
        if root.left:
            self.goodNodes(root.left)
            self.path.pop()
        if root.right:
            self.goodNodes(root.right)
            self.path.pop()
        return self.goodNodesCount
        
        
        