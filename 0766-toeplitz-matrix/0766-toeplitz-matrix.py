class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def checkValidToeplitz(x, y):
            target = matrix[y][x]
            while True:
                nx = x + 1
                ny = y + 1
                if nx >= len(matrix[0]) or ny >= len(matrix):
                    return True
                
                if matrix[ny][nx] != target:
                    return False
                
                x = nx
                y = ny
                
        for x in range(len(matrix[0])):
            if not checkValidToeplitz(x, 0):
                return False
        
        for y in range(len(matrix)):
            if not checkValidToeplitz(0, y):
                return False
        
        return True
            
        
        