# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
            
        for i in range(1, len(arr)):
            if arr[i] >= x:
                continue
                
            j = i 
            while j >= 1 and arr[j - 1] >= x:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
            
        if not arr:
            return None
        
        node = ListNode(arr[0])
        h = node
        for i in range(1, len(arr)):
            node.next = ListNode(arr[i])
            node = node.next
            
        return h

                
            
        