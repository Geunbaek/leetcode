class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cache = {}
        self.food_map = {}
        self.renewal = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = cuisine

            if cuisine not in self.cache:
                self.cache[cuisine] = []

            heappush(self.cache[cuisine], (-rating, food))

            if cuisine not in self.renewal:
                self.renewal[cuisine] = {}
            
            self.renewal[cuisine][food] = rating

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_map[food]
        self.renewal[cuisine][food] = newRating
        heappush(self.cache[cuisine], (-newRating, food))
        
    def highestRated(self, cuisine: str) -> str:
        while self.cache[cuisine]:
            rating, food = heappop(self.cache[cuisine])

            if self.renewal[cuisine][food] != -rating:
                continue
            heappush(self.cache[cuisine], (rating, food))
            return food    


        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)