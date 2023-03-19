class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = max(startPos, fruits[-1][0])
        arr = [0 for _ in range(n + 1)]
        for pos, fruit in fruits:
            arr[pos] = fruit
            
            
        prefix = [0]
        temp = 0
        
        for fruit in arr:
            temp += fruit
            prefix.append(temp)
            
        answer = 0
        for right in range(min(k, n - startPos) + 1):
            left = max(0, k - 2 * right)  
            l_pos, r_pos = max(0, startPos - left), startPos + right    
            answer = max(answer, prefix[r_pos + 1] - prefix[l_pos])    
            
        for left in range(min(k, startPos) + 1):
            right = max(0, k - 2 * left)            
            l_pos, r_pos = startPos - left, min(n, startPos + right)     
            answer = max(answer, prefix[r_pos + 1] - prefix[l_pos])
        return answer
    