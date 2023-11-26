class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        res = [0 for _ in range(len(nums))]
        index_nums = [(num, i) for i, num in enumerate(nums)]
        index_nums.sort()
        
        n = len(nums)
        
        start = 0
        
        while start < n:
            num = index_nums[start]
            
            indexs = [num[1]]
            end = start + 1
            
            while end < n and index_nums[end][0] - num[0] <= limit:
                num = index_nums[end]
                indexs.append(index_nums[end][1])
                end += 1
                
            indexs.sort()
            
            for i, j in zip(indexs, range(start, end)):
                res[i] = index_nums[j][0]
                
            start = end
        return res
                
