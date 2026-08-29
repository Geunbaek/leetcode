class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        res = [0 for _ in range(len(nums))]
        h = []
        for i, num in enumerate(nums):
            heapq.heappush(h, (num, i))
        
        while h:
            num, index = heapq.heappop(h)
            index_h = [index]
            num_h = [num]
            while h and h[0][0] - num <= limit:
                num, index = heapq.heappop(h)
                heapq.heappush(index_h, index)
                heapq.heappush(num_h, num)
                
            while index_h:
                index = heapq.heappop(index_h)
                num = heapq.heappop(num_h)
                res[index] = num
        
        return res