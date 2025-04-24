class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        counter = Counter(nums)
        m = len(counter)
        n = len(nums)

        cache = {}
        left = 0
        answer = 0

        for right in range(n):
            now = nums[right]
            cache[now] = cache.get(now, 0) + 1

            while len(cache) == m:
                answer += n - right

                first = nums[left]
                cache[first] = cache.get(first) - 1

                if cache[first] == 0:
                    del cache[first]
                
                left += 1
       
        return answer

            