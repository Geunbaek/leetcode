class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def get_min_diff(x, y):
            nums = set()
            for ny in range(y, y + k):
                for nx in range(x, x + k):
                    nums.add(grid[ny][nx])

            sorted_num = sorted(nums)
            min_diff = math.inf

            for n1, n2 in zip(sorted_num, sorted_num[1:]):
                min_diff = min(min_diff, abs(n1 - n2))

            return 0 if len(sorted_num) == 1 else min_diff                  

        r, c = len(grid), len(grid[0])
        ans = []
        for y in range(r - k + 1):
            ans.append([])
            for x in range(c - k + 1):
                ans[-1].append(get_min_diff(x, y))
        return ans

