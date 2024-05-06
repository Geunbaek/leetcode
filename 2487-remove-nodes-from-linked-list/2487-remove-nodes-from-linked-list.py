# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        node = head
        while node:
            value = node.val
            while stack and stack[-1] < value:
                stack.pop()
            stack.append(node.val)
            node = node.next
        
        node = ListNode()
        answer = node
        
        for val in stack:
            node.next = ListNode(val)
            node = node.next
        return answer.next