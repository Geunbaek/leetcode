

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair_cars_in_time(time):
            repair_cars = 0

            for rank in ranks:
                repair_cars += math.floor(math.sqrt(time // rank))

            return repair_cars >= cars
        
        left, right = 0, max(ranks) * cars * cars

        while left <= right:
            mid = (left + right) // 2

            if can_repair_cars_in_time(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left