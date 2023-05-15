# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        
        node = head
        
        while node:
            nodes.append(node.val)
            node = node.next
            
        left = (k - 1)
        right = -(k - 1) - 1
        
        nodes[left], nodes[right] = nodes[right], nodes[left]
        
        root = ListNode(nodes[0])
        node = root
        for i in range(1, len(nodes)):
            node.next = ListNode(nodes[i])
            node = node.next
            
        return root
        