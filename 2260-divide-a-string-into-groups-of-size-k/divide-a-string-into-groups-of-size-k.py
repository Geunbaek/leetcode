class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        answer = []
        now = ""

        for c in s:
            if len(now) >= k:
                answer.append(now)
                now = ""
            
            now += c

        if now:
            answer.append(now.ljust(k, fill))
        return answer