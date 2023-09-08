class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        
        for i in range(numRows):
            answer.append([1 for _ in range(i + 1)])
            
        for y in range(2, numRows):
            for x in range(1, len(answer[y]) - 1):
                answer[y][x] = answer[y - 1][x - 1] + answer[y - 1][x]
                
        return answer
                
            
        