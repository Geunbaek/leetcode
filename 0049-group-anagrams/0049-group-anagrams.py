from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        answer = []
        
        for string in strs:
            anagram = "".join(sorted(list(string)))
            anagramDict[anagram].append(string)
            
        for key, val in anagramDict.items():
            answer.append(val)
        return answer
        
        
    
        