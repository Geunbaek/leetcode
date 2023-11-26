class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        res = [0 for _ in range(len(nums))]
        index_nums = [(num, i) for i, num in enumerate(nums)]
        index_nums.sort()
        index_nums = deque(index_nums)
        
        
        while index_nums:
            num, i = index_nums.popleft()
            indexs = [i]
            nums = [num]
            while index_nums and index_nums[0][0] - num <= limit:
                num, i = index_nums.popleft()
                indexs.append(i)
                nums.append(num)
                
            indexs.sort()
            nums.sort()
            
            n = len(nums)
            for i, num in zip(indexs, nums):
                res[i] = num
                
        
        return res