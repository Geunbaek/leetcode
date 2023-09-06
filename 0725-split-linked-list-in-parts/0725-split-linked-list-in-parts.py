# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        queue = collections.deque()
        
        node = head
        
        while node:
            queue.append(node)
            node = node.next
            
            
        n = len(queue)
        q = n // k
        r = n % k
        
        s = (k - n) if k > n else 0
        answer = []
        while queue:
            if r > 0:
                front = queue.popleft()
                last = None
                for _ in range(q):
                    if not queue:
                        break
                    last = queue.popleft()
                if last:
                    last.next = None
                else:
                    front.next = None
                answer.append(front)
                r -= 1
            else:
                front = queue.popleft()
                last = None
                for _ in range(q - 1):
                    if not queue:
                        break
                    last = queue.popleft()
                if last:
                    last.next = None
                else:
                    front.next = None
                answer.append(front)
                
        for _ in range(s):
            answer.append(None)
            
        return answer
                