class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)   

        counts = []
        for y in range(n):
            cnt = 0
            for x in range(n - 1, -1, -1):
                if grid[y][x] == 1:
                    break
                cnt += 1
            counts.append(cnt)

        now = n - 1
        answer = 0
        for i in range(n - 1):
            for y in range(len(counts)):
                if counts[y] >= now:
                    answer += y
                    counts.pop(y)
                    now -= 1
                    break
            else:
                return -1
        return answer
            

