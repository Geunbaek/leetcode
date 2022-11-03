from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = defaultdict(int)
        answer = 0
        
        for word in words:
            if counter[word[::-1]] > 0: 
                counter[word[::-1]] -= 1
                answer += 4
            else: 
                counter[word] += 1
                
        for key, val in counter.items(): 
            if val > 0 and key == key[::-1]: 
                break
        else:
            return answer
        
        return answer + 2
                