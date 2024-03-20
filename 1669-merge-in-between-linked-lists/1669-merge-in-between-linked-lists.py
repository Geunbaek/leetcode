# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        
        left = head
        right = head
        
        for _ in range(a - 1):
            left = left.next
        
        for _ in range(b + 1):
            right = right.next
            
        left.next = list2
        
        tail = list2
        
        while tail.next:
            tail = tail.next
            
        tail.next = right
        
        return head
            