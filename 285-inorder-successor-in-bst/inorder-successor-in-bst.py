# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        inorders = []
        def inorder(node):
            if not node:
                return

            if node.left:
                inorder(node.left)
            
            inorders.append(node)

            if node.right:
                inorder(node.right)
        inorder(root)
        target = inorders.index(p)
        return None if target + 1 >= len(inorders) else inorders[target + 1]