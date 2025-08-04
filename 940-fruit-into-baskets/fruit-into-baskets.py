class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        def canHold(basket, fruitType, limit):
            if len(basket) < limit:
                return True

            if fruitType in basket:
                return True

            return False

        n = len(fruits)
        basket = {}

        total = 0
        answer = 0
        right = 0
        for left in range(n):
            while right < n and canHold(basket, fruits[right], 2):
                basket[fruits[right]] = basket.get(fruits[right], 0) + 1
                total += 1
                right += 1
            
            answer = max(answer, total)
            basket[fruits[left]] -= 1
            total -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]


        return answer

        