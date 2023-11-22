class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        h = []
        ans = []
        
        for y in range(len(nums)):
            for x in range(len(nums[y])):
                heapq.heappush(h, (x + y, x, nums[y][x]))
                
        while h:
            ans.append(heapq.heappop(h)[-1])
            
        return ans
        
        
            