class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        ans = float('-inf')
        
        while i < n:
            l = i  
            i += 1
            
            while i < n and nums[i - 1] < nums[i]:
                i += 1
            
            if i == l + 1:
                continue
            
            p = i - 1  
            
            s = nums[p - 1] + nums[p]
            
            while i < n and nums[i - 1] > nums[i]:
                s += nums[i]
                i += 1
            
            if i == p + 1 or i == n or nums[i - 1] == nums[i]:
                continue
            
            q = i - 1  
            
            s += nums[i]  
            i += 1
            
            mx = 0
            t = 0
            while i < n and nums[i - 1] < nums[i]:
                t += nums[i]
                mx = max(mx, t)
                i += 1
            s += mx
            
            mx = 0
            t = 0
            j = p - 2
            while j >= l:
                t += nums[j]
                mx = max(mx, t)
                j -= 1
            s += mx
            
            ans = max(ans, s)
            
            i = q
        
        return ans