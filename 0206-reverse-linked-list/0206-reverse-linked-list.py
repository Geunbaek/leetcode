# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        node = head
        _next = None
        _prev = None
        
        while node.next:
            _next = node.next
            node.next = _prev
            _prev = node
            node = _next
            
        node.next = _prev
        return node
            