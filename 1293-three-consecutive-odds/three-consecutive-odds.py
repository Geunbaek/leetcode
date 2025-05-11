class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_counts = 0

        for num in arr:
            if num % 2 == 0:
                odd_counts = 0
                continue
            
            odd_counts += 1
            if odd_counts == 3:
                return True

        return False