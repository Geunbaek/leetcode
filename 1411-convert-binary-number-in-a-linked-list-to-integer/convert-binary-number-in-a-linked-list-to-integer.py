# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        nums = []

        node = head

        while node:
            nums.append(str(node.val))
            node = node.next
        
        return int("0b" + "".join(nums), 2)
