# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_values.append({
                "value": node.val,
                "diff": abs(node.val - target)
            })
            inorder(node.right)
        
        sorted_values = []
        inorder(root)
        sorted_values.sort(key=lambda x: x["diff"])
        return list(map(lambda x: x['value'], sorted_values[:k]))
