# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        slow, fast = head, head.next
        
        while slow:
            if fast is None:
                break
            slow.val, fast.val = fast.val, slow.val
            slow = slow.next.next
            if slow is None:
                break
            fast = slow.next
        return head
        
        