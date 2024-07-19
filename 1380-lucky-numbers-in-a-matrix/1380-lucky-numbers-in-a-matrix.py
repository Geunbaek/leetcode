class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r, c = len(matrix), len(matrix[0])
        
        def getColMax(x):
            _max = 0
            for y in range(r):
                _max = max(_max, matrix[y][x])
            return _max
        
        answer = []
        for y in range(r):
            row_min = min(matrix[y])
            for x in range(c):
                col_max = getColMax(x)
                target = matrix[y][x]
                if target == row_min and target == col_max:
                    answer.append(target)
                    
        return answer
        