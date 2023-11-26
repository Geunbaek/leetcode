class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        
        for y in range(r):
            for x in range(c):
                if y == 0:
                    continue
                if matrix[y][x] == 0:
                    continue
                matrix[y][x] += matrix[y - 1][x]
  
        answer = 0
        for y in range(r):
            sorted_line = sorted(matrix[y], reverse=True)
                
            area = 0
            _min = float('inf')
            for x in range(c):
                _min = min(_min, sorted_line[x])
                area = max(area, (x + 1) * _min)
            answer = max(answer, area)
            
        return answer
                