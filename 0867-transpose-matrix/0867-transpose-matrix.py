class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        ret = []
        for x in range(c):
            ret.append([])
            for y in range(r):
                ret[-1].append(matrix[y][x])
                
        return ret
                
        