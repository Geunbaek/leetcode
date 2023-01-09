# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        order=[root.val]
        order.extend(self.preorderTraversal(root.left))
        order.extend(self.preorderTraversal(root.right))
        return order