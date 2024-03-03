# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def recur(slow, fast, n, depth):
            if fast is None:
                if slow.next is None:
                    slow.next = None
                else:
                    slow.next = slow.next.next
                return
            
            if depth > n:
                recur(slow.next, fast.next, n, depth + 1)
            else:
                recur(slow, fast.next, n, depth + 1)
        
        dummy = ListNode(0, head)
        recur(dummy, dummy, n, 0)
        
        return dummy.next
    
        