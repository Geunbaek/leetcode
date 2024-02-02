class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        arr = [str(i) for i in range(1, 10)]
        digits = []
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                digit = "".join(arr[i: j + 1])
                digits.append(int(digit))
                
        ans = []
        
        for digit in digits:
            if low <= digit <= high:
                ans.append(digit)
        return sorted(ans)
                