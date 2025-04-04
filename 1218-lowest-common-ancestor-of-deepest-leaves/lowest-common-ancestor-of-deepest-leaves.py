# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(depth, node, parent):
            if not node:
                return (depth, parent)

            l_d, l_p = recur(depth + 1, node.left, node)
            r_d, r_p = recur(depth + 1, node.right, node)

            if l_d < r_d:
                return (r_d, r_p)
            elif l_d > r_d:
                return (l_d, l_p)
            else:
                return (l_d, node)

        d, p = recur(0, root, None)
        return p