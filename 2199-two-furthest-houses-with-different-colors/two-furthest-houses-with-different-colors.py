class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        min_dists = {}

        answer = 0
        for i in range(len(colors)):
            if colors[i] not in min_dists:
                min_dists[colors[i]] = i

            for key, j in min_dists.items():
                if key == colors[i]:
                    continue
                answer = max(answer, i - j)

        return answer