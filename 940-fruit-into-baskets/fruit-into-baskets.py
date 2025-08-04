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
        left = 0
        for right in range(n):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1
            total += 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                total -= 1
                left += 1
            
            answer = max(answer, total)

        return answer

        