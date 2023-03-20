class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = [0] + flowerbed + [0]
        count  =0
        for i in range(0, len(flowers) - 2):
            if flowers[i] == 0 and flowers[i + 1] == 0 and flowers[i + 2] == 0:
                count += 1
                flowers[i + 1] = 1
                
        return count >= n        