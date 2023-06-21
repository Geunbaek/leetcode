class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def get_cost(num):
            return sum(abs(num - n) * c for n, c in zip(nums, cost))
    
        left, right = 0, 1_000_001
        answer = get_cost(nums[0])
        
        while left <= right:
            mid = (left + right) // 2
            
            cost1 = get_cost(mid)
            cost2 = get_cost(mid + 1)
            answer = min(cost1, cost2)
            
            if cost1 > cost2:
                left = mid + 1
            else:
                right = mid - 1
        return answer
            
            
            
        