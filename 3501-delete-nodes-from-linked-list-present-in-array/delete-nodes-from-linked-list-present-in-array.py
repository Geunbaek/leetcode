# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        del_nums = set(nums)

        root = None
        node = head
        tail = root
        
        while node:
            value = node.val 
            if value in del_nums:
                node = node.next
                continue
            if not root:
                root = ListNode(value)
                tail = root
            else:   
                tail.next = ListNode(value)
                tail = tail.next
            node = node.next
        return root