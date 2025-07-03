class Solution:
    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not self.is_valid_bst(root.left):
            return False

        if self.previous and self.previous.val >= root.val:
            return False

        self.previous = root

        return self.is_valid_bst(root.right)

    def count_nodes(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
        
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.previous = None

        if self.is_valid_bst(root):
            return self.count_nodes(root)
        
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))