# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nums = []
        
        node = head
        while node:
            nums.append(node.val)
            node = node.next
            
        left, right = 1, len(nums) - 1
        
        node = head
        while left <= right:
            node.next = ListNode(nums[right])
            right -= 1
            node = node.next
            if not (left <= right):
                break
            node.next = ListNode(nums[left])
            left += 1
            node = node.next