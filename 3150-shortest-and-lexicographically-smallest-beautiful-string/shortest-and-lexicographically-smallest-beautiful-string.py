class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        answer = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                if s[i: j].count('1') == k:
                    answer.append(s[i: j])
                    break

        answer.sort(key = lambda x: (len(x), x))
        if not answer:
            return ""
        return answer[0]