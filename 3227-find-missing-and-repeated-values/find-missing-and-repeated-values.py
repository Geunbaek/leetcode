class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        cache = defaultdict(int)

        n = len(grid)
        answer = []

        for y in range(n):
            for x in range(n):
                cache[grid[y][x]] += 1

                if cache[grid[y][x]] == 2:
                    answer.append(grid[y][x])

        for i in range(1, n * n + 1):
            if i not in cache:
                answer.append(i)
                break
        return answer