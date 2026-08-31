# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []

        now = head.next
        prev = head
        index = 1
        while now.next:
            _next = now.next
            if prev.val < now.val and _next.val < now.val:
                critical_points.append(index)
            if prev.val > now.val and _next.val > now.val:
                critical_points.append(index)
            index += 1
            prev = now
            now = now.next

        if len(critical_points) < 2:
            return [-1, -1]

        _min = float('inf')
        _max = critical_points[-1] - critical_points[0]
        for u, v in zip(critical_points, critical_points[1:]):
            _min = min(_min, v - u)
        return [_min, _max]
