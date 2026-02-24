# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def recur(node, path):
            if not node.left and not node.right:
                return int(path + str(node.val), 2)
            _sum = 0
            if node.left:
                _sum += recur(node.left, path + str(node.val))
            if node.right:
                _sum += recur(node.right, path + str(node.val))
            return _sum
        return recur(root, "")
