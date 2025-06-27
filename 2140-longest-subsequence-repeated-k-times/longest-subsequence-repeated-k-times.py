class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        candidate = sorted(
            [char for char, count in Counter(s).items() if count >= k],
            reverse=True
        )
        q = deque(candidate)

        answer = ""

        while q:
            now = q.popleft()

            if len(now) > len(answer):
                answer = now

            for c in candidate:
                _next = now + c
                it = iter(s)
                for ch in _next * k:
                    if ch not in it:
                        break
                else:
                    q.append(_next)

        return answer
