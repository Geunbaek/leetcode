class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        prev = [0, colors[0]]
        for i, color in enumerate(colors[1:]):
            if color == prev[1]:
                if neededTime[i + 1] > neededTime[prev[0]]:
                    time += neededTime[prev[0]]
                    prev = [i + 1, color]
                else:
                    time += neededTime[i + 1]
            else:
                prev = [i + 1, color]
            print(prev)
        return time
        