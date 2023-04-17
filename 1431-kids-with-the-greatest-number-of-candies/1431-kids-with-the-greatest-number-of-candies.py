class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _max = max(candies)
        answer = []
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= _max:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer