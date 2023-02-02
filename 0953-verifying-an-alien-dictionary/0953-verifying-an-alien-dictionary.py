from functools import cmp_to_key
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def orderOper(x, y):
            for c1, c2 in zip(x, y):
                if orderMap[c1] > orderMap[c2]:
                    return 1
                elif orderMap[c1] < orderMap[c2]:
                    return -1
            if len(x) > len(y):
                return 1
            elif len(x) < len(y):
                return -1
            else:
                return 0
                
        orderMap = {}
        
        for i, char in enumerate(order):
            orderMap[char] = i
        
        return words == sorted(words, key=cmp_to_key(orderOper))
            
        