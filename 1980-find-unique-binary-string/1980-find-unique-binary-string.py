class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def recur(binary):
            if len(answer) >= 1:
                return
            
            if len(binary) > n:
                return
            
            if binary and int(binary, 2) not in cache:
                answer.append(binary)
                return
    
            recur("0" + binary)
            recur("1" + binary)
            
        
        n = len(nums[0])
        cache = {
            int(num, 2) for num in nums
        }
        answer = []
        recur("")
        return answer[0].zfill(n)
        
        
        