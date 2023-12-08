# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def recur(root):

            ret = ""

            ret += f"{root.val}"
            
            if root.left:
                ret += recur(root.left)
            
            if not root.left and root.right:
                ret += f"()";

            if root.right:
                ret += recur(root.right)

            return f"({ret})"
        
        return recur(root)[1:-1]
        