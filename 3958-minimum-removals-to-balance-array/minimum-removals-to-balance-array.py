class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        r = 0   
        answer = 0
        for l in range(n):
            while r + 1 < n and nums[l] * k >= nums[r + 1] :
                r += 1
            answer = max(answer, (r - l + 1))
        return n - answer



            
