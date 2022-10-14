# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        
        node = head
        while node:
            nodes.append(node)
            node = node.next
            
        length = len(nodes)
        if length <= 1:
            return None
        
        
        mid = length // 2
        if length <= mid + 1:
            nodes[mid - 1].next = None
        else:
            nodes[mid - 1].next = nodes[mid + 1]
        return head
        