# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def doubleStringNumber(stringNum):
            n = len(stringNum)
            q = deque()
            
            temp = 0
            for i in range(n-1, -1, -1):
                now = int(stringNum[i]) * 2 + temp
                upper = now // 10
                lower = now % 10
                q.appendleft(str(lower))
                temp = upper
            if temp > 0:
                q.appendleft(str(temp))
            return "".join(q)
        
        s = ""
        
        node = head
        while node:
            s += str(node.val)
            node = node.next
            
        s = doubleStringNumber(s)
        ret = ListNode()
        node = ret
        for c in s:
            node.next = ListNode(int(c))
            node = node.next
        return ret.next