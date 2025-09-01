class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = []

        for p, t in classes:
            now = p / t
            _next = (p + 1) / (t + 1)
            heappush(h, (-(_next - now), p + 1, t + 1))

        for _ in range(extraStudents):
            av, p, t = heappop(h)
            now = p / t
            _next = (p + 1) / (t + 1)
            heappush(h, (-(_next - now), p + 1, t + 1))

        total = 0
        n = len(h)
        while h:
            _, p, t = heappop(h)
            total += (p - 1) / (t - 1)

        return total / n

