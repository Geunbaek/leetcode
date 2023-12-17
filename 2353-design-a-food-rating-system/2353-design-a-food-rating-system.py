from sortedcontainers import SortedSet
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = dict()
        self.rating_info = defaultdict(dict)
        self.food_cache = dict()
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = {
                "cuisine": cuisine,
                "rating": rating
            }
            
            if cuisine not in self.rating_info[rating]:
                self.rating_info[rating][cuisine] = SortedSet()
                
            self.rating_info[rating][cuisine].add(food)
            
            if cuisine not in self.food_cache:
                self.food_cache[cuisine] = SortedSet()
                
            self.food_cache[cuisine].add(rating)
            
    def changeRating(self, food: str, newRating: int) -> None:
        current_rating = self.food_info[food]['rating']
        current_cuisine = self.food_info[food]['cuisine']
        
        self.rating_info[current_rating][current_cuisine].remove(food)
        
        if current_cuisine not in self.rating_info[newRating]:
            self.rating_info[newRating][current_cuisine] = SortedSet()
            
        self.rating_info[newRating][current_cuisine].add(food)
        
        if len(self.rating_info[current_rating][current_cuisine]) == 0:
            self.food_cache[current_cuisine].remove(current_rating)
        
        self.food_cache[current_cuisine].add(newRating)
        
        self.food_info[food]['rating'] = newRating
        
        
        

    def highestRated(self, cuisine: str) -> str:
        food_rating = self.food_cache[cuisine][-1]
        
        return self.rating_info[food_rating][cuisine][0]
            
            
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)