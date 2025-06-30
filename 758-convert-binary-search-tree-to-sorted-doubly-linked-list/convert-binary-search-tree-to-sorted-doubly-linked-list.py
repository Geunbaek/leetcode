"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        def recur(node):
            nonlocal tail
            if node.left:
                recur(node.left)

            tail.right = node
            node.left = tail
            tail = node

            if node.right:
                recur(node.right)

        head = Node(None)
        tail = head

        recur(root)
        tail.right = head.right
        head.right.left = tail

        return head.right


            