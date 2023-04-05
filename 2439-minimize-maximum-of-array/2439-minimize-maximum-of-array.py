class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = max(nums)
        left, right = 0, ans
        while left <= right:
            mid = (left + right) // 2
            copy_nums = [num for num in nums]
            for i in range(len(nums) - 1, 0, -1):
                if copy_nums[i] <= mid:
                    continue
                
                diff = copy_nums[i] - mid
                copy_nums[i] -= diff
                copy_nums[i - 1] += diff
       
            if mid >= copy_nums[0]:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans
                    
                
            
        
        