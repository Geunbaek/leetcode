class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        size = len(s)
        
        for idx in range(1, size // 2 + 1):
            if size % idx == 0:
                restruct_str = s[:idx] * ( size // idx)
                if restruct_str == s:
                    return True
        return False