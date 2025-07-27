class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        def isHill(_prev, now, _next):
            return _prev < now and _next < now

        def isValley(_prev, now, _next):
            return _prev > now and _next > now

        def expand(now):
            value = nums[now]
            l, r = now, now
            while l >= 0 or r < n:
                flag = False
                if l >= 0 and nums[l] == value:
                    flag = True
                    l -= 1
                
                if r < n and nums[r] == value:
                    flag = True
                    r += 1
                
                if not flag:
                    break
            return l, r
    
        n = len(nums)
        answer = 0
        visited = [0 for _ in range(n)]

        for i, num in enumerate(nums):
            l, r = expand(i)
            if l < 0 or r >= n:
                continue

            if visited[i]:
                continue

            if isHill(nums[l], num, nums[r]) or isValley(nums[l], num, nums[r]):
                answer += 1
                for i in range(l, r):
                    visited[i] = 1
        return answer