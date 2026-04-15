class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        answer = float("inf")
        n = len(words)
        for i in range(n):
            if words[i] == target:
                if startIndex < i:
                    answer = min(answer, abs(startIndex - i), abs(n - i + startIndex))
                else:
                    answer = min(answer, abs(startIndex - i), abs(n - startIndex + i))

        if answer == float("inf"):
            return -1
        return answer