class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alpha = [0 for _ in range(26)]

        for i, c in enumerate(s):
            alpha[ord(c) - ord('a')] = i

        start, end = 0, 0
        answer = []

        for i, c in enumerate(s):
            end = max(end, alpha[ord(c) - ord('a')])
            if end == i:
                answer.append(i - start + 1)
                start = i + 1

        return answer