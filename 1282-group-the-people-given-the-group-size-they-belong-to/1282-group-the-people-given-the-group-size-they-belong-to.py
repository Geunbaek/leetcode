class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        g = [(size, i) for i, size in enumerate(groupSizes)]
        g.sort(reverse=True)
        answer = []
        
        while g:
            answer.append([])
            for i in range(g[-1][0]):
                answer[-1].append(g.pop()[1])
                
        return answer
                
            
        