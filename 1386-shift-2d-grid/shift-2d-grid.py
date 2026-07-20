class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(grid), len(grid[0])

        ret = deque()

        for y in range(r):
            for x in range(c):
                ret.append(grid[y][x])

        ret.rotate(k)
        ret = list(ret)
        answer = []

        for y in range(r):
            answer.append(ret[c * y: (c * y) + c])
        return answer

