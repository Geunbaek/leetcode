class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        answer = ""
        for word in words:
            answer += chr(ord('z') - (sum([weights[ord(c) - ord('a')] for c in word]) % 26))
                
        return answer