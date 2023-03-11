# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
            
        n = len(nodes)
        
        def make_BST(left, right):
            if left > right:
                return None
         
            mid = (left + right) // 2
            parent = TreeNode(nodes[mid].val, make_BST(left, mid - 1), make_BST(mid + 1, right))
            
            return parent
        
        return make_BST(0, n - 1)
            
            
        