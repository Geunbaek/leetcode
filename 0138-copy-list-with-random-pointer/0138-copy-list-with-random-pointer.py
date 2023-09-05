"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        
        temp = head
        
        cache = dict()
        
        while temp:
            cache[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp.next:
            cache[temp].next = cache[temp.next]
            temp = temp.next
            
        temp = head
        while temp:
            if temp.random is not None:
                cache[temp].random = cache[temp.random]
            temp = temp.next
            
            
        return cache[head]
            
        