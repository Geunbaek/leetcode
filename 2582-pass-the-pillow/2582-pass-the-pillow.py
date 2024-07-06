class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        answer = 1
        state = 0
        
        for _ in range(time):
            if state == 0:
                answer += 1
                
            if state == 1:
                answer -= 1
                
            if answer == n:
                state = 1
            
            if answer == 1:
                state = 0
            
        return answer