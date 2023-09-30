class Solution(object):
    def find132pattern(self, nums):
        stack=[]
        n = float('-inf')
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < n:
                return True
            
            while stack and stack[-1] < nums[i]:
                n = stack.pop()
                
            stack.append(nums[i])
            
        return False