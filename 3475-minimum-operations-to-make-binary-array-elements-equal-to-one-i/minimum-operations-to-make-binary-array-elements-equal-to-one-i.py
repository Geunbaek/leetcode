def swap_zero_one(num):
    return 1 if num == 0 else 0

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        stack = []
        
        for num in nums:
            if len(stack) < 2:
                stack.append(num)
                continue

            if stack[-2] == 0:
                first = stack.pop()
                second = stack.pop()
                
                stack.append(swap_zero_one(second))
                stack.append(swap_zero_one(first))
                stack.append(swap_zero_one(num))
                count += 1
            else:
                stack.append(num)
        if stack[-1] == 0 or stack[-2] == 0:
            return -1
        return count