class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        num_cnt = Counter(nums)
        
        keys = sorted(num_cnt.keys())

        memo = dict()

        def dp(now):
            if now in memo:
                return memo[now]

            ret = 1
            if num_cnt[now] >= 2 and now * now in num_cnt:
                ret = dp(now * now) + 2
            memo[now] = ret
            return ret
        answer = 0
        for key in keys:
            if key == 1:
                if num_cnt[key] % 2 == 0:
                    answer = max(answer, num_cnt[key] - 1)
                else:
                    answer = max(answer, num_cnt[key])
            else:
                answer = max(answer, dp(key))
        return answer