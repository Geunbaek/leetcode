# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes=[]
        for li in lists:
            n = li
            while n:
                nodes.append(n.val)
                n=n.next
        nodes.sort()
        node = None
        head = None
        for i, n in enumerate(nodes):
            _next = ListNode(n)
            if i == 0:
                head = _next
            if node:
                node.next = _next
            node = _next
        return head
            
                
        
        
        
        
        