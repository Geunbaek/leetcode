

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check():
            for key, value in count_t.items():
                if now[key] < value:
                    return False
            return True
        
        count_t = Counter(t)
        now = defaultdict(int)
        _min = len(s)
        answer = ""
        
        left = 0
        for right, char in enumerate(s):
            now[char] += 1 
            
            while check():
                if _min > right - left:
                    _min = right - left
                    answer = s[left: right + 1]
                    
                left_char = s[left]
                now[left_char] -= 1
                left += 1
                
        return answer
            
                
        
        
        
        