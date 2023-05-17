# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes = []
        node = head
        
        while node:
            nodes.append(node.val)
            node = node.next
            
        answer = 0
        
        for i in range(len(nodes) // 2):
            answer = max(answer, nodes[i] + nodes[-i - 1])
        return answer
        