class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = []
        target = deque(target)
        num = 1
        
        while target:
            first = target.popleft()
            while num != first:
                num += 1
                answer.append("Push")
                answer.append("Pop")
                
            num += 1
            answer.append("Push")
            
        return answer
            
            
            
        