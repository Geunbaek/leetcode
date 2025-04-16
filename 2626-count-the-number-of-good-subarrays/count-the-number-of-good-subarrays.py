class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        def check(cache):
            ret = 0
            for key, val in cache.items():
                if val <= 1:
                    continue
                ret += math.factorial(val - 1)
            return ret


        answer = 0

        right = -1
        cache = defaultdict(int)
        count = 0
        
        for left in range(len(nums)):
            while right + 1 < len(nums) and count < k:
                right += 1
                count += cache[nums[right]]
                cache[nums[right]] += 1

            if count >= k:
                answer += len(nums) - right
                
            cache[nums[left]] -= 1
            count -= cache[nums[left]]

        return answer
