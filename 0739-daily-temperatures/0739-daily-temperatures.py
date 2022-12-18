class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0 for _ in range(len(temperatures))]
        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                last = stack.pop()
                answer[last[0]] = i - last[0]
            
            stack.append((i, temperature))
        
        return answer