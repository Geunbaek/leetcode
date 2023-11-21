class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        cache = defaultdict(int)
        
        for num in nums:
            rev = int(str(num)[::-1])
            cache[num - rev] += 1
        
        ans = 0
        MOD = 1_000_000_007
        for val in cache.values():
            for i in range(1, val):
                ans += i
                ans %= MOD
                
        return ans
        