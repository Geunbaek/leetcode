class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        answer = [1 for _ in range(n)]
        
        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                answer[i + 1] = max(answer[i + 1], answer[i] + 1)
                
        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                answer[i] = max(answer[i + 1] + 1, answer[i])
        
        return sum(answer)
    
