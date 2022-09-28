# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        
        if len(stack) == 1:
            return None
        if n == 1:
            stack[-2].next = None
        elif n == len(stack):
            stack[0].next = None
            head = stack[1]
        else:
            stack[-n].next = None
            stack[-(n + 1)].next = stack[-n + 1]
        
        return head
        