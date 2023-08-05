# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from itertools import permutations

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return
        
        node = self.root
        while node:
            if value > node.val:
                if not node.right:
                    node.right = TreeNode(value)
                    break
                node = node.right
            elif value < node.val:
                if not node.left:
                    node.left = TreeNode(value)
                    break
                node = node.left
        
        
class Solution:
    def is_equal(r1, r2):
        if not r1 and not r2:
            return True
        
        if not r1 and r2:
            return False
        
        if r1 and not r2:
            return False
            
        if r1.val != r2.val:
            return False
    
        return Solution.is_equal(r1.left, r2.left) and Solution.is_equal(r1.right, r2.right)
            
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        answer = []
        for perm in permutations([i for i in range(1, n + 1)], n):
            bst = BST()
            for value in perm:
                bst.insert(value)
                
            for tree in answer:
                if Solution.is_equal(tree, bst.root):
                    break
            else:
                answer.append(bst.root)
        return answer
                
            
    
        