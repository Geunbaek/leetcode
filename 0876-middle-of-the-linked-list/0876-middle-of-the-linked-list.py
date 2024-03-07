# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        nodes = []
        index = -1
        
        while node:
            nodes.append(node)
            node = node.next
            index += 1
        
        mid = index // 2 if index % 2 == 0 else index // 2 + 1
        return nodes[mid]
        
        