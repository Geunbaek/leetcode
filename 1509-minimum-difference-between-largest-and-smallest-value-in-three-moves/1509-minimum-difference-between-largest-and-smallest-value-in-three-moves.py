class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        
        right = nums[3:]
        left = nums[:-3]
        l_right = nums[2:-1]
        r_left = nums[1: -2]
        cases = [right, left, l_right, r_left]
        answer = float('inf')
        
        for case in cases:
            answer = min(answer, case[-1] - case[0])
        
        
        return answer
        
        
        