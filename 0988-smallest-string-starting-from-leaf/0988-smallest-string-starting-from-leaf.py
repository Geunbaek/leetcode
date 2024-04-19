# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def recur(node, word):
            cur = chr(ord("a") + node.val)
            if not node.left and not node.right:
                word = cur + word
                words.append(word)
                return
            
            if node.left:
                recur(node.left, cur + word)
            if node.right:
                recur(node.right, cur + word)
                
            
        words = []
        recur(root, "")
        words.sort()
        return words[0]                