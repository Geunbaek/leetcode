class Solution:
    def minimumDeletions(self, s: str) -> int:
        prefix_a = [0]
        prefix_b = [0]

        for c in s:
            if c == 'a':
                prefix_a.append(prefix_a[-1] + 1)
                prefix_b.append(prefix_b[-1] + 0)
            else:
                prefix_a.append(prefix_a[-1] + 0)
                prefix_b.append(prefix_b[-1] + 1)
        n = len(s)
        if prefix_a[n] - prefix_a[0] == 0 or prefix_b[n] - prefix_b[0] == 0:
            return 0
        answer = n
        for i in range(1, n + 1):
            answer = min(answer, prefix_b[i - 1] - prefix_b[0] + prefix_a[n] - prefix_a[i])
        return answer