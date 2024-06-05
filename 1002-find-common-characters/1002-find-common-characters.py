class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        temp = Counter(words[0])
        for word in words[1:]:
            count = Counter(word)
            temp &= count
        answer = []
        
        for key, count in temp.items():
            answer += [key] * count
        return answer
            
                
        