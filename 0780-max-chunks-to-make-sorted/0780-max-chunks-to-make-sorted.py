class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        def check_sorted_arr(arr):
            left = start_index
            right = start_index + len(arr)
            return [num for num in range(left, right)] == sorted(arr)
        
        n = len(arr)
        answer = 0

        temp = []
        start_index = 0

        for i, num in enumerate(arr):
            temp.append(num)
            if check_sorted_arr(temp):
                temp.clear()
                answer += 1
                start_index = i + 1

        if temp:
            answer += 1
        return answer
            
        