# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        cache = {value: i for i, value in enumerate(inorder)}

        def get_tree(l, r):
            if l > r:
                return
            
            value = postorder.pop()
            
            parent = TreeNode(value)
            p_index = cache[value]
            
            parent.right = get_tree(p_index + 1, r)
            parent.left = get_tree(l, p_index - 1)
            return parent
        
        return get_tree(0, len(inorder) - 1)
            
        