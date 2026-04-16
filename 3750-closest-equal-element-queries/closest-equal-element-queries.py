class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        cache = defaultdict(list)
        memo = [float('inf') for _ in range(n)]
        for i in range(n):
            num = nums[i]
            if len(cache[num]) > 0:
                memo[i] = min(memo[i], i - cache[num][-1])
                memo[cache[num][-1]] = min(memo[cache[num][-1]], i - cache[num][-1])
            cache[num].append(i)
        
        for i in range(n):
            num = nums[i]
            if len(cache[num]) > 0:
                memo[i] = min(memo[i], n - cache[num][-1] + i)
                memo[cache[num][-1]] = min(memo[cache[num][-1]], n - cache[num][-1] + i)
            cache[num].append(i)
        answer = []
        for q in queries:
            if memo[q] == float('inf') or memo[q] >= n:
                answer.append(-1)
            else:
                answer.append(memo[q])
        return answer