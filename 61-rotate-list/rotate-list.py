# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        tail = head
        n = 1
        while tail.next:
            n += 1
            tail = tail.next
    
        k %= n
        diff = n - k
        if k == 0 or n == 1 or n == k:
            return head
        node = head
        prev = None
        for _ in range(diff):
            prev = node
            node = node.next
        prev.next = None
        tail.next = head
        return node
        