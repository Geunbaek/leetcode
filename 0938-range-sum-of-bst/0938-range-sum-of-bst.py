# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        val = root.val
        
        _sum = val if low <= val <= high else 0
        
        _sum += self.rangeSumBST(root.left, low, high)
        _sum += self.rangeSumBST(root.right, low, high)
        return _sum
        
        
        