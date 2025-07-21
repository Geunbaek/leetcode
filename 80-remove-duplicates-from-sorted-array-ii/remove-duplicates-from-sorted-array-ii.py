class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        prev = -float('inf')
        duplicate_count = 0
        cnt = 0

        for num in nums:
            if num == prev:
                if duplicate_count < 2:
                    duplicate_count += 1
                    nums[i] = num
                    i += 1
                else:
                    duplicate_count += 1
                    cnt += 1
            else:
                nums[i] = num
                prev = num
                i += 1
                duplicate_count = 1
        return n - cnt
