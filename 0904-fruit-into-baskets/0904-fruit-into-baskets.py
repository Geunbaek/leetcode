from collections import deque
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = {}
        temp = deque()
        count = 0
        answer = 0
        
        for fruit in fruits:
            counter[fruit] = counter.get(fruit, 0) + 1
            temp.append(fruit)
            count += 1
            
            while temp and counter and len(counter) > 2:
                first = temp.popleft()
                counter[first] -= 1
                count -= 1
                if counter[first] == 0:
                    del counter[first]
      
            answer = max(answer, count)
            
        return answer
                    
                
        