# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(node):
            if not node:
                return 0, True
            
            l, l_balanced = get_depth(node.left)
            r, r_balanced = get_depth(node.right)
            if not l_balanced or not r_balanced:
                return 0, False
            return max(l + 1, r + 1), abs(l - r) <= 1
        return get_depth(root)[1]
