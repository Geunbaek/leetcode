# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a_head = ListNode()
        a_node = a_head
        temp = 0
        
        node = head
        
        while node:
            if node.val:
                temp += node.val
            
            if not node.val and temp:
                a_node.next = ListNode(temp)
                a_node = a_node.next
                temp = 0
            node = node.next
        return a_head.next
        
        