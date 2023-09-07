# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack = []
        
        node = head
        while node:
            stack.append(node)
            node = node.next
      
        stack = stack[:left - 1] + stack[left - 1: right][::-1] + stack[right:]
     
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        stack[-1].next = None
            
        return stack[0]
            