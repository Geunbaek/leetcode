# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def recur(node, d):
            if d > depth:
                return
            if d == depth - 1:
                left = node.left
                node.left = TreeNode(val, left)
                right = node.right
                node.right = TreeNode(val, None, right)
            if node.left:
                recur(node.left, d + 1)
            if node.right:
                recur(node.right, d + 1)
    
        if depth == 1:
            new_root = TreeNode(val, root);
            return new_root
        recur(root, 1)
        return root