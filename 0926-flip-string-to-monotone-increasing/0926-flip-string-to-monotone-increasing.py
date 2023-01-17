class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        answer = s.count("0")
        count = answer
        for char in s:
            if char == "0":
                count -= 1
                answer = min(answer, count)
            else:
                count += 1
        return answer
            
        