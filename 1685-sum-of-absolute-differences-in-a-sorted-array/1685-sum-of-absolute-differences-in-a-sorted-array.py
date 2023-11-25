class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        
        prefix = [0]
        
        for num in nums:
            prefix.append(num + prefix[-1])
 
        for i in range(n):
            num = nums[i]
            left = abs((i + 1) * num - prefix[i + 1])
            right = abs((n - i - 1) * num - (prefix[n] - prefix[i + 1]))
       
            ans.append(left + right)
            
        return ans
            