class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0 for _ in range(len(temperatures))]
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                last = stack.pop()
                answer[last] = i - last
            
            stack.append(i)
        
        return answer