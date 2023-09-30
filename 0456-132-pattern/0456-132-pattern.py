class Solution(object):
    def find132pattern(self, nums):
        stack = []
        
        n = float("-inf")
        
        for num in nums[::-1]:
            if num < n:
                return True
            
            while stack and stack[-1] < num:
                n = stack.pop()
                
            stack.append(num)
            
        return False
        