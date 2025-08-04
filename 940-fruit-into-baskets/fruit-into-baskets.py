class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        def canHold(basket, fruitType, limit):
            if len(basket) < limit:
                return True

            if fruitType in basket:
                return True
            return False

        def getTotal(basket):
            total = 0
            for value in basket.values():
                total += value

            return total


        n = len(fruits)
        basket = {}

        answer = 0
        right = 0
        for left in range(n):
            while right < n and canHold(basket, fruits[right], 2):
                if fruits[right] not in basket:
                    basket[fruits[right]] = 0
                basket[fruits[right]] += 1
                right += 1
            
            answer = max(answer, getTotal(basket))
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]


        return answer

        