class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dxys = {
            "N": [0, -1],
            "S": [0, 1],
            "E": [1, 0],
            "W": [-1, 0],
        }
        
        x, y = 0, 0
        p = set([(x, y)])
        
        for char in path:
            dx, dy = dxys[char]
            nx = x + dx
            ny = y + dy
            
            if (nx, ny) in p:
                return True
            
            p.add((nx, ny))
            x, y = nx, ny
            
        return False
        
        