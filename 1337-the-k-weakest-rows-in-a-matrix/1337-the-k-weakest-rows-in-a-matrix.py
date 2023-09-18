class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        
        for i, row in enumerate(mat):
            arr.append((row.count(1), i))
            
        arr.sort()
        return list(map(lambda x: x[1], arr))[:k]
        
        