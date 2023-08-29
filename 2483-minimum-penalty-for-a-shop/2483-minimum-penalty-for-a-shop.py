class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count("Y")
        _min = penalty
        
        answer = 0
        
        for i in range(len(customers)):
            customer = customers[i]
            if customer == "Y":
                penalty -= 1
            else:
                penalty += 1
                
            if _min > penalty:
                answer = i + 1
                _min = penalty
                
        return answer
                
        