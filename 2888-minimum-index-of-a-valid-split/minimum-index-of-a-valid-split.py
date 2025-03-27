class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        cache = Counter(nums)
        now = Counter()
        for i in range(n - 1):
            num = nums[i]
            cache[num] -= 1
            now[num] += 1

            # now_most, now_count = now.most_common(1)[0]
            # most, count = cache.most_common(1)[0]
            if 2 * now[num] > i + 1 and 2 * cache[num] > n - i - 1: 
                return i
        return -1
