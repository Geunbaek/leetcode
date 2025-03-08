class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        answer = n

        for i in range(n - k + 1):
            w = blocks[i: i + k].count("W")
            answer = min(answer, w)

        return answer