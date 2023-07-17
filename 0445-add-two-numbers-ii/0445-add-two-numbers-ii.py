# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = []
        s1 = []
        s2 = []
        
        n1 = l1
        n2 = l2
        
        while n1:
            s1.append(n1)
            n1 = n1.next
        
        while n2:
            s2.append(n2)
            n2 = n2.next
        
        temp = 0
        
        while s1 or s2:
            if s1 and s2:
                _sum = s1.pop().val + s2.pop().val + temp
            else:
                if s1:
                    _sum = s1.pop().val + temp
                else:
                    _sum = s2.pop().val + temp
            node = ListNode(_sum % 10, None)
            answer.append(node)
            temp = _sum // 10
            
        if temp:
            node = ListNode(temp, None)
            answer.append(node)
            
        head = answer.pop()
        node = head
        
        while answer:
            node.next = answer.pop()
            node = node.next
                    
        return head
                
                        
                    
                