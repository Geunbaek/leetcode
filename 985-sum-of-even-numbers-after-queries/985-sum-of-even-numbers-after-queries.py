class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for n in nums:
            if n % 2 == 0:
                evenSum+=n
        
        ans = []
        for q in queries:
            v, i = q
            if nums[i] % 2 ==0:
                evenSum-=nums[i]
            
            nums[i] += v
            if nums[i] % 2 == 0:
                evenSum += nums[i]
            ans.append(evenSum)
            
        return ans