class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        _min = min(nums)
        _max = max(nums)
        min_i = nums.index(_min)
        max_i = nums.index(_max)
        n = len(nums)
        if n == 1:
            return n

        answer = 0

        l = min_i if min_i < max_i else max_i
        r = max_i if min_i < max_i else min_i
        print(l, r)
        if l + 1 < n - r:
            answer += l + 1
            r -= l + 1
            n -= l + 1
            answer += min(n - r, r + 1)
        else:
            answer += n - r
            n -= (n - r)
            answer += min(l + 1, n - l)

        return answer
        

