class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        pattern_map = dict()
        ban = set()
        
        for p, string in zip(pattern, s.split()):
            if p not in pattern_map:
                if string in ban:
                    return False
                pattern_map[p] = string
                ban.add(string)
                continue
            
            if pattern_map[p] != string:
                return False
    
        return True
        