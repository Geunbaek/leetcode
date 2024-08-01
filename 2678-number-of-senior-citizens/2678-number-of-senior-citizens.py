class Solution:
    def countSeniors(self, details: List[str]) -> int:
        answer = 0
        
        for detail in details:
            age = int(detail[-4: -2])
        
            if age > 60:
                answer += 1
        return answer