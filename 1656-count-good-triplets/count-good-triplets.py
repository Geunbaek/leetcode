class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        def is_good_triplets(i, j, k):
            if not (i < j < k):
                return False

            if not (abs(arr[i] - arr[j]) <= a):
                return False

            if not (abs(arr[j] - arr[k]) <= b):
                return False

            if not (abs(arr[i] - arr[k]) <= c):
                return False
            
            return True
        
        answer = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if is_good_triplets(i, j, k):
                        answer += 1

        return answer